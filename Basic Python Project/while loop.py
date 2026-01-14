

#name = input("Enter your name: ")
#while name == "":
  #  print("Name is empty")
  #  name = input("Enter your name: ")
#else:
  #  print(f"hello {name}!")


#age = int(input("Enter your age: "))

#while age < 0 or age > 100:
 #   print("age must be between 0 and 100")
 #   age = int(input("Enter your age: "))
#else:
  #  print(f"you are {age}year old")


#food = input("Enter food: (q to quit): ")

#while not food == "q":
   # print(f"you like {food}")
   # food = input("Enter food you like (q to quit): ")
   # print("bye")



num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valide")
    num = int(input("Enter a number between 1 and 10: "))

    print(f"your number is {num}")