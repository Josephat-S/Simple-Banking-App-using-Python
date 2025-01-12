# For showing the balance
def show_balance(balance):
    return f"{balance:.2f}"

# For depositing
def deposit():
    amount = float(input("Enter amount you want to deposit \n"))
    if amount < 0:
        print("==============================")
        print("Invalid amount!")
        print("==============================")
        return 0
    else:
        print("==============================")
        print(f"You have deposited ${amount:.2f}, your new balance is ${balance + amount}")
        return amount

# For withdrawing
def withdraw():
    amount = float(input("Enter amount you want to withdraw \n"))
    if amount > balance:
        print("==============================")
        print(f"Insufficient amount")
        return 0
    elif amount < 0:
        print("==============================")
        print("Invalid amount!")
        return 0
    else:
        print("==============================")
        print(f"You have withdrawn ${amount:.2f}, your new balance is ${balance - amount}")
        return amount

# Variable for running
is_running = True
# Variable for balance
balance = 0.0
# Lopp for the program
while is_running:
    print("==============================")
    print("Banking application")
    print("==============================")
    print("1: Show balance")
    print("2: Deposit")
    print("3: Withdraw")
    print("4: Exit")
    # Input to enter the action number 
    action = input("Enter a number for action \n")
    print("==============================")
    # Selecting purpose
    if action == "1":
        print("==============================")
        print("Your balance is $", show_balance(balance))
    elif action == "2":
        balance += deposit()
    elif action == "3":
        balance -= withdraw()
    elif action == "4":
        is_running = False
    else:
        print("Invalid input")

# Ending message
print("==============================")
print("THANK YOU FOR USING OUR SYSTEM!")
print("==============================")

