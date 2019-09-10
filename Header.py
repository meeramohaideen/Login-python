from Login import Login

log=Login()


print("Enter Username and password to login:")
userName=log.getUserName()
password=log.getPassword()

user_category=log.authenticate_user(userName,password)



if user_category=='ADM':
    print("""
    WELCOME ADMIN
    1.Create User
    2.Update User
    """)
    option=int(input("Enter Option:"))
    if option==1:
        log.createUser()
    elif option==2:
        log.updateUser()

elif user_category=='STU':
    print("STUDENT/USER")
else:
    print("Login Failed")
# if userValidation:
#
#     passwordValidation = log.validatePassword(password)
#     print(passwordValidation)
#     if passwordValidation==0:
#         print("Password must match below conditions:")
#         print("Minimum 8 charecters, must have atleast one upper case,one lower case and a digit")
#
#
# else:
#
#
# if userValidation and passwordValidation:
#     print("Login Successful")






