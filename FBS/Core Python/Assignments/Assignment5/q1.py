id = "admin"
password = "1234"

for i in range(3):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == id and password == password:
        print("Login successful!")
        break
    else:
        print("Incorrect User ID or Password")

else:
    print("You have used all 3 attempts.")
    print("Program terminated.")
