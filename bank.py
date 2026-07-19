users = {}
# Function Register
def register():
    username = input("Enter username: ").strip()
    if username == "":
        print("Username cannot be empty.")
    elif username in users:
        print("Username already exists.")
    else:
        password = input("Enter password: ").strip()
        if not password or len(password) < 6:
            print("Password must be at least 6 characters.")
        else:
            users[username] = {
                "password": password,
                "balance": 0.0
            }
            print("Account created successfully.")
# Function Login
def login():
    username = input("Enter username: ").strip()
    if username in users:
        password = input("Please enter password: ").strip()
        if password == users[username]["password"]:
            print("Login successful")
            return username
        else:
            print("Incorrect password")
            return None
    else:
        print("Username does not exist.")
        return None
# Show balance
def check_balance(username):
    print(f"Your Balance: {users[username]['balance']} EGP")
# Add money
def deposit(username):
    amount = float(input("Enter money: "))
    if amount > 0:
        users[username]["balance"] += amount
        print("Deposit successful.")
    else:
        print("Amount must be greater than zero.")
# Withdraw money
def withdraw(username):
    amount = float(input("Enter amount: "))
    if amount > 0:
        if amount > users[username]["balance"]:
            print("Insufficient balance.")
        else:
            users[username]["balance"] -= amount
            print("Withdraw successful.")
    else:
        print("Amount must be greater than zero.")
# Transfer money
def transfer(username):
    recipient = input("Enter recipient username: ").strip()
    # Check recipient exists
    if recipient not in users:
        print("Recipient does not exist.")
        return
    # Check self transfer
    if recipient == username:
        print("You cannot transfer money to yourself.")
        return
    amount = float(input("Enter amount to transfer: "))
    # Check amount
    if amount <= 0:
        print("Invalid amount.")
        return
    # Check balance
    if users[username]["balance"] < amount:
        print("Insufficient balance.")
        return
    # Transfer
    users[username]["balance"] -= amount
    users[recipient]["balance"] += amount
    print("Transfer successful.")
# Change password
def change_password(username):
    current_password = input("Enter current password: ").strip()
    if current_password == users[username]["password"]:
        new_password = input("Enter new password: ").strip()
        if len(new_password) >= 6:
            users[username]["password"] = new_password
            print("Password changed successfully.")
        else:
            print("Password must be at least 6 characters.")
    else:
        print("Incorrect password.")
# Bank Menu
def bank_menu(username):
    while True:
        print("""
========== Bank Menu ==========
1. Check Balance
2. Deposit
3. Withdraw
4. Transfer
5. Change Password
6. Logout
""")
        choice = input("Enter your choice: ")
        if choice == "1":
            check_balance(username)
        elif choice == "2":
            deposit(username)
        elif choice == "3":
            withdraw(username)
        elif choice == "4":
            transfer(username)
        elif choice == "5":
            change_password(username)
        elif choice == "6":
            print("Logged out successfully.")
            break
        else:
            print("Invalid choice.")