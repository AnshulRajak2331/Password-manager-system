# Password Manager System

import random
import string

passwords = {}
try:
    with open ("passwords.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(": ")
            passwords[website] = pwd
except:
    pass

def generatePwd():
    chars = string.ascii_letters + string.digits + "@#$%&"
    password = "".join(random.choice(chars) for i in range(8)) # 8 digit pwd
    print(f"Your Generated password: {password}")
    print("Password saved...")



while True:
    print(''' --------Password Manager System---------
            1. Save Password
            2. View Password
            3. Generate Password
            4. Exit''' )
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        site = input("Enter your website: ")
        pwd= input("Enter your Password: ")
        passwords[site] = pwd
        with open("passwords.txt", "a") as file:
            file.write(f"{site} : {pwd} \n")

        print("Password saved...")

    elif choice == 2:
        if not passwords :
            print("No Password saved...")
        else:
            for site, pwd in passwords.items():
                print(site, ":" ,pwd)
    
    elif choice == 3:
        generatePwd()
    
    elif choice == 4:
        print("Exiting...")
        break
    else:
        print("Invalid Choice!")

    


