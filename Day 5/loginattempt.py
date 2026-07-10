correct_password=input("enter the password: ")
for i in range (3):
    password=input("Enter the password: ")
    if correct_password==password:
        print("login succesful:")
        break
    else:
        print("Login failed")
if password!= correct_password:
    print("access denied")        