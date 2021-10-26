# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_add_tavoloJAyQdt.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class gui_add_tavolo(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(359, 220)
        Dialog.setMaximumSize(QSize(16777215, 220))
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_insert = QFrame(Dialog)
        self.frame_insert.setObjectName(u"frame_insert")
        self.frame_insert.setFrameShape(QFrame.StyledPanel)
        self.frame_insert.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_insert)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_insert)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 500 11pt \"Poppins\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.lineEdit_posti_tavolo = QLineEdit(self.frame_insert)
        self.lineEdit_posti_tavolo.setObjectName(u"lineEdit_posti_tavolo")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_posti_tavolo.sizePolicy().hasHeightForWidth())
        self.lineEdit_posti_tavolo.setSizePolicy(sizePolicy)
        self.lineEdit_posti_tavolo.setStyleSheet(u"QLineEdit{border-bottom: 2px solid #ff8c00;\n"
"border-radius: 0px;\n"
"font: 11pt \"Poppins\";\n"
"color: rgb(31, 31, 31);}")
        self.lineEdit_posti_tavolo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit_posti_tavolo, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_insert)

        self.frame_buttons = QFrame(Dialog)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setMaximumSize(QSize(16777215, 100))
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_buttons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_ok_add_tavolo = QPushButton(self.frame_buttons)
        self.btn_ok_add_tavolo.setObjectName(u"btn_ok_add_tavolo")
        self.btn_ok_add_tavolo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ok_add_tavolo.setStyleSheet(u"QPushButton {background-color: #ff8c00;\n"
"color: white;\n"
"padding: 10px;\n"
"border-radius: 10px;\n"
"font: 500 11.5pt \"Poppins\";}\n"
"\n"
"QPushButton:hover {\n"
"font: 500 11pt \"Poppins\"; \n"
"padding: 10px;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.btn_ok_add_tavolo)

        self.btn_close_dialog = QPushButton(self.frame_buttons)
        self.btn_close_dialog.setObjectName(u"btn_close_dialog")
        self.btn_close_dialog.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close_dialog.setStyleSheet(u"background-color: #fff;\n"
"border: 2px solid #000;\n"
"border-radius: 10px;\n"
"color: black;\n"
"padding: 10px;\n"
"font: 500 11.5pt \"Poppins\";")

        self.horizontalLayout_2.addWidget(self.btn_close_dialog)


        self.verticalLayout_2.addWidget(self.frame_buttons)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Scrivi i posti disponibili sul nuovo tavolo", None))
        self.lineEdit_posti_tavolo.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.btn_ok_add_tavolo.setText(QCoreApplication.translate("Dialog", u"Aggiungi", None))
        self.btn_close_dialog.setText(QCoreApplication.translate("Dialog", u"Annulla", None))
    # retranslateUi

