"""
This file contains actual class implemetation.
All validations are performed here.
cx_Oracale is used for oracle database.
User and password validation, only admin can add or update user details,
existing username cannot be used as new username are the main properties of this program.
"""

import re
import cx_Oracle
class Login:

    def getUserName(self):
        self.__userName=input("Enter User Name :")
        return self.__userName
    def getPassword(self):
        self.__password = input("Enter Password :")
        return self.__password

    def authenticate_user(self,userName,password):
        try:
            con = cx_Oracle.connect("system/mohameme@localhost:1521/orcl")
            print("Connection Succesfull")
        except:
            print("Connection Failed")
        cur=con.cursor()
        cur.execute("select user_category,username from library_users where username=:1 and password=:2",(userName,password))
        try:
            user = cur.fetchone()[0]
            return user
        except:
            return "False"
    def validateUsername(self,userName):
        if len(userName) >6 and len(userName) <15 and userName.isalnum():
            return True
        else:
            return False

    def validatePassword(self,password):

        if len(password) >8:
            length=1
        else:
            length=0

        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if (regex.search(password) == None):
            specialchr=0
        else:
            specialchr=1
        upper=0
        lower=0
        digit=0
        for i in password:
            if i.isupper():
                upper=1
            if i.islower():
                lower=1
            if i.isdigit():
                digit=1
        print(length,upper,lower,specialchr)
        if length and upper and lower and specialchr and digit:
            return 1
        else:
            return 0

    def createUser(self):
        userName=self.getUserName()
        userValidation=self.validateUsername(userName)
        if userValidation:
            password=self.getPassword()
            passwordValidation=self.validatePassword(password)
            if passwordValidation:
                userCategory=input("Enter User Catogory {ADM / STU}")
                try:
                    con = cx_Oracle.connect("system/mohameme@localhost:1521/orcl")
                    print("Connection Succesfull")
                except:
                    print("Connection Failed")
                cur = con.cursor()
                cur.execute("select count(*) from library_users")
                fixture_count = cur.fetchone()[0]+1
                cur.execute("insert into library_users values(:1,:2,:3,:4)",(userCategory,userName,password,fixture_count))
                con.commit()
                con.close()
            else:
                print("Password must match below conditions:")
                print("Minimum 8 charecters, must have atleast one upper case,one lower case and a digit")
                self.createUser()

        else:
            print("Username must match below conditions:")
            print("Username mush have more than 6 charecter and less than 10 charecters and should be alphanumeric")
            self.createUser()
    def updateUser(self):
        pass
