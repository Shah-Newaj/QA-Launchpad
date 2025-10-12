# step4_login_function.py

def validate_login(username, password):
    if not username or not password:
        # print("Username and password are required.")
        return "Username and password are required."
    elif len(password) < 8:
        return "Password must be at least 8 characters long."
        # print("Password is invalid, Should be at-least 8 characters")
    else:
        return f"Welcome, {username}!"

# Test the function
print(validate_login("tester", "pass1234"))
print(validate_login("qw", "12"))
