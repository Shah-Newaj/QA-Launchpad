password = input("Enter Your Password:" )

if(len(password)) < 8:
    print("Password is invalid, Should be at-least 8 characters")
else:
    print("Password is Valid")