correct_username = "admin"
correct_password = "1234"
attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful! - smartlogin.py:10")
        break
    else:
        attempts += 1
        print("Invalid credentials. Attempts left: - smartlogin.py:14", 3 - attempts)

if attempts == 3:
    print("Account Locked due to 3 failed attempts. - smartlogin.py:17")
