
name = input("what is your name")
age = input("what is your age")

age = int(age)
age =age + 1


print(f"Hello {name}")
print("HAPPY BIRTHDAY")
print(f"your are {age} years old")


#exercise 1 rectangle Area calc

length = float(input("enter the length"))
width = float(input("Enter the width"))
area = length * width
print(f"the area is {area} cm")

# exercise 2 Shopping Cart Program
item = input("what item would you like to buy")
price = float(input("What is the price"))
quantiy = int(input("how many would you like to buy"))
total = price * quantiy

print(f"you have bought {quantiy} of {item}")
print(f"your total is {total}$")

