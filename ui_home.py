# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceHomeMYMYWS.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ui_home(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setMinimumSize(QSize(1000, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.centralwidget)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 50))
        self.top_bar.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"font: 10pt \"Dubai\";")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toggle = QFrame(self.top_bar)
        self.toggle.setObjectName(u"toggle")
        self.toggle.setMaximumSize(QSize(50, 50))
        self.toggle.setStyleSheet(u"background-color: rgb(123, 114, 255);")
        self.toggle.setFrameShape(QFrame.StyledPanel)
        self.toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.toggle)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: solid 0px;")

        self.verticalLayout_2.addWidget(self.btn_toggle)


        self.horizontalLayout.addWidget(self.toggle)

        self.top = QFrame(self.top_bar)
        self.top.setObjectName(u"top")
        self.top.setStyleSheet(u"background-color: rgb(35, 35, 35);\n"
"font: 10pt \"Dubai\";\n"
"color: white;")
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.blank_top = QFrame(self.top)
        self.blank_top.setObjectName(u"blank_top")
        self.blank_top.setMinimumSize(QSize(500, 0))
        self.blank_top.setFrameShape(QFrame.NoFrame)
        self.blank_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.blank_top)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_date_time = QLabel(self.blank_top)
        self.label_date_time.setObjectName(u"label_date_time")
        self.label_date_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_date_time)

        self.label_posti = QLabel(self.blank_top)
        self.label_posti.setObjectName(u"label_posti")
        self.label_posti.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_posti)

        self.btn_home_top = QPushButton(self.blank_top)
        self.btn_home_top.setObjectName(u"btn_home_top")
        self.btn_home_top.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home_top.setStyleSheet(u"QPushButton {font: 700 16pt \"Dubai\";\n"
"background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	text-decoration: underline;\n"
"	font: 700 14pt \"Dubai\";\n"
"}\n"
"")

        self.horizontalLayout_16.addWidget(self.btn_home_top)


        self.horizontalLayout_3.addWidget(self.blank_top)

        self.top_menu = QFrame(self.top)
        self.top_menu.setObjectName(u"top_menu")
        self.top_menu.setFrameShape(QFrame.NoFrame)
        self.top_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.top_menu)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_add_tavolo = QPushButton(self.top_menu)
        self.btn_add_tavolo.setObjectName(u"btn_add_tavolo")
        self.btn_add_tavolo.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(123, 114, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_add_tavolo)

        self.btn_add_ordine = QPushButton(self.top_menu)
        self.btn_add_ordine.setObjectName(u"btn_add_ordine")
        self.btn_add_ordine.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(123, 114, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_add_ordine)

        self.btn_logout = QPushButton(self.top_menu)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(123, 114, 255);\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_logout)


        self.horizontalLayout_3.addWidget(self.top_menu)


        self.horizontalLayout.addWidget(self.top)


        self.verticalLayout.addWidget(self.top_bar)

        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(50, 0))
        self.frame_left_menu.setMaximumSize(QSize(50, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menu = QFrame(self.frame_left_menu)
        self.frame_top_menu.setObjectName(u"frame_top_menu")
        sizePolicy.setHeightForWidth(self.frame_top_menu.sizePolicy().hasHeightForWidth())
        self.frame_top_menu.setSizePolicy(sizePolicy)
        self.frame_top_menu.setFrameShape(QFrame.NoFrame)
        self.frame_top_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_top_menu)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_personale = QPushButton(self.frame_top_menu)
        self.btn_personale.setObjectName(u"btn_personale")
        self.btn_personale.setMinimumSize(QSize(0, 40))
        self.btn_personale.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(123, 114, 255);\n"
"}")

        self.gridLayout.addWidget(self.btn_personale, 2, 0, 1, 1)

        self.btn_menu = QPushButton(self.frame_top_menu)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(0, 40))
        self.btn_menu.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(123, 114, 255);\n"
"	border: 0px solid;\n"
"}")

        self.gridLayout.addWidget(self.btn_menu, 1, 0, 1, 1)

        self.btn_statistiche = QPushButton(self.frame_top_menu)
        self.btn_statistiche.setObjectName(u"btn_statistiche")
        self.btn_statistiche.setMinimumSize(QSize(0, 40))
        self.btn_statistiche.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(123, 114, 255);\n"
"}")

        self.gridLayout.addWidget(self.btn_statistiche, 3, 0, 1, 1)

        self.btn_home = QPushButton(self.frame_top_menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 40))
        self.btn_home.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent;\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(123, 114, 255);\n"
