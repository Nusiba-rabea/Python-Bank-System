from bank import *

def main():

    while True:

        print("""
========== Welcome To Python Bank ==========
1. Register
2. Login
3. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()

        elif choice == "2":
            username = login()

            if username:
                bank_menu(username)

        elif choice == "3":
            print("Thank you for using Python Bank.")
            break

        else:
            print("Invalid choice.")


main()