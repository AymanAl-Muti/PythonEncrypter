import mysql.connector
import datetime

isPassUsed = False

def addToDatabase(username,password, isUserUsed):
    now = datetime.datetime.now()

    myDB = mysql.connector.connect(user="root",
                            host="localhost",
                            password = "ayman7865",
                            database="creditentials")

    myCursor = myDB.cursor()

    sqlCommand = "INSERT INTO logininfo (username, password, timeOfCreation) VALUES (%s,%s, %s)"

    #Checks to see if username already exists;  it pulls all the usernames and puts them into a list
    myCursor.execute("SELECT username FROM logininfo")
    res = myCursor.fetchall()

    #it then pulls each element from the list and then pulls the text from the element to check if it exists, if yes then ask again for a new one
    for i in range(len(res)):
        text = res[i]
        if username == text[0]:
            isUserUsed = True

            '''
            print("Username already exists please try again: ")
            username = input()
            '''


    informationTuple = (username, password,now.strftime("%Y-%m-%d") )

    myCursor.execute(sqlCommand, informationTuple)

    myDB.commit()

