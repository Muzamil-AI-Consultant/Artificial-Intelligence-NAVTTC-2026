import bankcore
import accounts

def main():
    print("****** Welcome to ABC Bank *******")

    while True:
        print("1: Create Account")
        print("2: Login")
        print("3: Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter name: ")
            password = input("Enter password: ")
            bankcore.create_account(name, password)

        elif choice == "2":
            cid = input("Enter Customer ID: ")
            password = input("Enter password: ")
            if bankcore.login(cid, password):

                while True:

                    print("1: Check Balance")
                    print("2: Deposit")
                    print("3: Withdraw")
                    print("4: Logout")

                    op = input("Enter option: ")

                    if op == "1":
                        print("Balance:", accounts.check_balance(cid))

                    elif op == "2":
                        amount = float(input("Enter amount: "))
                        accounts.deposit(cid, amount)

                    elif op == "3":
                        amount = float(input("Enter amount: "))
                        accounts.withdraw(cid, amount)

                    elif op == "4":
                        print("Logout successful")
                        break

                    else:
                        print("Invalid option")

        elif choice == "3":
            print("Thank you for using ABC Bank")
            break

        else:
            print("Invalid choice")


main()