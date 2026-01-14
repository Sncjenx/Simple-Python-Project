import math

## circle
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference1 of the circle is: {round(circumference, 2)}")

radius = float(input("Enter radius of a circle: "))
area = math.pi * pow(radius, 2)
print(f"The area of the circle is {round(area)}cm")

a = float(input("enter side a : "))
b = float(input("enter side b : "))

c= math.sqrt(pow(a ,2) + pow(b, 2))
print(c)