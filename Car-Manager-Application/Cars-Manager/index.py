from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType

import sys
from os import path

import mysql.connector
from mysql.connector import errorcode

from manager import MainApp
import xlsxwriter

form_class, _ = loadUiType(path.join(path.dirname(__file__), "main.ui"))
form_class2, _ = loadUiType(path.join(path.dirname(__file__), "login.ui"))


class Login(QMainWindow, form_class2):

    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Login.clicked.connect(self.Handel_Login)
        self.window2 = None

    def Handel_Login(self):

        self.cnx = mysql.connector.connect(user='root', password='Leen2021!',
                                           host='localhost',
                                           database='mydb')
        self.cursor = self.cnx.cursor()

        User_Name = self.txt_User_Name.text()
        Password = self.txt_Password.text()

        user_name = ''' SELECT user_name FROM users '''
        password = ''' SELECT password FROM users '''
        sql = ''' SELECT * FROM users '''
        self.cursor.execute(sql)

        data = self.cursor.fetchall()

        for row in data:

            if row[1] == User_Name and row[2] == Password:

                self.window2 = MainApp()
                self.close()
                self.window2.show()

            else:
                self.label_MMessages.setText("The password or the username is incorrect")



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window = Login()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
