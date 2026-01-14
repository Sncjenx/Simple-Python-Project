


principle = 0
rate = 0
time = 0


while True :
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("principle cant be less than  0")
    else:
        break

while True:
    rate = float(input("Enter the interest rate amount: "))
    if rate < 0:
        print("rate cant be less than  0")
    else:
        break

while True:
    time = int(input("Enter the time amount: "))
    if time < 0:
        print("time cant be less than  0")
    else:
        break

print(principle)
print(rate)
print(time)


total = principle *pow((1 + rate / 100), time)
print(f"balance after {time}years/s ${total:.2f}")
