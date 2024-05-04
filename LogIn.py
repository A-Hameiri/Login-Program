# Ariel Hameiri 27/09/2023
# This is a simple login program with a menu of options including
# Login, register new user, generate password.
# And a save file for test data, adding new users and viewing users


import time  # used for  timing the exit
import sys  # used to close the programme
import string  # for use in secure password and other parts of the programme
import random  # for use in the password generator

# creating file and setting parameters to not double up on test file  entries that follow
def matchFile(matchId):
    with open("accounts.txt" "r+") as f:
        data = set(f)
        for match in matchId:
            match += "\n"
            if match not in data:
                f.write(match)



# populating save file with test data
saveFile = open("accounts.txt", "r+")

saveFile.write("fredsmart1 12345678"
                "\njrobertson4 r@=%8(_W=1"
                "\nbob101 1234598"
                "\nmarcusw 3#tr@9dw%4"
                "\npopeyedd 1989eidjce"
                "\njunkman00 p3*(kd8&ld"
                "\nsbj2021 $d5e(ep2(d"
                "\nrobotman 7777Spy007")


data = saveFile.read()  # converting accounts.txt to a variable for matching above

saveFile.close()

def main():
    menu()



def menu():  # defining the main menu

    print("Welcome to the login programme")
# assigning choice variable to user input
    choice = input(""" 
    A: Login
    B: Register
    C: View Accounts
    Q: Exit 
    
    Please enter your choice: """)  # define choice keys

    if choice == "A" or choice == "a":  # define menu options with logical operator
        login()
    elif choice == "B" or choice == "b":
        register()
    elif choice == "C" or choice == "c":
        view()
    elif choice == "Q" or choice == "q":
        close()
    else:
        print("invalid selection please try again")  # loops back to the start of the programme
        menu()

def login():
    notLoggedIn = "true"  # set a variable (boolean type) to be true if the user is NOT logged in
    while notLoggedIn == "true":  # opening the loop
       print("Welcome Please Login")

       with open("accounts.txt", "r") as file:  # open file for reading and defining as variable
           userName = input("Please enter your user name ")  # getting log in credentials and assigning variables
           passWord = input("please enter your password")

           info = file.read()  # defining info variable to read file
           info = info.split()  # defining info variable to read over each line file
           if userName in info:
               index = info.index(userName) + 1  # checking if users name and password are in file
               usr_pw = info[index]
               if usr_pw == passWord:
                   print("Logged in successfully")
                   notLoggedIn = False  # closing the loop

               else:
                   print("login failed")



def register():  # defining registration menu
    print("welcome to the user registration menu")

    option = input("""  
    A: Create password
    B: Generate password
    
    Please enter your choice """)  # define choice keys

    if option == "A" or option == "a":  # define menu options with logical operator
        create()
    elif option == "B" or option == "b":
        generate()
    else:
        print("Invalid selection, please try again")
        register()  # loops back to the beginning of the menu

def create():  #  for password creation
    print("Welcome to the account creator")
    print("Please enter your user name")
    userName = "_"

    while (not userName.isalnum()):  # restricting username to letters and numbers
        userName = input("Letters and numbers only")

    print("Please enter password")
    # setting password charactars to letters, numbers and symbols
    chars = (string.ascii_uppercase + string.ascii_lowercase +
             string.digits + string.punctuation)

    passWord = input("letters, numbers and symbols only")
    if any(x not in chars for x in passWord):  # checking characters are allowed
        print("invalid character")
        create()

    else:
        print("Password accepted")

        saveFile = open("accounts.txt", "a")  # open file to append new log in credentials

        saveFile.write("\n")  # writing new log in credentials to list
        saveFile.write(userName)
        saveFile.write(" ")
        saveFile.write(passWord)

        saveFile.close()

        login() # Loops back to log in now that account has been created


def generate():  # password generator
    print("welcome to the password generator")
    print("Would you like to choose the length or use the default length of 10:")
    #  setting user choices for length type
    pwLen = input(""" 
    1: Choose length
    2: Default length

    Please enter your choice """)

    if pwLen == "1":
          choose()


    elif pwLen == "2":
          default()

    else:
        print("invalid selection")
        generate()  # loops back to the start if invalid entry is made

def choose():
    print("Please enter your username")

    userName = "_"

    while (not userName.isalnum()):  # restricting username to letters and numbers
        userName = input("Letters and numbers only")

    length = int(input("how long would you like the password to be?"))  # asking user for the length
    #  setting user choices of character types or random
    print("""Would you like to choose your characters or use random:  
            1. Digits
            2. Letters
            3. Special characters
            4. Random
            5. Confirm""")

    chars = ""

    while (True):
        choice = int(input("Please enter your choices"))   # user is able to choose character types or random

        if (choice == 1):
            chars += string.digits

        elif (choice == 2):
            chars += string.ascii_lowercase + string.ascii_uppercase

        elif (choice == 3):
            chars += string.punctuation

        elif (choice == 4):
            chars += (string.ascii_uppercase + string.ascii_lowercase
                     + string.digits + string.punctuation)

        elif (choice == 5):  # confirms user choices
            break

        else:
            print("Please pick a valid option")
            choose() # loops back to the start if invalid choice is made


    pwd = []   # assigns users choices to a list
    for i in range(length):
         randomchar = random.choice(chars)  # randomises users choices
         pwd.append(randomchar) # appends to pwd list
    print("".join(pwd))  # displays new password

    saveFile = open("accounts.txt", "a")  # open file to append new log in credentials

    saveFile.write("\n")  # writing new log in credentials to list
    saveFile.write(userName)
    saveFile.write(" ")
    for item in pwd:
        saveFile.write(item)

    saveFile.close()

    login() # loops to login menu now that new account has been made

def default():
    print("Please enter your username")

    userName = "_"

    while (not userName.isalnum()):  # restricting username to letters and numbers
        userName = input("Letters and numbers only")

    length = 10 # setting the password length to the default of 10
    #  setting user choices of character types or random
    print("""Would you like to choose your characters or use random:  
                1. Digits
                2. Letters
                3. Special characters
                4. Random
                5. Confirm""")

    chars = ""

    while (True):
        choice = int(input("Please enter your choices"))  # user is able to choose character types or random

        if (choice == 1):
            chars += string.digits

        elif (choice == 2):
            chars += string.ascii_lowercase + string.ascii_uppercase

        elif (choice == 3):
            chars += string.punctuation

        elif (choice == 4):
            chars += (string.ascii_uppercase + string.ascii_lowercase
                      + string.digits + string.punctuation)

        elif (choice == 5):  # confirms user choices
            break

        else:
            print("Please pick a valid option")
            default()  # loops back to the start if invalid choice is made

    pwd = []  # assigns users choices to a list
    for i in range(length):
        randomchar = random.choice(chars)  # randomises users choices
        pwd.append(randomchar)  # appends to pwd list
    print("".join(pwd))  # displays new password

    saveFile = open("accounts.txt", "a")  # open file to append new log in credentials

    saveFile.write("\n")  # writing new log in credentials to list
    saveFile.write(userName)
    saveFile.write(" ")
    for item in pwd:
        saveFile.write(item)

    saveFile.close()

    login() # loops t login menu now that account has been created


def view():  # for viewing registered accounts
    saveFile = open("accounts.txt", "r")  # open file for reading
    content = saveFile.read()
    print(content)  # output file contents

    saveFile.close()



def close():  # closing function
    print("Closing programme, see you next time. ")
    time.sleep(2)  # setting two-second delay before exit
    sys.exit()


main()











































