import bankcore
import accounts
import init

def main():
    print("******Welcome to ABC Bank*******")

    while True:
        print("1. Create an account")
        print("2. Login to the account")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            password = input("Enter password: ")
            bankcore.create_account(name, password)

        elif choice == "2":
            customer_id = input("Enter Customer ID: ")
            password = input("Enter password: ")

            if bankcore.login(customer_id, password):

                while True:
                    print("1. Check Balance")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Logout")

                    option = input("Enter option: ")

                    if option == "1":
                        print("Balance:", accounts.check_balance(customer_id))

                    elif option == "2":
                        amount = float(input("Enter amount: "))
                        accounts.deposit(customer_id, amount)

                    elif option == "3":
                        amount = float(input("Enter amount: "))
                        accounts.withdraw(customer_id, amount)

                    elif option == "4":
                        print("Logged out")
                        break

                    else:
                        print("Invalid option")

        elif choice == "3":
            print("Thank you for using ABC Bank")
            break

        else:
            print("Invalid choice")


main()