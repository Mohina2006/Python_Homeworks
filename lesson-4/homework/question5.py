password = input("Enter your password: ")
has_upper = False

if len(password) < 8:
    print("Password is too short.")
else:
    for char in password:
        if char.isupper():
            has_upper = True
            break

    if not has_upper:
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")
