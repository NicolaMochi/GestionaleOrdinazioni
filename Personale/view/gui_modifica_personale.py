# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_modifica_personaleauPVwP.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class gui_modifica_personale(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 393)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 400, 80))
        self.frame.setMaximumSize(QSize(16777215, 80))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(30, 10, -1, 0)
        self.label_message = QLabel(self.frame)
        self.label_message.setObjectName(u"label_message")
        self.label_message.setStyleSheet(u"font: 10pt \"Poppins\";\n"
"color: rgb(120, 120, 120);")

        self.gridLayout_2.addWidget(self.label_message, 1, 0, 1, 1)

        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setMaximumSize(QSize(16777215, 40))
        self.label_title.setStyleSheet(u"font: 700 19pt \"Poppins\";\n"
"color: #1921FA;\n"
"letter-spacing: 0.5px;\n"
"")

        self.gridLayout_2.addWidget(self.label_title, 0, 0, 1, 1)

        self.btn_elimina_personale = QPushButton(self.frame)
        self.btn_elimina_personale.setObjectName(u"btn_elimina_personale")
        self.btn_elimina_personale.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_elimina_personale.setStyleSheet(u"QPushButton{\n"
"font: 400 11pt \"Poppins\";\n"
"letter-spacing:0.2px ;\n"
"border: none;\n"
"color:#1921FA;}\n"
"QPushButton:hover{text-decoration: underline}\n"
"/*rgb(99, 159, 171)*/")

        self.gridLayout_2.addWidget(self.btn_elimina_personale, 1, 1, 1, 1)

        self.frame_top = QFrame(Dialog)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setGeometry(QRect(0, 80, 400, 313))
        self.frame_top.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top.setStyleSheet(u"\n"
"background-color: rgb(255, 255, 255);")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_top)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 0, 10, 0)
        self.lineEdit_nome_personale = QLineEdit(self.frame_top)
        self.lineEdit_nome_personale.setObjectName(u"lineEdit_nome_personale")
        self.lineEdit_nome_personale.setMinimumSize(QSize(50, 0))
        self.lineEdit_nome_personale.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_nome_personale.setStyleSheet(u"color: #000;\n"
"font: 400 12pt \"Poppins\";\n"
"border: solid;\n"
"border-bottom: 2px solid black;")

        self.gridLayout.addWidget(self.lineEdit_nome_personale, 1, 0, 1, 1)

        self.lineEdit_cognome_personale = QLineEdit(self.frame_top)
        self.lineEdit_cognome_personale.setObjectName(u"lineEdit_cognome_personale")
        self.lineEdit_cognome_personale.setMinimumSize(QSize(50, 0))
        self.lineEdit_cognome_personale.setMaximumSize(QSize(150, 16777215))
        font = QFont()
        font.setFamily(u"Poppins")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.lineEdit_cognome_personale.setFont(font)
        self.lineEdit_cognome_personale.setStyleSheet(u"color: #000;\n"
"font: 400 12pt \"Poppins\";\n"
"border: solid;\n"
"border-bottom: 2px solid black;")

        self.gridLayout.addWidget(self.lineEdit_cognome_personale, 1, 1, 1, 1)

        self.btn_close_new_personale = QPushButton(self.frame_top)
        self.btn_close_new_personale.setObjectName(u"btn_close_new_personale")
        self.btn_close_new_personale.setStyleSheet(u"QPushButton{\n"
"font: 600 12pt \"Poppins\";\n"
"padding: 6px;\n"
"letter-spacing:0.2px ;\n"
"border-radius: 5px;\n"
"color:#1921FA;\n"
"margin-right: 5px;}\n"
"QPushButton:hover{text-decoration: underline}\n"
"/*rgb(99, 159, 171)*/")

        self.gridLayout.addWidget(self.btn_close_new_personale, 7, 1, 1, 1)

        self.checkBox_amministratore = QCheckBox(self.frame_top)
        self.checkBox_amministratore.setObjectName(u"checkBox_amministratore")
        font1 = QFont()
        font1.setFamily(u"Poppins")
        font1.setPointSize(13)
        self.checkBox_amministratore.setFont(font1)
        self.checkBox_amministratore.setStyleSheet(u"")
        self.checkBox_amministratore.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.checkBox_amministratore, 6, 0, 1, 1)

        self.lineEdit_password_personale = QLineEdit(self.frame_top)
        self.lineEdit_password_personale.setObjectName(u"lineEdit_password_personale")
        self.lineEdit_password_personale.setMinimumSize(QSize(50, 0))
        self.lineEdit_password_personale.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_password_personale.setStyleSheet(u"color: #000;\n"
"font: 400 12pt \"Poppins\";\n"
"border: solid;\n"
"border-bottom: 2px solid black;")
        self.lineEdit_password_personale.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEdit_password_personale, 2, 0, 1, 1)

        self.btn_confirm_new_personale = QPushButton(self.frame_top)
        self.btn_confirm_new_personale.setObjectName(u"btn_confirm_new_personale")
        self.btn_confirm_new_personale.setStyleSheet(u"QPushButton{ border: 2px solid #1921FA;\n"
"font: 600 12pt \"Poppins\";\n"
"padding: 6px;\n"
"letter-spacing:0.2px ;\n"
"border-radius: 5px;\n"
"color:#1921FA;\n"
"margin-right: 5px;}\n"
"QPushButton:focus:pressed{background-color: #1921FA; color: #fff;}\n"
"QPushButton:hover{border: none; background-color: #1921FA; color: #fff;}\n"
"/*rgb(99, 159, 171)*/")

        self.gridLayout.addWidget(self.btn_confirm_new_personale, 7, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_message.setText(QCoreApplication.translate("Dialog", u"Modifica o elimina", None))
        self.label_title.setText(QCoreApplication.translate("Dialog", u"Utente", None))
        self.btn_elimina_personale.setText(QCoreApplication.translate("Dialog", u"Elimina utente", None))
        self.lineEdit_nome_personale.setPlaceholderText(QCoreApplication.translate("Dialog", u"Nome", None))
        self.lineEdit_cognome_personale.setPlaceholderText(QCoreApplication.translate("Dialog", u"Cognome", None))
        self.btn_close_new_personale.setText(QCoreApplication.translate("Dialog", u"Annulla", None))
        self.checkBox_amministratore.setText(QCoreApplication.translate("Dialog", u"Amministratore", None))
        self.lineEdit_password_personale.setText("")
        self.lineEdit_password_personale.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.btn_confirm_new_personale.setText(QCoreApplication.translate("Dialog", u"Modifica", None))
    # retranslateUi

