def validate_username(username):
    if username[0].isdigit() or not username[0].isalnum():
        return False
    if "@" not in username or "." not in username.split("@")[-1]:
        return False
    if "@." in username:
        return False
    return True

def validate_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in "!@#$%^&*" for c in password):
        return False
    return True

def register():
    while True:
        username = input("Enter email: ")
        if validate_username(username):
            break
        print("Invalid email format")

    while True:
        password = input("Enter password: ")
        if validate_password(password):
            break
        print("Weak password")

    with open("users.txt", "a") as file:
        file.write(f"{username}:{password}\n")

    print("Registration successful")

def login():
    username = input("Enter email: ")
    password = input("Enter password: ")

    with open("users.txt", "r") as file:
        users = file.readlines()

    for user in users:
        stored_user, stored_pass = user.strip().split(":")
        if username == stored_user and password == stored_pass:
            print("Login successful")
            return

    print("Invalid credentials")
    forgot = input("Forgot password? (yes/no): ")

    if forgot.lower() == "yes":
        forgot_password()

def forgot_password():
    username = input("Enter registered email: ")

    with open("users.txt", "r") as file:
        users = file.readlines()

    for user in users:
        stored_user, stored_pass = user.strip().split(":")
        if username == stored_user:
            print("Your password is:", stored_pass)
            return

    print("User not found. Please register.")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
