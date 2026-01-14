
age = int(input("Enter your age: "))

if age >= 100:
   print("you are to old ")
elif age >= 18:
    print("You are sign up ")
elif age < 0:
    print("you are not born yet")
else:
    print("You are not sign up ")

responses = input("would you like food (Y/N)? ")
if responses == "Y" :
    print("have some food")
elif responses == "N" :
    print("alr you dont need food anyway")


name = input("enter your name")
if name == "":
   print("you did not enter a name ")
else:
    print(f"Hello {name}")

online = True

if online:
    print("user is online")
else:
    print("user is offline")






