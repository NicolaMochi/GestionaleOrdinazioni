# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginGuiwfKLzG.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ui_login(object):
    def setupUi(self, ui_login):
        if not ui_login.objectName():
            ui_login.setObjectName(u"ui_login")
        ui_login.resize(328, 369)
        ui_login.setMinimumSize(QSize(328, 369))
        ui_login.setMaximumSize(QSize(328, 369))
        font = QFont()
        font.setFamily(u"Dubai")
        ui_login.setFont(font)
        ui_login.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.wrap = QWidget(ui_login)
        self.wrap.setObjectName(u"wrap")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wrap.sizePolicy().hasHeightForWidth())
        self.wrap.setSizePolicy(sizePolicy)
        self.frame_input = QFrame(self.wrap)
        self.frame_input.setObjectName(u"frame_input")
        self.frame_input.setGeometry(QRect(40, 60, 241, 241))
        self.frame_input.setStyleSheet(u"background-color: rgb(250, 250, 250);\n"
"border: 0.1px solid transparent;\n"
"border-radius: 20px")
        self.frame_input.setFrameShape(QFrame.StyledPanel)
        self.frame_input.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.frame_input)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(40, 30, 141, 21))
        self.label_title.setStyleSheet(u"color: black;\n"
"font: 700 22pt \"Dubai\";")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.lineEdit_username = QLineEdit(self.frame_input)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setGeometry(QRect(40, 90, 161, 41))
        self.lineEdit_username.setStyleSheet(u"border-bottom: 1.5px solid black;\n"
"border-radius: 0px;\n"
"color: rgb(21, 21, 21);\n"
"font:  16px \"Dubai\";\n"
"letter-spacing: 0.4px;")
        self.lineEdit_password = QLineEdit(self.frame_input)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setGeometry(QRect(40, 150, 161, 41))
        self.lineEdit_password.setStyleSheet(u"border-bottom: 1.5px solid black;\n"
"border-radius: 0px;\n"
"color: rgb(21, 21, 21);\n"
"font:  16px \"Dubai\";\n"
"letter-spacing: 0.4px;")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.label_message = QLabel(self.frame_input)
        self.label_message.setObjectName(u"label_message")
        self.label_message.setGeometry(QRect(40, 60, 151, 16))
        self.label_message.setStyleSheet(u"font: 11pt \"Dubai\";")
        self.btn_enter = QPushButton(self.wrap)
        self.btn_enter.setObjectName(u"btn_enter")
        self.btn_enter.setGeometry(QRect(90, 280, 131, 41))
        self.btn_enter.setStyleSheet(u"color: white;\n"
"font: 9pt \"Dubai\";\n"
"background-color: #fd4902;\n"
"font-size: 18px;\n"
"border:  0.1px solid transparent;\n"
"border-radius: 10px;\n"
"font-weight: 500;")
        ui_login.setCentralWidget(self.wrap)

        self.retranslateUi(ui_login)

        QMetaObject.connectSlotsByName(ui_login)
    # setupUi

    def retranslateUi(self, ui_login):
        ui_login.setWindowTitle(QCoreApplication.translate("ui_login", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("ui_login", u"Bentornato", None))
        self.lineEdit_username.setText(QCoreApplication.translate("ui_login", u"Username", None))
        self.lineEdit_password.setText(QCoreApplication.translate("ui_login", u"Password", None))
        self.label_message.setText(QCoreApplication.translate("ui_login", u"Scrivi utente e password", None))
        self.btn_enter.setText(QCoreApplication.translate("ui_login", u"Entra", None))
    # retranslateUi

