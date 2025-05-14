username = input("Enter your username:")
password = input("Enter your password:")

is_valid = bool(username) and bool(password)

if is_valid:
    print("Username and password are both provided.")
else:
    print("Either username or password is empty.")
