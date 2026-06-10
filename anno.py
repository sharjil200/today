password = "lala200"
enter_pass = input("Enter your password: ")

while enter_pass != password:
    enter_pass = input("Wrong password please try again: ")

print("Congratulations! You have entered the correct password.")
