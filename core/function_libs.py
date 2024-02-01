import string
import random
import pandas as pd
from core.account import Account


def email_generator():
    """
    Function to generate a random email
    :return: email
    """
    email_chars = string.ascii_letters + string.digits
    account = "".join([random.choice(email_chars) for _ in range(random.randint(5, 10))])
    domain = random.choice(["gmail.com", "outlook.com"])
    return f"{account}@{domain}"


def password_generator():
    """
    Function to generate a password
    :return: password
    """
    pass_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password_chars = [random.choice(pass_chars) for _ in range(random.randint(3, 10))]
    password_chars.append(random.choice(string.ascii_uppercase))
    password_chars.append(random.choice(string.ascii_lowercase))
    password_chars.append(random.choice(string.digits))
    password_chars.append(random.choice(string.punctuation))
    random.shuffle(password_chars)
    return "".join(password_chars)


def get_account_info():
    """
    Function to get a random account in data file
    :return: account with info
    """
    account = Account()
    print(f"Getting account data.")
    data = pd.read_excel("core/account.xls")
    account_index = random.randint(0, len(data))
    account.email = data["Email"][account_index]
    account.password = data["Password"][account_index]
    account.first_name = data["First_Name"][account_index]
    account.last_name = data["Last_Name"][account_index]
    account.phone = data["Phone"][account_index]
    account.country = data["Country"][account_index]
    account.address = data["Address"][account_index]
    account.city = data["City"][account_index]
    account.state = data["State"][account_index]
    account.postcode = data["Postcode"][account_index]
    return account
