#imports the required libraries
from encrypt import *
import csv
import pandas as pd
import datetime

#Asks the user for their creditentials they want to be inputed
print("Please enter a username")
username = input()

print("Please enter a password")
password = input()

#It then sees if the passwords meets the requirments else it will ask you to enter a new one
while Validate(password) == False:
    password = input("Enter A New Password: ")

#it then ecrypts the password with a key.
e_password = encrypt(password)

#prints the encrypted password to check if its done correctly
print(e_password)

#it nows has a header on the top of the CSV file
Header = ["UserName","Password"]
now = datetime.datetime.now()

#it opens the CSV file in read mode as a CSV file
with open('Info1.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    
    #it stores the contents of the CSV file in a variable
    data = list(reader)
    data_us = [item[0] for item in data]
    
    #Here it checks if the username already exists, if so now ask the user for a new username
    for i in range(len(data_us)):
        while data_us[i] == username:
            print("UserName already exists")
            username = input("Please enter a new username: ")

    passwords = [item[1] for item in data]
    dates = [item[2] for item in data]

    #print(data_us)
    #print(passwords)
    #print(dates)
    
#Opens the CSV file in append mode to add new information to it
with open('Info1.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    
    #now it adds the username, the encrypted password, and the current time into the file
    Info = [username, e_password, now.strftime("%Y-%m-%d %H:%M:%S")]
    
    #writes the actual information
    writer.writerow(Info)

#closes the CSV file
csvFile.close()
