import pygame
import sys


pygame.init()

screen_width = 800
screen_height = 800

screen = pygame.display.set_mode((screen_height,screen_width))
pygame.display.set_caption('Calculator')

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit




pygame.display.update()
clock.tick(60)