username = input("Enter username: ")
password = input("Enter password: ")

def validate_login():
    if (len(password)) < 8:
        print("Password is invalid, Should be at-least 8 characters")
    else:
        print("Welcome", username)

validate_login()