"	border: 0px solid;\n"
"}")

        self.gridLayout.addWidget(self.btn_home, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_top_menu, 0, Qt.AlignTop)

        self.frame_settings = QFrame(self.frame_left_menu)
        self.frame_settings.setObjectName(u"frame_settings")
        sizePolicy.setHeightForWidth(self.frame_settings.sizePolicy().hasHeightForWidth())
        self.frame_settings.setSizePolicy(sizePolicy)
        self.frame_settings.setMinimumSize(QSize(0, 0))
        self.frame_settings.setMaximumSize(QSize(16777215, 100))
        self.frame_settings.setFrameShape(QFrame.NoFrame)
        self.frame_settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_settings)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.btn_settings = QPushButton(self.frame_settings)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setContextMenuPolicy(Qt.PreventContextMenu)
        self.btn_settings.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: transparent\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(123, 114, 255);\n"
"}")

        self.verticalLayout_10.addWidget(self.btn_settings)


        self.verticalLayout_3.addWidget(self.frame_settings)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_pages = QFrame(self.content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setMinimumSize(QSize(70, 0))
        self.frame_pages.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 500 10pt \"Dubai\";")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Pages_widget = QStackedWidget(self.frame_pages)
        self.Pages_widget.setObjectName(u"Pages_widget")
        self.TavoliPage = QWidget()
        self.TavoliPage.setObjectName(u"TavoliPage")
        self.horizontalLayout_10 = QHBoxLayout(self.TavoliPage)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_table_widget_tavoli = QFrame(self.TavoliPage)
        self.frame_table_widget_tavoli.setObjectName(u"frame_table_widget_tavoli")
        self.frame_table_widget_tavoli.setMaximumSize(QSize(500, 16777215))
        self.frame_table_widget_tavoli.setFrameShape(QFrame.StyledPanel)
        self.frame_table_widget_tavoli.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_table_widget_tavoli)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_tavoli = QTableWidget(self.frame_table_widget_tavoli)
        self.tableWidget_tavoli.setObjectName(u"tableWidget_tavoli")
        self.tableWidget_tavoli.setBaseSize(QSize(0, 0))
        self.tableWidget_tavoli.setStyleSheet(u"QScrollBar:vertical {\n"
"width: 7px;\n"
"		background-color: white;\n"
"		margin: 0px 0px 0px 0px;\n"
"		border-radius: 10px;\n"
"    }\n"
"QScrollBar::handle {\n"
"        background: rgb(125, 125, 125);\n"
"        border-radius: 2px;\n"
"    }\n"
"\n"
"QTableView::item {\n"
"    border:2px solid  rgb(255, 170, 0);\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	margin-left: 10px;\n"
"	height: 20px!important;\n"
"	margin-top: 10px;\n"
"}\n"
"\n"
"QTableView::item:focus {background-color: rgb(255, 170, 0);}\n"
"QTableView::item:hover {background-color: rgb(255, 170, 0);}")
        self.tableWidget_tavoli.setFrameShape(QFrame.NoFrame)
        self.tableWidget_tavoli.setLineWidth(0)
        self.tableWidget_tavoli.setMidLineWidth(0)
        self.tableWidget_tavoli.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_tavoli.setShowGrid(False)
        self.tableWidget_tavoli.setGridStyle(Qt.NoPen)
        self.tableWidget_tavoli.setRowCount(0)
        self.tableWidget_tavoli.setColumnCount(0)
        self.tableWidget_tavoli.horizontalHeader().setVisible(False)
        self.tableWidget_tavoli.horizontalHeader().setMinimumSectionSize(52)
        self.tableWidget_tavoli.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_tavoli.verticalHeader().setVisible(False)
        self.tableWidget_tavoli.verticalHeader().setDefaultSectionSize(100)
        self.tableWidget_tavoli.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_11.addWidget(self.tableWidget_tavoli)


        self.horizontalLayout_10.addWidget(self.frame_table_widget_tavoli)

        self.frame_tavolo_selected = QFrame(self.TavoliPage)
        self.frame_tavolo_selected.setObjectName(u"frame_tavolo_selected")
        self.frame_tavolo_selected.setMaximumSize(QSize(16777215, 16777215))
        self.frame_tavolo_selected.setFrameShape(QFrame.NoFrame)
        self.frame_tavolo_selected.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_tavolo_selected)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_buttons_tavolo = QFrame(self.frame_tavolo_selected)
        self.frame_buttons_tavolo.setObjectName(u"frame_buttons_tavolo")
        self.frame_buttons_tavolo.setMaximumSize(QSize(16777215, 50))
        self.frame_buttons_tavolo.setFrameShape(QFrame.NoFrame)
        self.frame_buttons_tavolo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_buttons_tavolo)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_delete_ordine_tavolo = QPushButton(self.frame_buttons_tavolo)
        self.btn_delete_ordine_tavolo.setObjectName(u"btn_delete_ordine_tavolo")
        self.btn_delete_ordine_tavolo.setMaximumSize(QSize(250, 16777215))
        self.btn_delete_ordine_tavolo.setStyleSheet(u"QPushButton{ border: none;\n"
"background-color: transparent;\n"
"font: 500 10.5pt \"Dubai\";\n"
"padding: 10px;\n"
"letter-spacing:0.2px ;\n"
"border: 2px solid rgb(255, 170, 0);\n"
"border-radius: 5px;\n"
"margin-right: 5px;}\n"
"QPushButton:focus:pressed{font: 500 11pt \"Dubai\";\n"
"	background-color: rgb(255, 170, 0);}\n"
"QPushButton:focus{ border: none;\n"
"background-color: transparent;\n"
"font: 500 10.5pt \"Dubai\";\n"
"padding: 10px; \n"
"border: 2px solid rgb(255, 170, 0);\n"
"border-radius: 5px;\n"
"margin-right: 5px;}\n"
"QPushButton:hover{ font: 500 11pt \"Dubai\";\n"
"	border: 2px solid rgb(255, 170, 0);}")

        self.horizontalLayout_5.addWidget(self.btn_delete_ordine_tavolo)

        self.btn_cliente_tavolo = QPushButton(self.frame_buttons_tavolo)
        self.btn_cliente_tavolo.setObjectName(u"btn_cliente_tavolo")
        self.btn_cliente_tavolo.setMaximumSize(QSize(250, 16777215))
        self.btn_cliente_tavolo.setStyleSheet(u"QPushButton{ border: none;\n"
"background-color: transparent;\n"
"font: 500 10.5pt \"Dubai\";\n"
"padding: 10px;\n"
"letter-spacing:0.2px ;\n"
"border: 2px solid rgb(255, 170, 0);\n"
"border-radius: 5px;\n"
"margin-left: 5px;}\n"
"QPushButton:focus:pressed{font: 500 11pt \"Dubai\";\n"
"	background-color: rgb(255, 170, 0);}\n"
"QPushButton:focus{ border: none;\n"
"background-color: transparent;\n"
"font: 500 10.5pt \"Dubai\";\n"
"padding: 10px; \n"
"border: 2px solid rgb(255, 170, 0);\n"
"border-radius: 5px;\n"
"margin-left: 5px;}\n"
"QPushButton:hover{ font: 500 11pt \"Dubai\";\n"
"	border: 2px solid rgb(255, 170, 0);}")

        self.horizontalLayout_5.addWidget(self.btn_cliente_tavolo)


        self.verticalLayout_6.addWidget(self.frame_buttons_tavolo)

        self.frame_tavolo_ordine = QFrame(self.frame_tavolo_selected)
        self.frame_tavolo_ordine.setObjectName(u"frame_tavolo_ordine")
        self.frame_tavolo_ordine.setFrameShape(QFrame.StyledPanel)
        self.frame_tavolo_ordine.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_tavolo_ordine)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.frame_tavolo_ordine)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"  QScrollBar:vertical {\n"
