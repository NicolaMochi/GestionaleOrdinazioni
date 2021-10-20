# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_add_personalePgYWXi.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide6.QtGui import *
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
        self.checkBox = QCheckBox(self.frame_top)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"font: 400 13pt \"Dubai\";")
        self.checkBox.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.checkBox, 4, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame_top)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(50, 0))
        self.lineEdit_3.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_3.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"background-color:transparent;\n"
"padding: 4px;")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame_top)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(50, 0))
        self.lineEdit.setMaximumSize(QSize(150, 16777215))
        self.lineEdit.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"background-color:transparent;\n"
"padding: 4px;")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame_top)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(50, 0))
        self.lineEdit_2.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_2.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"background-color:transparent;\n"
"padding: 4px;")

        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_top)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(50, 0))
        self.lineEdit_4.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_4.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"background-color:transparent;\n"
"padding: 4px;")

        self.gridLayout.addWidget(self.lineEdit_4, 2, 1, 1, 1)


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
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Amministratore", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Dialog", u"Username", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Nome", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Dialog", u"Cognome", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.btn_confirm_new_personale.setText(QCoreApplication.translate("Dialog", u"Aggiungi", None))
        self.btn_close_new_personale.setText(QCoreApplication.translate("Dialog", u"Annulla", None))
    # retranslateUi

