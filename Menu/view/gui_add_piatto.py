# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_add_piattoVAChJt.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class gui_add_piatto(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 424)
        Dialog.setStyleSheet(u"background-color:#fff;")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: white;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 19pt \"Poppins\";\n"
"color: rgb(255, 85, 0);\n"
"letter-spacing: 0.5px;")

        self.verticalLayout_2.addWidget(self.label)

        self.label_message = QLabel(self.frame)
        self.label_message.setObjectName(u"label_message")
        self.label_message.setMaximumSize(QSize(16777215, 20))
        self.label_message.setStyleSheet(u"font: 10pt \"Poppins\";\n"
"color: rgb(120, 120, 120);")

        self.verticalLayout_2.addWidget(self.label_message)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_nome_piatto = QLabel(self.frame_3)
        self.label_nome_piatto.setObjectName(u"label_nome_piatto")
        self.label_nome_piatto.setStyleSheet(u"font: 500 11pt \"Poppins\";")
        self.label_nome_piatto.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_nome_piatto, 0, Qt.AlignLeft)

        self.lineEdit_nome_piatto = QLineEdit(self.frame_3)
        self.lineEdit_nome_piatto.setObjectName(u"lineEdit_nome_piatto")
        self.lineEdit_nome_piatto.setMinimumSize(QSize(50, 0))
        self.lineEdit_nome_piatto.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_nome_piatto.setStyleSheet(u"color: #000;\n"
"font: 400 12pt \"Poppins\";\n"
"border: solid;\n"
"border-bottom: 2px solid black;")

        self.horizontalLayout_4.addWidget(self.lineEdit_nome_piatto)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_categoria = QLabel(self.frame_6)
        self.label_categoria.setObjectName(u"label_categoria")
        self.label_categoria.setStyleSheet(u"font: 500 11pt \"Poppins\";")
        self.label_categoria.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_categoria, 0, Qt.AlignLeft)

        self.lineEdit_categoria = QLineEdit(self.frame_6)
        self.lineEdit_categoria.setObjectName(u"lineEdit_categoria")
        self.lineEdit_categoria.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_categoria.setStyleSheet(u"color: #000;\n"
"font: 400 12pt \"Poppins\";\n"
"border: solid;\n"
"border-bottom: 2px solid black;")

        self.horizontalLayout_3.addWidget(self.lineEdit_categoria)


        self.verticalLayout_2.addWidget(self.frame_6)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_prezzo = QLabel(self.frame_4)
        self.label_prezzo.setObjectName(u"label_prezzo")
        self.label_prezzo.setStyleSheet(u"font: 500 11pt \"Poppins\";")
        self.label_prezzo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_prezzo, 0, Qt.AlignLeft)

        self.lineEdit_prezzo = QLineEdit(self.frame_4)
        self.lineEdit_prezzo.setObjectName(u"lineEdit_prezzo")
        self.lineEdit_prezzo.setMaximumSize(QSize(150, 16777215))
        self.lineEdit_prezzo.setStyleSheet(u"color: #000;\n"
"font: 400 12pt \"Poppins\";\n"
"border: solid;\n"
"border-bottom: 2px solid black;")

        self.horizontalLayout_2.addWidget(self.lineEdit_prezzo)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 150))
        self.frame_5.setMaximumSize(QSize(16777215, 150))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_ingredienti = QLabel(self.frame_5)
        self.label_ingredienti.setObjectName(u"label_ingredienti")
        self.label_ingredienti.setStyleSheet(u"font: 10pt \"Poppins\";\n"
"color: rgb(120, 120, 120);")

        self.verticalLayout_3.addWidget(self.label_ingredienti)

        self.text_ingredienti = QPlainTextEdit(self.frame_5)
        self.text_ingredienti.setObjectName(u"text_ingredienti")
        self.text_ingredienti.setStyleSheet(u"border: 2px solid black;\n"
"border-radius: 5px;\n"
"background-color:transparent;")

        self.verticalLayout_3.addWidget(self.text_ingredienti)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 70))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_add_to_menu = QPushButton(self.frame_2)
        self.btn_add_to_menu.setObjectName(u"btn_add_to_menu")
        self.btn_add_to_menu.setStyleSheet(u"QPushButton{ border: 2px solid rgb(255, 85, 0);;\n"
"font: 600 12pt \"Poppins\";\n"
"padding: 6px;\n"
"letter-spacing:0.2px ;\n"
"border-radius: 5px;\n"
"color:rgb(255, 85, 0);;\n"
"margin-right: 5px;}\n"
"QPushButton:focus:pressed{background-color: rgb(255, 85, 0);; color: #fff;}\n"
"QPushButton:hover{border: none; background-color: rgb(255, 85, 0);; color: #fff;}\n"
"/*rgb(99, 159, 171)*/")

        self.horizontalLayout.addWidget(self.btn_add_to_menu)


        self.verticalLayout.addWidget(self.frame_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nuova Portata", None))
        self.label_message.setText(QCoreApplication.translate("Dialog", u"Crea una nuova portata", None))
        self.label_nome_piatto.setText(QCoreApplication.translate("Dialog", u"Nome del piatto", None))
        self.label_categoria.setText(QCoreApplication.translate("Dialog", u"Categoria", None))
        self.label_prezzo.setText(QCoreApplication.translate("Dialog", u"Prezzo", None))
        self.label_ingredienti.setText(QCoreApplication.translate("Dialog", u"Scrivi gli ingredienti separati da uno spazio", None))
        self.btn_add_to_menu.setText(QCoreApplication.translate("Dialog", u"Aggiungi", None))
    # retranslateUi

