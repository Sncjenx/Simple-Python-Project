

unit = input(" Is this temperature in celsius or Fahrenheit?(C/F) ")
temp = float(input("enter the temperature "))


if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is : {round(temp, 1)} F")
elif unit == "F":
    temp = round((temp - 32) * 5/9, 1)
    print(f"The temperature in Celsius is :  {round(temp, 1)} C")
else :
    print(f"{unit} is not a valid unit")
