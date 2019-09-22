"""
This file has only Main program i.e. A UI that prompts for username and password.On succesful login, It choses 
Admin or user, based on credentials (adm or user) Program Operation varies.

"""

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







