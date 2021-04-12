from encrypt import *
import csv
import pandas as pd
import datetime

print("Please enter a username")
username = input()
print("Please enter a password")
password = input()

while Validate(password) == False:
    password = input("Enter A New Password: ")


e_password = encrypt(password)


print(e_password)

Header = ["UserName","Password"]
now = datetime.datetime.now()

with open('Info1.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    data = list(reader)
    data_us = [item[0] for item in data]

    for i in range(len(data_us)):
        while data_us[i] == username:
            print("UserName already exists")
            username = input("Please enter a new username: ")

    passwords = [item[1] for item in data]
    dates = [item[2] for item in data]

    #print(data_us)
    #print(passwords)
    #print(dates)

with open('Info1.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    Info = [username, e_password, now.strftime("%Y-%m-%d %H:%M:%S")]
    writer.writerow(Info)

csvFile.close()