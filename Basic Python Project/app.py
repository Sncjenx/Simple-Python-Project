import pygame
import math
import random
import sys
import warnings

# Suppress the pkg_resources deprecation warning from pygame
warnings.filterwarnings("ignore", category=UserWarning, module="pygame.pkgdata")

# -------- Config --------
LOGICAL_W, LOGICAL_H = 320, 180
WINDOW_W, WINDOW_H   = 960, 540
TITLE                = "Pygame Starter: Polished & Scalable"
BG_COLOR             = (20, 22, 25)
GRID_COLOR           = (40, 44, 50)
FPS_TARGET           = 60

# -------- Helpers --------
def clamp(v, lo, hi): return max(lo, min(hi, v))
def centered_rect(w, h, cx, cy):
    r = pygame.Rect(0, 0, w, h)
    r.center = (cx, cy)
    return r

# -------- Render scaling --------
class RenderTarget:
    def __init__(self, logical_w, logical_h):
        self.logical_w = logical_w
        self.logical_h = logical_h
        self.surface = pygame.Surface((logical_w, logical_h)).convert()
        self.scale = 1
        self.offset = (0, 0)

    def update_layout(self, window_size):
        ww, wh = window_size
        sx = ww // self.logical_w
        sy = wh // self.logical_h
        self.scale = max(1, min(sx, sy))
        scaled_w = self.logical_w * self.scale
        scaled_h = self.logical_h * self.scale
        ox = (ww - scaled_w) // 2
        oy = (wh - scaled_h) // 2
        self.offset = (ox, oy)

    def present(self, screen):
        screen.fill(BG_COLOR)
        scaled = pygame.transform.scale(
            self.surface,
            (self.logical_w * self.scale, self.logical_h * self.scale)
        )
        screen.blit(scaled, self.offset)

# -------- Scene base --------
class Scene:
    def __init__(self, game): self.game = game
    def enter(self): pass
    def exit(self): pass
    def handle_event(self, e): pass
    def update(self, dt): pass
    def draw(self, surf): pass

# -------- Title scene --------
class TitleScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.font_big = pygame.font.SysFont(None, 48)
        self.font_small = pygame.font.SysFont(None, 24)

    def handle_event(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key in (pygame.K_SPACE, pygame.K_RETURN):
                self.game.change_scene(GameplayScene(self.game))
            elif e.key == pygame.K_f:
                self.game.toggle_fullscreen()
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            self.game.change_scene(GameplayScene(self.game))

    def draw(self, surf):
        draw_grid(surf)
        title = self.font_big.render("Pygame Starter", True, (220, 230, 240))
        subtitle = self.font_small.render(
            "Press Space / Click to Start • F to toggle fullscreen",
            True, (150, 160, 170)
        )
        surf.blit(title, centered_rect(title.get_width(), title.get_height(), LOGICAL_W/2, LOGICAL_H/2 - 20))
        surf.blit(subtitle, centered_rect(subtitle.get_width(), subtitle.get_height(), LOGICAL_W/2, LOGICAL_H/2 + 20))

# -------- Gameplay scene --------
class GameplayScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.SysFont(None, 18)
        self.player = Player(LOGICAL_W//2, LOGICAL_H//2)
        self.collectibles = []
        self.spawn_collectibles(8)
        self.paused = False
        self.score = 0

    def spawn_collectibles(self, n):
        self.collectibles = []
        margin = 16
        for _ in range(n):
            x = random.randint(margin, LOGICAL_W - margin)
            y = random.randint(margin, LOGICAL_H - margin)
            self.collectibles.append(Collectible(x, y))

    def handle_event(self, e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                self.paused = not self.paused
            elif e.key == pygame.K_r and not self.paused:
                self.player.reset()
                self.spawn_collectibles(8)
                self.score = 0
            elif e.key == pygame.K_f:
                self.game.toggle_fullscreen()

    def update(self, dt):
        if self.paused: return
        keys = pygame.key.get_pressed()
        self.player.update(dt, keys)
        before = len(self.collectibles)
        self.collectibles = [c for c in self.collectibles if not c.collide(self.player)]
        if len(self.collectibles) < before:
            self.score += 1
        if not self.collectibles:
            self.spawn_collectibles(8)

    def draw(self, surf):
        draw_grid(surf)
        for c in self.collectibles: c.draw(surf)
        self.player.draw(surf)
        hud = self.font.render(f"FPS: {self.game.fps:.0f} | Score: {self.score}", True, (170, 180, 190))
        surf.blit(hud, (6, 6))
        if self.paused:
            overlay = pygame.Surface((LOGICAL_W, LOGICAL_H), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 140))
            surf.blit(overlay, (0, 0))
            ptxt = pygame.font.SysFont(None, 36).render("Paused", True, (230, 230, 230))
            surf.blit(ptxt, centered_rect(ptxt.get_width(), ptxt.get_height(), LOGICAL_W/2, LOGICAL_H/2))

# -------- Entities --------
class Player:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.vx, self.vy = 0.0, 0.0
        self.size = 8
        self.accel = 180.0
        self.drag = 0.85
        self.max_speed = 220.0
        self.color = (120, 200, 255)

    def reset(self):
        self.x, self.y = LOGICAL_W//2, LOGICAL_H//2
        self.vx, self.vy = 0.0, 0.0

    def update(self, dt, keys):
        ax = ay = 0.0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:  ax -= self.accel
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: ax += self.accel
        if keys[pygame.K_UP] or keys[pygame.K_w]:    ay -= self.accel
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:  ay += self.accel
        self.vx += ax * dt
        self.vy += ay * dt
        self.vx *= (self.drag if ax == 0 else 1.0)
        self.vy *= (self.drag if ay == 0 else 1.0)
        sp = math.hypot(self.vx, self.vy)
        if sp > self.max_speed:
            scale = self.max_speed / sp
            self.vx *= scale; self.vy *= scale
        self.x += self.vx * dt; self.y += self.vy * dt
        self.x = clamp(self.x, self.size, LOGICAL_W - self.size)
        self.y = clamp(self.y, self.size, LOGICAL_H - self.size)

    def draw(self, surf):
        pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), self.size)

class Collectible:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.r = 5
        self.color = (255, 205, 90)

    def collide(self, player):
        return math.hypot(self.x - player.x, self.y - player.y) < (self.r + player.size)

    def draw(self, surf):
        pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), self.r)

# -------- Visuals --------
def draw_grid(surf, cell=16):
    surf.fill(BG_COLOR)
    w, h = surf.get_size()
    for x in range(0, w, cell):
        pygame.draw.line(surf, GRID_COLOR, (x, 0), (x, h))
    for y in range(0, h, cell):
        pygame.draw.line(surf, GRID_COLOR, (0, y), (w, y))

# -------- Game core --------
class Game:
     