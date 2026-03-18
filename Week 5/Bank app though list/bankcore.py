branch_id = 2057

# users list -> [customer_id, name, password]
users_info = []


def create_account(name, password):

    user_number = len(users_info) + 1
    customer_id = str(branch_id) + "-" + str(user_number)

    users_info.append([customer_id, name, password])

    print("Account created successfully")
    print("Your Customer ID:", customer_id)

    return customer_id


def login(customer_id, password):

    for user in users_info:

        if user[0] == customer_id and user[2] == password:
            print("Login successful")
            return True

    print("Invalid login")
    return False