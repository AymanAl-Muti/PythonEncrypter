#Creates an function that encrypts the password like an website
#So it takes a Password and then adds a key to it
#It will have a normal password like Ayman123
#Then it will turn it to gture234 as an example


import re
def encrypt(password):
    # Makes an arrat of the password
    a_password = list(password)

    #Creates an empty variable to use it later
    na_ecrypted = ""

    # Goes through the array depending on the length of the array then goes through each one
    for i in range(len(a_password)):
        #Turns each letter in the array to a ascii
        o_ecrypted = ord(a_password[i])

        #We are creating a variable that takes the ascii number and adds 3 to it
        ecrypted =  o_ecrypted + 3

        #creates a variable that joins its empty self plus the character so the first character plus its empty self etc.
        na_ecrypted += chr(ecrypted)

    #Returns out the whole thing as a string
    return(na_ecrypted)

def Validate(password):
    boole = False
    a_password = list(password)
    ascii = 48
    ascii1 = 57
    msg = ""

    p_length = len(password)

    if p_length >= 6 or re.search("[A-Z]",password) or re.search("[!@#$%^&*]",password) or re.search("[0-9]",password):
        boole = True

    if not p_length >= 6:
         print("Your Password is shorter than 6")
         boole = False

    if not re.search("[A-Z]",password):
         print("Please Type a capital letter")
         boole = False

    if not re.search("[!@#$%^&*]",password):
         print("Please enter a Special character")
         boole = False

    if not re.search("[0-9]",password):
         print("Please enter a number")
         boole = False

    return(boole)