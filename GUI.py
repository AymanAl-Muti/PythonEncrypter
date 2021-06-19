from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from database import addToDatabase, isPassUsed

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(544, 455)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Starting Text telling you to login!
        self.sText = QtWidgets.QLabel(self.centralwidget)
        self.sText.setGeometry(QtCore.QRect(180, 80, 181, 41))
        self.sText.setFont(QtGui.QFont('Arial', 12))
        self.sText.setObjectName("sText")
        self.sText.setText("Welcome! Please login")

        #username Input
        self.usernameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameInput.setGeometry(QtCore.QRect(190, 130, 141, 16))

        #password input
        self.passwordInput = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordInput.setGeometry(QtCore.QRect(190, 160, 141, 16))
        self.passwordInput.setObjectName("passwordInput")

        #Text saying that the username already exists, will be shown only when the username entered already exists
        self.usernameTakenText = QtWidgets.QLabel(self.centralwidget)
        self.usernameTakenText.setStyleSheet('color: red')
        self.usernameTakenText.setText("Sorry, username has already been used.")
        self.usernameTakenText.setGeometry(QtCore.QRect(183, 240, 250, 30))
        self.usernameTakenText.hide()


        def onLoginClick():
            addToDatabase(self.usernameInput.text(), self.passwordInput.text(), False)
            print(isPassUsed)
            print(self.usernameInput.text(), self.passwordInput.text())

        #Login Button taking you to "You logged in!" page
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(230, 190, 75, 23))
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setText("Login")


        #Register button taking you to registration page
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(230, 220, 75, 23))
        self.registerButton.setObjectName("registerButton")
        self.registerButton.setText("Register")
        self.registerButton.clicked.connect(onLoginClick)

        MainWindow.setCentralWidget(self.centralwidget)



#runs and shows the application
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())