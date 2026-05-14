user_name = input("Please enter your name: ")
password = input("Enter your password: ")
password_again = input("Enter your password again: ")

if password == password_again:
    print("you sighned up")
else:
    print("password does not match")

new_name = input("Please enter your new name: ")
new_password = input("Enter your password: ")

if (user_name == new_name) and (password == new_password):
    print("you logged in")

elif password != new_password:
    print("password does not match")

elif user_name != new_name:
    print("your user name does not match")