


def show_balance():
    print("Your balance is:", balance)

def deposit():
    amount = float(input("Enter the amount you want to deposit: "))

def withdraw():
    amount = float(input("Enter the amount you want to withdraw: "))

balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("1.show balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = int(input("Enter your choice(1-4): "))
    if choice == "1":
        show_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Invalid choice")


print("Thank You have a nice day!")



