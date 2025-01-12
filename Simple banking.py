# A method that will be used to show the balance
def show_balance(balance):
    return f"{balance:.2f}"

# A method that will be used to deposit
def deposit():
    amount = float(input("Enter amount you want to deposit \n"))
# Checking if the amount entered is not less than zero
    if amount < 0:
        print("==============================")
        print("Invalid amount!")
        print("==============================")
        return 0
    else:
# If the amount is greater than zero then deposit is acceptable
        print("==============================")
        print(f"You have deposited ${amount:.2f}, your new balance is ${balance + amount}")
        return amount
# A method that will be used for withdrawing
def withdraw():
# The input must be type casted because we're dealing with US currency
    amount = float(input("Enter amount you want to withdraw \n"))
# Checking whether the amount desired to withraw is greater than balance or not
# If true, it means that he/she wamts to withdraw money that they do not have. The progra will terminate
    if amount > balance:
        print("==============================")
        print(f"Insufficient amount")
        return 0
# If the amount is less than zero, the program will terminate
    elif amount < 0:
        print("==============================")
        print("Invalid amount!")
        return 0
# If the balance is greater than amount, then the withdraw process can proceed
    else:
        print("==============================")
        print(f"You have withdrawn ${amount:.2f}, your new balance is ${balance - amount}")
        return amount

# Variable for application running and control
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
# Selecting purposes
# When the action is 1, the it will call show_balance method
    if action == "1":
        print("==============================")
        print("Your balance is $", show_balance(balance))
# When the action is 2, the it will call deposit method
    elif action == "2":
        balance += deposit()
# When the action is 3, the it will call withdraw method
    elif action == "3":
        balance -= withdraw()
# When the action is 4, the program will terminate
    elif action == "4":
        is_running = False
# If the input is invalid, the program will terminate
    else:
        print("Invalid input")

# Ending message
print("==============================")
print("THANK YOU FOR USING OUR SYSTEM!")
print("==============================")
# End of the program