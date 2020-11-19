import sqlite3
import time
from hashlib import sha256
MASTERPW = "dhruv97"
PASSWORD = input("ENTER THE MASTER PASSWORD: ")

while MASTERPW != PASSWORD:
        print("Invalid Password\n")
        break
    
if MASTERPW == PASSWORD:
    print("Welcome Back Dhruv :)")

# Establish connection with the SQLite Database
conn = sqlite3.connect('pass_manager.db')

# combines strings together and return first 15 characters of the hex
# * .encode is used because sha256() requires the string to be encoded before processing it
# * .hexdigest in used bacause sha256() just returns an object, to get the hash of the string, we use .hexdigest() method
def create_password(pass_key, service, admin_pass):
    return sha256(admin_pass.encode('utf-8') + service.lower().encode('utf-8') + pass_key.encode('utf-8')).hexdigest()[:15]

# returns full length hex
def get_hex_key(admin_pass, service):
    return sha256(admin_pass.encode('utf-8') + service.lower().encode('utf-8')).hexdigest()

# Get password of given service from the Database. Returns None if nothing is found in DB.
def get_password(admin_pass, service):
    secret_key = get_hex_key(admin_pass, service)
    cursor = conn.execute("SELECT * from KEYS WHERE PASS_KEY=" + '"' + secret_key + '"')

    file_string = ""
    for row in cursor:
        file_string = row[0]
    if not file_string:
        return
    else:
        return create_password(file_string, service, admin_pass)

# Generates password/hex
# Stores it in DB
def add_password(service, admin_pass):
    secret_key = get_hex_key(admin_pass, service)

    command = 'INSERT INTO KEYS (PASS_KEY) VALUES (%s);' %('"' + secret_key +'"')        
    conn.execute(command)
    conn.commit()
    return create_password(secret_key, service, admin_pass)

if MASTERPW == PASSWORD:
    # creates table if not already existing
    try:
        conn.execute('''CREATE TABLE KEYS
            (PASS_KEY TEXT PRIMARY KEY NOT NULL);''')
        print("Your safe has been created!\nWhat would you like to store in it?")
    except:
        print("You have an existing safe, how would you like to proceed?")
    
    
    while True:
        time.sleep(2)
        print("\n"+ "*"*15)
        print("Commands:")
        print("Press 1 : Generate and store a password")
        print("Press 2 : Retrieve a stored password")
        print("Press 3 : Quit")
        print("*"*15)
        input_ = input(">")

        if input_ == "3":
            break
        if input_ == "1":
            service = input("What is the name of the service?\n:")
            print("\n" + service.capitalize() + " password created: " + add_password(service, MASTERPW))
        if input_ == "2":
            service = input("What is the name of the service?\n:")
            print("Checking password for " + service.capitalize())
            result = get_password(MASTERPW, service)
            if not result:
                print('No password for ' + service.capitalize())
                
            else:
                print('The password for ' + service.capitalize() + ' is ' + result)
            if not result:
                x = input("Would you like to create a password for " + service.capitalize() + " (y/n): ")
                if x.lower() == 'y':
                    print("Password for " + service.capitalize() + " is: " + add_password(service, MASTERPW))
                    # first argument in the above function is for getting the '
                elif x.lower() == 'n':
                    continue
                else:
                    print('Incorrect selection... returning to menu.')
                    continue
