# a loop within another loop
  #outer loop
   # inner loop


rows = int(input("enter number of row: "))
columns = int(input("enter number of columns: "))
symbol = input("enter symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end=" ")
    print()

