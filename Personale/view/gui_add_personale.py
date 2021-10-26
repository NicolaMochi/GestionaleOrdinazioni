# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_add_personaleyWKKVX.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class gui_add_personale(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 393)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 16pt \"Dubai\";\n"
"color: black;\n"
"letter-spacing: 0.5px;\n"
"")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_top = QFrame(Dialog)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_top)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_amministratore = QCheckBox(self.frame_top)
        self.checkBox_amministratore.setObjectName(u"checkBox_amministratore")
        self.checkBox_amministratore.setStyleSheet(u"font: 400 13pt \"Dubai\";")
        self.checkBox_amministratore.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.checkBox_amministratore, 4, 0, 1, 1)

        self.lineEdit_nome_personale = QLineEdit(self.frame_top)
        self.lineEdit_nome_personale.setObjectName(u"lineEdit_nome_personale")
        self.lineEdit_nome_personale.setMinimumSize(QSize(50, 0))
        self.lineEdit_nome_personale.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_nome_personale.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"background-color:transparent;\n"
"padding: 4px;")

        self.gridLayout.addWidget(self.lineEdit_nome_personale, 0, 0, 1, 1)

        self.lineEdit_cognome_personale = QLineEdit(self.frame_top)
        self.lineEdit_cognome_personale.setObjectName(u"lineEdit_cognome_personale")
        self.lineEdit_cognome_personale.setMinimumSize(QSize(50, 0))
        self.lineEdit_cognome_personale.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_cognome_personale.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"background-color:transparent;\n"
"padding: 4px;")

        self.gridLayout.addWidget(self.lineEdit_cognome_personale, 0, 1, 1, 1)

        self.lineEdit_password_personale = QLineEdit(self.frame_top)
        self.lineEdit_password_personale.setObjectName(u"lineEdit_password_personale")
        self.lineEdit_password_personale.setMinimumSize(QSize(50, 0))
        self.lineEdit_password_personale.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_password_personale.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"background-color:transparent;\n"
"padding: 4px;")

        self.gridLayout.addWidget(self.lineEdit_password_personale, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_bottom = QFrame(Dialog)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setMaximumSize(QSize(16777215, 70))
        self.frame_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_confirm_new_personale = QPushButton(self.frame_bottom)
        self.btn_confirm_new_personale.setObjectName(u"btn_confirm_new_personale")
        self.btn_confirm_new_personale.setStyleSheet(u"QPushButton{ border: none;\n"
"background-color: qlineargradient(spread:pad, x1:0.596045, y1:0.649, x2:1, y2:0.994, stop:0 rgba(99, 159, 171, 248), stop:1 rgba(255, 255, 255, 215));\n"
"font: 500 12pt \"Dubai\";\n"
"padding: 9px;\n"
"letter-spacing:0.2px ;\n"
"border-radius: 5px;\n"
"color:white;\n"
"margin-right: 5px;}\n"
"QPushButton:focus:pressed{font: 500 9.5pt \"Dubai\";\n"
"	background-color: rgb(99, 159, 171);}\n"
"QPushButton:hover{background-color:rgb(99, 159, 171);}\n"
"/*rgb(99, 159, 171)*/")

        self.horizontalLayout.addWidget(self.btn_confirm_new_personale)

        self.btn_close_new_personale = QPushButton(self.frame_bottom)
        self.btn_close_new_personale.setObjectName(u"btn_close_new_personale")
        self.btn_close_new_personale.setStyleSheet(u"QPushButton{ border: none;\n"
"background-color: qlineargradient(spread:pad, x1:0.596045, y1:0.649, x2:1, y2:0.994, stop:0 rgba(99, 159, 171, 248), stop:1 rgba(255, 255, 255, 215));\n"
"font: 500 12pt \"Dubai\";\n"
"padding: 9px;\n"
"letter-spacing:0.2px ;\n"
"border-radius: 5px;\n"
"color:white;\n"
"margin-right: 5px;}\n"
"QPushButton:focus:pressed{font: 500 9.5pt \"Dubai\";\n"
"	background-color: rgb(99, 159, 171);}\n"
"QPushButton:hover{background-color:rgb(99, 159, 171);}\n"
"/*rgb(99, 159, 171)*/")

        self.horizontalLayout.addWidget(self.btn_close_new_personale)


        self.verticalLayout.addWidget(self.frame_bottom)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nuovo Dipendente", None))
        self.checkBox_amministratore.setText(QCoreApplication.translate("Dialog", u"Amministratore", None))
        self.lineEdit_nome_personale.setPlaceholderText(QCoreApplication.translate("Dialog", u"Nome", None))
        self.lineEdit_cognome_personale.setPlaceholderText(QCoreApplication.translate("Dialog", u"Cognome", None))
        self.lineEdit_password_personale.setText(QCoreApplication.translate("Dialog", u"Prima password", None))
        self.lineEdit_password_personale.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.btn_confirm_new_personale.setText(QCoreApplication.translate("Dialog", u"Aggiungi", None))
        self.btn_close_new_personale.setText(QCoreApplication.translate("Dialog", u"Annulla", None))
    # retranslateUi

