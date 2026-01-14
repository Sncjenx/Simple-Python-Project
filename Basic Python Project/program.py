

foods = []
prices = []
total = 0


while True:
    food = input("Enter food item to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $ "))
        foods.append(food)
        prices.append(price)

print("-----your cart-----")

for food in foods :
    print(food, end=" ")


for price in prices :
    total += price

print()
print(f"your total is : ${total}")

