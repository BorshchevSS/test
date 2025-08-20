login = "BSS"
password = "123"
user_login = input("Enter login: ")

if login == user_login:
    user_password = input("Enter password: ")
    if user_password == password:
        print("Login successful")
    else:
        print("Password incorrect")
else:
    print("Login failed")