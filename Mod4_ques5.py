
def login_system():
    correct_username = "python"
    correct_password = "rule"
    max_attempts = 5
    attempts = 0
    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check if the entered credentials are correct
        if username == correct_username and password == correct_password:
            print("Welcome")
            return
        else:
            print("Incorrect username or password.")
            attempts += 1
            print("Access denied")

login_system()