"        min-width: 8px;\n"
"        height: 7px;\n"
"		background-color: white;\n"
"		margin: 0px 0px 0px 0px;\n"
"		border-radius: 3px;\n"
"    }\n"
"QScrollBar::handle {\n"
"        background: rgb(125, 125, 125);\n"
"        border-radius: 3px;\n"
"    }")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 460, 284))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_ordine_tavolo = QLabel(self.scrollAreaWidgetContents)
        self.label_ordine_tavolo.setObjectName(u"label_ordine_tavolo")
        self.label_ordine_tavolo.setMinimumSize(QSize(0, 0))
        self.label_ordine_tavolo.setMaximumSize(QSize(16777215, 16777215))
        self.label_ordine_tavolo.setStyleSheet(u"font: 500 12pt \"Dubai\";\n"
"padding: 10px;")
        self.label_ordine_tavolo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_14.addWidget(self.label_ordine_tavolo)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_13.addWidget(self.scrollArea_2)

        self.label_datetime_ordine_tavolo = QLabel(self.frame_tavolo_ordine)
        self.label_datetime_ordine_tavolo.setObjectName(u"label_datetime_ordine_tavolo")
        self.label_datetime_ordine_tavolo.setStyleSheet(u"font: 10pt \"Dubai\";\n"
"padding: 8px;")

        self.verticalLayout_13.addWidget(self.label_datetime_ordine_tavolo)


        self.verticalLayout_6.addWidget(self.frame_tavolo_ordine)

        self.frame_btn_stampa_scontrino = QFrame(self.frame_tavolo_selected)
        self.frame_btn_stampa_scontrino.setObjectName(u"frame_btn_stampa_scontrino")
        self.frame_btn_stampa_scontrino.setMaximumSize(QSize(16777215, 70))
        self.frame_btn_stampa_scontrino.setFrameShape(QFrame.NoFrame)
        self.frame_btn_stampa_scontrino.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_btn_stampa_scontrino)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_stampa_scontrino = QPushButton(self.frame_btn_stampa_scontrino)
        self.btn_stampa_scontrino.setObjectName(u"btn_stampa_scontrino")
        self.btn_stampa_scontrino.setStyleSheet(u"QPushButton{ border: none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 170, 0, 255), stop:1 rgba(230, 179, 79, 255));\n"
"font: 500 15pt \"Dubai\";\n"
"padding: 9px;\n"
"letter-spacing:0.2px ;\n"
"/*border: 2px solid rgb(255, 170, 0);*/\n"
"border-radius: 5px;\n"
"margin-right: 5px;}\n"
"QPushButton:focus:pressed{font: 500 13.5pt \"Dubai\";\n"
"	background-color: rgb(255, 170, 0);}\n"
"QPushButton:focus{/*uguale allo stile normale*/}\n"
"QPushButton:hover{background-color: rgb(255, 170, 0);}")

        self.horizontalLayout_14.addWidget(self.btn_stampa_scontrino)


        self.verticalLayout_6.addWidget(self.frame_btn_stampa_scontrino)


        self.horizontalLayout_10.addWidget(self.frame_tavolo_selected)

        self.Pages_widget.addWidget(self.TavoliPage)
        self.MenuPage = QWidget()
        self.MenuPage.setObjectName(u"MenuPage")
        self.horizontalLayout_18 = QHBoxLayout(self.MenuPage)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_list_and_new_piatto = QFrame(self.MenuPage)
        self.frame_list_and_new_piatto.setObjectName(u"frame_list_and_new_piatto")
        self.frame_list_and_new_piatto.setMaximumSize(QSize(380, 16777215))
        self.frame_list_and_new_piatto.setFrameShape(QFrame.StyledPanel)
        self.frame_list_and_new_piatto.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_list_and_new_piatto)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_categorie_menu = QFrame(self.frame_list_and_new_piatto)
        self.frame_categorie_menu.setObjectName(u"frame_categorie_menu")
        self.frame_categorie_menu.setMinimumSize(QSize(0, 0))
        self.frame_categorie_menu.setMaximumSize(QSize(16777215, 60))
        self.frame_categorie_menu.setFrameShape(QFrame.NoFrame)
        self.frame_categorie_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_categorie_menu)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.table_categorie_menu = QTableWidget(self.frame_categorie_menu)
        if (self.table_categorie_menu.rowCount() < 1):
            self.table_categorie_menu.setRowCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_categorie_menu.setVerticalHeaderItem(0, __qtablewidgetitem)
        self.table_categorie_menu.setObjectName(u"table_categorie_menu")
        self.table_categorie_menu.setStyleSheet(u"QTableView::item {\n"
"    border:2px solid  rgb(255, 170, 0);\n"
"	border-radius: 10px;\n"
"	background-color: transparent;\n"
"	margin-left: 10px;\n"
"	height: 20px!important;\n"
"	color: white;\n"
"	margin-top: 10px;\n"
"}\n"
"\n"
"QTableView::item:focus {background-color: rgb(255, 170, 0);}\n"
"QTableView::item:hover {background-color: rgb(255, 170, 0);}")
        self.table_categorie_menu.setFrameShape(QFrame.NoFrame)
        self.table_categorie_menu.setGridStyle(Qt.NoPen)
        self.table_categorie_menu.horizontalHeader().setVisible(False)
        self.table_categorie_menu.verticalHeader().setVisible(False)
        self.table_categorie_menu.verticalHeader().setDefaultSectionSize(60)

        self.horizontalLayout_11.addWidget(self.table_categorie_menu)


        self.verticalLayout_18.addWidget(self.frame_categorie_menu)

        self.list_piatti = QListWidget(self.frame_list_and_new_piatto)
        self.list_piatti.setObjectName(u"list_piatti")
        self.list_piatti.setStyleSheet(u"\n"
" QListWidget::item {\n"
"	background-color: #ffaa00;\n"
"	color: white;\n"
"	border: 2px solid;\n"
"	border-radius: 15px;\n"
"}\n"
"QListWidget {\n"
"	font-size: 22px;\n"
"}\n"
"\n"
"  QScrollBar:vertical {\n"
"        min-width: 8px;\n"
"        height: 7px;\n"
"		background-color: white;\n"
"		margin: 0px 0px 0px 0px;\n"
"		border-radius: 3px;\n"
"    }\n"
"QScrollBar::handle {\n"
"        background: rgb(125, 125, 125);\n"
"        border-radius: 3px;\n"
"    }")
        self.list_piatti.setFrameShape(QFrame.NoFrame)
        self.list_piatti.setItemAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_18.addWidget(self.list_piatti)

        self.btn_new_piatto = QPushButton(self.frame_list_and_new_piatto)
        self.btn_new_piatto.setObjectName(u"btn_new_piatto")
        self.btn_new_piatto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new_piatto.setStyleSheet(u"font: 700 14pt \"Dubai\";\n"
"background-color: transparent;\n"
"text-decoration: underline;\n"
"")

        self.verticalLayout_18.addWidget(self.btn_new_piatto)


        self.horizontalLayout_18.addWidget(self.frame_list_and_new_piatto)

        self.frame_view_ingridients_delete = QFrame(self.MenuPage)
        self.frame_view_ingridients_delete.setObjectName(u"frame_view_ingridients_delete")
        self.frame_view_ingridients_delete.setFrameShape(QFrame.StyledPanel)
        self.frame_view_ingridients_delete.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_view_ingridients_delete)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_portata_on_click = QFrame(self.frame_view_ingridients_delete)
        self.frame_portata_on_click.setObjectName(u"frame_portata_on_click")
        self.frame_portata_on_click.setFrameShape(QFrame.NoFrame)
        self.frame_portata_on_click.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_portata_on_click)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_title_portata = QFrame(self.frame_portata_on_click)
        self.frame_title_portata.setObjectName(u"frame_title_portata")
        self.frame_title_portata.setFrameShape(QFrame.StyledPanel)
        self.frame_title_portata.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_title_portata)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_id = QLabel(self.frame_title_portata)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setMaximumSize(QSize(16777215, 16777215))
        self.label_id.setStyleSheet(u"font: 500 14pt \"Dubai\";")
        self.label_id.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_19.addWidget(self.label_id)

        self.label_categoria = QLabel(self.frame_title_portata)
        self.label_categoria.setObjectName(u"label_categoria")
        self.label_categoria.setStyleSheet(u"font: 500 13pt \"Dubai\";")

        self.verticalLayout_19.addWidget(self.label_categoria)

        self.label_ingredienti = QLabel(self.frame_title_portata)
        self.label_ingredienti.setObjectName(u"label_ingredienti")
        self.label_ingredienti.setStyleSheet(u"font: 500 13pt \"Dubai\";")
        self.label_ingredienti.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_19.addWidget(self.label_ingredienti)

        self.label_prezzo = QLabel(self.frame_title_portata)
        self.label_prezzo.setObjectName(u"label_prezzo")
        self.label_prezzo.setStyleSheet(u"font: 500 13pt \"Dubai\";")

        self.verticalLayout_19.addWidget(self.label_prezzo)


        self.horizontalLayout_20.addWidget(self.frame_title_portata)

        self.frame_show_portata = QFrame(self.frame_portata_on_click)
        self.frame_show_portata.setObjectName(u"frame_show_portata")
        self.frame_show_portata.setFrameShape(QFrame.NoFrame)
        self.frame_show_portata.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_show_portata)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_id_portata = QLabel(self.frame_show_portata)
        self.label_id_portata.setObjectName(u"label_id_portata")

        self.verticalLayout_20.addWidget(self.label_id_portata)

        self.label_categoria_portata = QLabel(self.frame_show_portata)
        self.label_categoria_portata.setObjectName(u"label_categoria_portata")

        self.verticalLayout_20.addWidget(self.label_categoria_portata)

        self.label_ingredienti_portata = QLabel(self.frame_show_portata)
        self.label_ingredienti_portata.setObjectName(u"label_ingredienti_portata")

        self.verticalLayout_20.addWidget(self.label_ingredienti_portata)

        self.label_prezzo_portata = QLabel(self.frame_show_portata)
        self.label_prezzo_portata.setObjectName(u"label_prezzo_portata")

        self.verticalLayout_20.addWidget(self.label_prezzo_portata)


        self.horizontalLayout_20.addWidget(self.frame_show_portata)


        self.verticalLayout_7.addWidget(self.frame_portata_on_click)

        self.frame_delete_portata = QFrame(self.frame_view_ingridients_delete)
        self.frame_delete_portata.setObjectName(u"frame_delete_portata")
        self.frame_delete_portata.setMaximumSize(QSize(16777215, 30))
        self.frame_delete_portata.setFrameShape(QFrame.NoFrame)
        self.frame_delete_portata.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_delete_portata)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.btn_delete_piatto = QPushButton(self.frame_delete_portata)
        self.btn_delete_piatto.setObjectName(u"btn_delete_piatto")
        self.btn_delete_piatto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_piatto.setStyleSheet(u"font: 700 14pt \"Dubai\";\n"
"background-color: transparent;\n"
"text-decoration: underline;\n"
"")
        self.btn_delete_piatto.setAutoRepeat(False)

        self.horizontalLayout_19.addWidget(self.btn_delete_piatto)


        self.verticalLayout_7.addWidget(self.frame_delete_portata)


        self.horizontalLayout_18.addWidget(self.frame_view_ingridients_delete)

        self.Pages_widget.addWidget(self.MenuPage)
        self.PersonalePage = QWidget()
        self.PersonalePage.setObjectName(u"PersonalePage")
        self.verticalLayout_8 = QVBoxLayout(self.PersonalePage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_ordini = QLabel(self.PersonalePage)
        self.label_ordini.setObjectName(u"label_ordini")
        font = QFont()
        font.setFamily(u"Dubai")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_ordini.setFont(font)
        self.label_ordini.setStyleSheet(u"color:white;")
        self.label_ordini.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_ordini)

        self.Pages_widget.addWidget(self.PersonalePage)
        self.StatistichePage = QWidget()
        self.StatistichePage.setObjectName(u"StatistichePage")
        self.verticalLayout_9 = QVBoxLayout(self.StatistichePage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_statistiche = QLabel(self.StatistichePage)
        self.label_statistiche.setObjectName(u"label_statistiche")
        self.label_statistiche.setFont(font)
        self.label_statistiche.setStyleSheet(u"color:white;")
        self.label_statistiche.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_statistiche)

        self.Pages_widget.addWidget(self.StatistichePage)
        self.OrdiniPage = QWidget()
        self.OrdiniPage.setObjectName(u"OrdiniPage")
        self.horizontalLayout_6 = QHBoxLayout(self.OrdiniPage)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_aggiungi_ordine = QFrame(self.OrdiniPage)
        self.frame_aggiungi_ordine.setObjectName(u"frame_aggiungi_ordine")
        self.frame_aggiungi_ordine.setFrameShape(QFrame.StyledPanel)
        self.frame_aggiungi_ordine.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_aggiungi_ordine)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_nuovo_ordine = QFrame(self.frame_aggiungi_ordine)
        self.frame_nuovo_ordine.setObjectName(u"frame_nuovo_ordine")
        self.frame_nuovo_ordine.setFrameShape(QFrame.StyledPanel)
        self.frame_nuovo_ordine.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_nuovo_ordine)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_seleziona_tavolo = QFrame(self.frame_nuovo_ordine)
        self.frame_seleziona_tavolo.setObjectName(u"frame_seleziona_tavolo")
        self.frame_seleziona_tavolo.setMinimumSize(QSize(0, 60))
        self.frame_seleziona_tavolo.setMaximumSize(QSize(16777215, 60))
        self.frame_seleziona_tavolo.setFrameShape(QFrame.StyledPanel)
        self.frame_seleziona_tavolo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_seleziona_tavolo)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_tavolo = QLabel(self.frame_seleziona_tavolo)
        self.label_tavolo.setObjectName(u"label_tavolo")
        self.label_tavolo.setStyleSheet(u"font: 500 14pt \"Dubai\";")

        self.horizontalLayout_7.addWidget(self.label_tavolo)

        self.comboBox_seleziona_tavolo = QComboBox(self.frame_seleziona_tavolo)
        self.comboBox_seleziona_tavolo.setObjectName(u"comboBox_seleziona_tavolo")
        self.comboBox_seleziona_tavolo.setStyleSheet(u"border: 2px solid rgb(255, 85, 0);\n"
"border-radius: 10px;\n"
"background-color:transparent;\n"
"box-shadow: none;")

        self.horizontalLayout_7.addWidget(self.comboBox_seleziona_tavolo)


        self.verticalLayout_12.addWidget(self.frame_seleziona_tavolo)

        self.frame_seleziona_categoria = QFrame(self.frame_nuovo_ordine)
        self.frame_seleziona_categoria.setObjectName(u"frame_seleziona_categoria")
        self.frame_seleziona_categoria.setMinimumSize(QSize(0, 60))
        self.frame_seleziona_categoria.setMaximumSize(QSize(16777215, 60))
        self.frame_seleziona_categoria.setFrameShape(QFrame.StyledPanel)
        self.frame_seleziona_categoria.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_seleziona_categoria)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.table_categorie = QTableWidget(self.frame_seleziona_categoria)
        if (self.table_categorie.rowCount() < 1):
            self.table_categorie.setRowCount(1)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_categorie.setVerticalHeaderItem(0, __qtablewidgetitem1)
        self.table_categorie.setObjectName(u"table_categorie")
        self.table_categorie.setStyleSheet(u"QTableView::item {\n"
"    border:2px solid  rgb(255, 170, 0);\n"
"	border-radius: 10px;\n"
"	background-color: transparent;\n"
"	margin-left: 10px;\n"
"	height: 20px!important;\n"
"	color: white;\n"
"	margin-top: 10px;\n"
"}\n"
"\n"
"QTableView::item:focus {background-color: rgb(255, 170, 0);}\n"
"QTableView::item:hover {background-color: rgb(255, 170, 0);}")
        self.table_categorie.setFrameShape(QFrame.NoFrame)
        self.table_categorie.setDefaultDropAction(Qt.IgnoreAction)
        self.table_categorie.setShowGrid(False)
        self.table_categorie.setGridStyle(Qt.NoPen)
        self.table_categorie.horizontalHeader().setVisible(False)
        self.table_categorie.horizontalHeader().setMinimumSectionSize(34)
        self.table_categorie.horizontalHeader().setDefaultSectionSize(100)
        self.table_categorie.verticalHeader().setVisible(False)
        self.table_categorie.verticalHeader().setDefaultSectionSize(50)
        self.table_categorie.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_8.addWidget(self.table_categorie)


        self.verticalLayout_12.addWidget(self.frame_seleziona_categoria)

        self.frame_seleziona_portata = QFrame(self.frame_nuovo_ordine)
        self.frame_seleziona_portata.setObjectName(u"frame_seleziona_portata")
        self.frame_seleziona_portata.setFrameShape(QFrame.StyledPanel)
        self.frame_seleziona_portata.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_seleziona_portata)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.frame_seleziona_portata)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setStyleSheet(u"QScrollBar:vertical {\n"
"width: 7px;\n"
"		background-color: white;\n"
"		margin: 0px 0px 0px 0px;\n"
"		border-radius: 10px;\n"
"    }\n"
"QScrollBar::handle {\n"
"        background: rgb(125, 125, 125);\n"
"        border-radius: 2px;\n"
"    }\n"
"\n"
"QTableView::item {\n"
"    border: 1px solid rgb(45, 45, 45);\n"
"	border-radius: 3px;\n"
"	background-color:qlineargradient(spread:pad, x1:0.579, y1:0.767636, x2:1, y2:1, stop:0 rgba(255, 170, 0, 248), stop:1 rgba(45, 45, 45, 215));\n"
"	max-width: 7px;\n"
"color: white;\n"
"}")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(Qt.NoPen)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(60)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_9.addWidget(self.tableWidget)


        self.verticalLayout_12.addWidget(self.frame_seleziona_portata)


        self.horizontalLayout_13.addWidget(self.frame_nuovo_ordine)

        self.frame_ordine_view = QFrame(self.frame_aggiungi_ordine)
        self.frame_ordine_view.setObjectName(u"frame_ordine_view")
        self.frame_ordine_view.setMaximumSize(QSize(300, 16777215))
        self.frame_ordine_view.setFrameShape(QFrame.StyledPanel)
        self.frame_ordine_view.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_ordine_view)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_view_ordine = QFrame(self.frame_ordine_view)
        self.frame_view_ordine.setObjectName(u"frame_view_ordine")
        self.frame_view_ordine.setMinimumSize(QSize(300, 0))
        self.frame_view_ordine.setMaximumSize(QSize(16777215, 16777215))
        self.frame_view_ordine.setFrameShape(QFrame.NoFrame)
        self.frame_view_ordine.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_view_ordine)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_view_ordine)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet(u"QScrollBar:vertical {\n"
"		width: 7px;\n"
"		background-color: white;\n"
"		margin: 0px 0px 0px 0px;\n"
"		border-radius: 10px;\n"
"    }\n"
"QScrollBar::handle {\n"
"        background: rgb(125, 125, 125);\n"
"        border-radius: 2px;\n"
"    }\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 300, 336))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_21.addWidget(self.scrollArea)


        self.verticalLayout_15.addWidget(self.frame_view_ordine)

        self.frame_8 = QFrame(self.frame_ordine_view)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 110))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_8)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.btn_elimina_ordine = QPushButton(self.frame_8)
        self.btn_elimina_ordine.setObjectName(u"btn_elimina_ordine")
        self.btn_elimina_ordine.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_elimina_ordine.setStyleSheet(u"border-radius: 7px;\n"
"font: 500 11pt \"Dubai\";\n"
"background-color: rgb(255, 170, 0);\n"
"padding: 7px\n"
"")

        self.verticalLayout_16.addWidget(self.btn_elimina_ordine)

        self.btn_invio_ordine = QPushButton(self.frame_8)
        self.btn_invio_ordine.setObjectName(u"btn_invio_ordine")
        self.btn_invio_ordine.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_invio_ordine.setStyleSheet(u"border-radius: 7px;\n"
"font: 500 11pt \"Dubai\";\n"
"background-color: rgb(255, 170, 0);\n"
"padding: 7px;\n"
"margin-top: 10px;\n"
"")

        self.verticalLayout_16.addWidget(self.btn_invio_ordine)


        self.verticalLayout_15.addWidget(self.frame_8)


        self.horizontalLayout_13.addWidget(self.frame_ordine_view)


        self.horizontalLayout_6.addWidget(self.frame_aggiungi_ordine)

        self.Pages_widget.addWidget(self.OrdiniPage)
        self.SettingsPage = QWidget()
        self.SettingsPage.setObjectName(u"SettingsPage")
        self.verticalLayout_17 = QVBoxLayout(self.SettingsPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label = QLabel(self.SettingsPage)
        self.label.setObjectName(u"label")

        self.verticalLayout_17.addWidget(self.label)

        self.Pages_widget.addWidget(self.SettingsPage)

        self.verticalLayout_5.addWidget(self.Pages_widget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.verticalLayout.addWidget(self.content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages_widget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"TOGGLE", None))
        self.label_date_time.setText(QCoreApplication.translate("MainWindow", u"Date and Time", None))
        self.label_posti.setText(QCoreApplication.translate("MainWindow", u"25/50", None))
        self.btn_home_top.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_add_tavolo.setText(QCoreApplication.translate("MainWindow", u"Aggiungi Tavolo", None))
        self.btn_add_ordine.setText(QCoreApplication.translate("MainWindow", u"Aggiungi Ordine", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.btn_personale.setText(QCoreApplication.translate("MainWindow", u"Personale", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btn_statistiche.setText(QCoreApplication.translate("MainWindow", u"Statistiche", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Tavoli", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_delete_ordine_tavolo.setText(QCoreApplication.translate("MainWindow", u"Cancella Ordini", None))
        self.btn_cliente_tavolo.setText(QCoreApplication.translate("MainWindow", u"Visualizza Cliente del Tavolo", None))
        self.label_ordine_tavolo.setText("")
        self.label_datetime_ordine_tavolo.setText(QCoreApplication.translate("MainWindow", u"Data e Ora dell'ordine:", None))
        self.btn_stampa_scontrino.setText(QCoreApplication.translate("MainWindow", u"Totale: 0\u20ac", None))
        ___qtablewidgetitem = self.table_categorie_menu.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.btn_new_piatto.setText(QCoreApplication.translate("MainWindow", u"Aggiungi nuovo piatto", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"ID Portata", None))
        self.label_categoria.setText(QCoreApplication.translate("MainWindow", u"Categoria Portata", None))
        self.label_ingredienti.setText(QCoreApplication.translate("MainWindow", u"Ingredienti Portata", None))
        self.label_prezzo.setText(QCoreApplication.translate("MainWindow", u"Prezzo", None))
        self.label_id_portata.setText("")
        self.label_categoria_portata.setText("")
        self.label_ingredienti_portata.setText("")
        self.label_prezzo_portata.setText("")
        self.btn_delete_piatto.setText(QCoreApplication.translate("MainWindow", u"Elimina Piatto", None))
        self.label_ordini.setText(QCoreApplication.translate("MainWindow", u"ORDINI", None))
        self.label_statistiche.setText(QCoreApplication.translate("MainWindow", u"STATISTICHE", None))
        self.label_tavolo.setText(QCoreApplication.translate("MainWindow", u"Seleziona Tavolo", None))
        ___qtablewidgetitem1 = self.table_categorie.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.btn_elimina_ordine.setText(QCoreApplication.translate("MainWindow", u"Elimina ultima aggiunta", None))
        self.btn_invio_ordine.setText(QCoreApplication.translate("MainWindow", u"Invia Ordine", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
    # retranslateUi
