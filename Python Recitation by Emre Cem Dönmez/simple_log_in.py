user_info = {"abc": "0000", "emre": "1234", "ahmet": "2222"}

username = input("Enter your username: ")
password = input("Enter your password: ")

while True:
    if username in user_info.keys() and user_info[username] == password:
        print("Authenticated.")
        break

    print("Your username or password is wrong. Try again.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
