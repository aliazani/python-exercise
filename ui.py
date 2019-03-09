# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets


class Form(QDialog):
    def __init__(self):
        super().__init__()
        self.setObjectName("Dialog")
        self.resize(400, 300)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(70, 210, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(60, 130, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 160, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(150, 210, 75, 23))
        self.label.setText("hello")

        self.retranslateUi(self)
        self.pushButton.clicked.connect(self.say_hello)
        QtCore.QMetaObject.connectSlotsByName(self)


    def say_hello(self):
        num1 = self.lineEdit.text()
        num2 = self.lineEdit_2.text()
        val = int(num1) + int(num2)
        self.label.setText(str(val))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))



if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
