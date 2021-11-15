# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerYVcMHQ.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ui_login(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(353, 326)
        MainWindow.setMaximumSize(QSize(353, 326))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(50, 30, 246, 273))
        self.frame.setStyleSheet(u"background-color: #fff;\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(200, 80))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(30, 10, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setStyleSheet(u"color: #000;\n"
"font: 700 20pt \"Poppins\";\n"
"border-radius: 20px;")

        self.verticalLayout_2.addWidget(self.label)

        self.label_message = QLabel(self.frame_2)
        self.label_message.setObjectName(u"label_message")
        self.label_message.setStyleSheet(u"font: 9pt \"Poppins\";\n"
"color: rgb(120, 120, 120);")

        self.verticalLayout_2.addWidget(self.label_message)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 20, 30, 0)
        self.lineEdit_username = QLineEdit(self.frame_3)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setStyleSheet(u"color: #000;\n"
"font: 400 12pt \"Poppins\";\n"
"border-bottom: 2px solid black;")

        self.verticalLayout_3.addWidget(self.lineEdit_username)

        self.lineEdit_password = QLineEdit(self.frame_3)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setStyleSheet(u"color: #000;\n"
"border-bottom: 2px solid black;\n"
"font: 400 12pt \"Poppins\";")
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.lineEdit_password)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.btn_enter = QPushButton(self.frame)
        self.btn_enter.setObjectName(u"btn_enter")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_enter.sizePolicy().hasHeightForWidth())
        self.btn_enter.setSizePolicy(sizePolicy)
        self.btn_enter.setMinimumSize(QSize(0, 0))
        self.btn_enter.setStyleSheet(u"background-color: #ff8c00;\n"
"color: #fff;\n"
"padding: 5px;\n"
"border-radius: 15px;\n"
"font: 500 15pt \"Poppins\";\n"
"margin-bottom: 20px;\n"
"margin-left: 30px;\n"
"margin-right: 30px;")

        self.verticalLayout.addWidget(self.btn_enter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_message.setText(QCoreApplication.translate("MainWindow", u"Inserisci i dati per accedere", None))
        self.lineEdit_username.setText("")
        self.lineEdit_username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btn_enter.setText(QCoreApplication.translate("MainWindow", u"Enter", None))
    # retranslateUi

