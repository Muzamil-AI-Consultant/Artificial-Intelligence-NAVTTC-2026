branch_id = 2057

# dictionary to store users
# {customer_id: {"name": name, "password": password}}
users_info = {}


def create_account(name, password):

    user_number = len(users_info) + 1
    customer_id = str(branch_id) + "-" + str(user_number)

    users_info[customer_id] = {
        "name": name,
        "password": password
    }

    print("Account created successfully")
    print("Customer ID:", customer_id)

    return customer_id


def login(customer_id, password):

    if customer_id in users_info:

        if users_info[customer_id]["password"] == password:
            print("Login successful")
            return True

    print("Invalid login")
    return False