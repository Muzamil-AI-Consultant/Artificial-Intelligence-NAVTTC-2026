balance_record = {}


def check_balance(customer_id):

    return balance_record.get(customer_id, 0)


def deposit(customer_id, amount):

    if customer_id in balance_record:
        balance_record[customer_id] += amount
    else:
        balance_record[customer_id] = amount

    print("Amount deposited successfully")


def withdraw(customer_id, amount):

    balance = balance_record.get(customer_id, 0)

    if balance >= amount:
        balance_record[customer_id] = balance - amount
        print("Withdrawal successful")
    else:
        print("Insufficient balance")