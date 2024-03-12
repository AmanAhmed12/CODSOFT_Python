import random

lower="qwertyuiopasdfghjklzxcvbnm"
upper="QWERTYUIOPASDFGHJKLZXCVBNM"
number="1234567890"
symbols="!@#$%^&*()_}{][/.,|:;-"

def generate_password():
    while True:
        print("\n \n")
        print("----------------- Password Generating System ----------------\n")
        print("Select a password generating  option from below")
        print("1.Simple\n2.Medium\n3.Hard\n4.Exit")
        complexity =input("Enter the option :")

        if complexity =="1":
            length = int(input("Enter the length of the password: "))  # Get length of the password from the user
            all=lower+upper
            password="".join(random.sample(all,length))
            print("password is =",password)
        elif complexity=="2":
            length = int(input("Enter the length of the password: "))  # Get length of the password from the user
            all=lower+upper+number
            password="".join(random.sample(all,length))
            print("password is =",password)
        elif complexity=="3":
            length = int(input("Enter the length of the password: "))  # Get length of the password from the user
            all=lower+upper+number+symbols
            password="".join(random.sample(all,length))
            print("password is =",password)
        elif complexity=="4":
            print("------------Thankyou-------------")
            break
        else:
            print("Invalid Option !!!")



generate_password()