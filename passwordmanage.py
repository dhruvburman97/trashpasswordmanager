#password Manager
import random
import string

#binascii converts between binary and ascii (fuck unicode)

print(string.ascii_letters)
random.choice(string.ascii_letters)

def store_password():
    #username
    username = str(input("Your username: "))
    #website
    website = str(input("Website: "))
    #generate random password       
    digit = int(input("How many digits should the pwd be? [integers only] "))
    password = ""
    for i in range(digit):
        char = random.choice(string.ascii_letters)
        password += char



    #store the password into a file
    f = open("password.txt", "a")                   #open in append mode
    f.write(f"{username}-{website}-{str(password)}\n")     #connecting shit
    f.close()

    print("The password generated randomly is: {password}")

######


def search():
    username_or_site = str(input("Search by username(Type 'username') or Website(Type 'site'? "))
    f = open("password.txt", "r")       #open file in read mode
    for line in f:
        #search by username
        info = line.split("-")
        if username_or_site == "username":
            value = str(input("What's the username to search for? "))
            if value ==  info[0]:
                return info[2]
        else:
            value = str(input("What's the site to search for? "))
            if username_or_site == "site":
                if value == info[1]:
                    return info[2]
            else:
                print("wrong input")


result = search()
if result == None:
    print("No result found")
else:
    print("Your password is: {result}")