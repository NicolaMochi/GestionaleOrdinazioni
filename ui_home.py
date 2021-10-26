# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceHomehQEaod.ui'
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
        MainWindow.setEnabled(True)
        MainWindow.resize(1198, 613)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"background-color: #F8F8F8;\n"
"color: black;\n"
"font: 9pt \"Poppins\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.centralwidget)
        self.content.setObjectName(u"content")
        self.content.setMaximumSize(QSize(16777215, 16777215))
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_pages = QFrame(self.content)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setMinimumSize(QSize(0, 0))
        self.frame_pages.setStyleSheet(u"color: black;\n"
"font: 500 10pt \"Dubai\";")
        self.frame_pages.setFrameShape(QFrame.NoFrame)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.top_bar = QFrame(self.frame_pages)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMaximumSize(QSize(16777215, 50))
        self.top_bar.setStyleSheet(u"/*background-color: rgb(35, 35, 35);*/\n"
"background-color: rgb(250, 250, 250);\n"
"font: 10pt \"Poppins\" black;")
        self.top_bar.setFrameShape(QFrame.NoFrame)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.top_bar)
        self.top.setObjectName(u"top")
        self.top.setStyleSheet(u"")
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
        self.btn_home_top.setStyleSheet(u"QPushButton {font: 700 16pt \"Poppins\";\n"
"background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	text-decoration: underline;\n"
"	font: 700 14pt \"Poppins\";\n"
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
        self.btn_add_tavolo.setStyleSheet(u"QPushButton{ border: none;\n"
"background-color: #ff8c00;\n"
"font: 500 9pt \"Poppins\";\n"
"color: white;\n"
"padding: 5px;\n"
"letter-spacing:0.2px ;\n"
"/*border: 2px solid rgb(255, 170, 0);*/\n"
"border-radius: 5px;\n"
"margin-right: 5px;}")

        self.horizontalLayout_4.addWidget(self.btn_add_tavolo)

        self.btn_add_ordine = QPushButton(self.top_menu)
        self.btn_add_ordine.setObjectName(u"btn_add_ordine")
        self.btn_add_ordine.setStyleSheet(u"QPushButton{ border: none;\n"
"background-color: #ff8c00;\n"
"font: 500 9pt \"Poppins\";\n"
"color: white;\n"
"padding: 5px;\n"
"letter-spacing:0.2px ;\n"
"/*border: 2px solid rgb(255, 170, 0);*/\n"
"border-radius: 5px;\n"
"margin-right: 5px;}")

        self.horizontalLayout_4.addWidget(self.btn_add_ordine)

        self.btn_logout = QPushButton(self.top_menu)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setStyleSheet(u"QPushButton{ border: none;\n"
"background-color: #ff8c00;\n"
"font: 500 9pt \"Poppins\";\n"
"color: white;\n"
"padding: 5px;\n"
"letter-spacing:0.2px ;\n"
"/*border: 2px solid rgb(255, 170, 0);*/\n"
"border-radius: 5px;\n"
"margin-right: 5px;}")

        self.horizontalLayout_4.addWidget(self.btn_logout)


        self.horizontalLayout_3.addWidget(self.top_menu)


        self.horizontalLayout.addWidget(self.top)


        self.verticalLayout_5.addWidget(self.top_bar)

        self.Pages_widget = QStackedWidget(self.frame_pages)
        self.Pages_widget.setObjectName(u"Pages_widget")
        self.TavoliPage = QWidget()
        self.TavoliPage.setObjectName(u"TavoliPage")
        self.horizontalLayout_10 = QHBoxLayout(self.TavoliPage)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 10, 20, 10)
        self.frame_table_widget_tavoli = QFrame(self.TavoliPage)
        self.frame_table_widget_tavoli.setObjectName(u"frame_table_widget_tavoli")
        self.frame_table_widget_tavoli.setMaximumSize(QSize(800, 16777215))
        self.frame_table_widget_tavoli.setFrameShape(QFrame.StyledPanel)
        self.frame_table_widget_tavoli.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_table_widget_tavoli)
        self.verticalLayout_11.setSpacing(100)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 30, 0)
        self.tableWidget_tavoli = QTableWidget(self.frame_table_widget_tavoli)
        if (self.tableWidget_tavoli.columnCount() < 4):
            self.tableWidget_tavoli.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_tavoli.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_tavoli.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_tavoli.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_tavoli.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_tavoli.setObjectName(u"tableWidget_tavoli")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget_tavoli.sizePolicy().hasHeightForWidth())
        self.tableWidget_tavoli.setSizePolicy(sizePolicy1)
        self.tableWidget_tavoli.setBaseSize(QSize(0, 0))
        self.tableWidget_tavoli.setStyleSheet(u"QTableView {\n"
"	margin-left: 20px;\n"
"}\n"
"QScrollBar:vertical {\n"
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
"    /*border:2px solid  rgb(255, 170, 0);*/\n"
"	border-radius: 10px;\n"
"	color: black;\n"
"	/*margin-left: 10px;*/\n"
"	height: 20px!important;\n"
"	/*margin-top: 10px;*/\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableView::item:focus {background-color: rgb(255, 170, 0); color: white;}\n"
"QTableView::item:hover {background-color: rgb(255, 170, 0); color: white;}")
        self.tableWidget_tavoli.setFrameShape(QFrame.NoFrame)
        self.tableWidget_tavoli.setLineWidth(0)
        self.tableWidget_tavoli.setMidLineWidth(0)
        self.tableWidget_tavoli.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_tavoli.setShowGrid(True)
        self.tableWidget_tavoli.setGridStyle(Qt.NoPen)
        self.tableWidget_tavoli.setRowCount(0)
        self.tableWidget_tavoli.setColumnCount(4)
        self.tableWidget_tavoli.horizontalHeader().setVisible(False)
        self.tableWidget_tavoli.horizontalHeader().setMinimumSectionSize(52)
        self.tableWidget_tavoli.horizontalHeader().setDefaultSectionSize(160)
        self.tableWidget_tavoli.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_tavoli.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_tavoli.verticalHeader().setVisible(False)
        self.tableWidget_tavoli.verticalHeader().setDefaultSectionSize(110)
        self.tableWidget_tavoli.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_11.addWidget(self.tableWidget_tavoli)


        self.horizontalLayout_10.addWidget(self.frame_table_widget_tavoli)

        self.frame_tavolo_selected = QFrame(self.TavoliPage)
        self.frame_tavolo_selected.setObjectName(u"frame_tavolo_selected")
        self.frame_tavolo_selected.setMinimumSize(QSize(0, 0))
        self.frame_tavolo_selected.setMaximumSize(QSize(420, 16777215))
        self.frame_tavolo_selected.setStyleSheet(u"background-color: #ffffff;\n"
"border-radius: 20px;")
        self.frame_tavolo_selected.setFrameShape(QFrame.NoFrame)
        self.frame_tavolo_selected.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_tavolo_selected)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 20, 20, 20)
        self.frame_buttons_tavolo = QFrame(self.frame_tavolo_selected)
        self.frame_buttons_tavolo.setObjectName(u"frame_buttons_tavolo")
        self.frame_buttons_tavolo.setMaximumSize(QSize(16777215, 50))
        self.frame_buttons_tavolo.setFrameShape(QFrame.NoFrame)
        self.frame_buttons_tavolo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_buttons_tavolo)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_cliente_tavolo = QPushButton(self.frame_buttons_tavolo)
        self.btn_cliente_tavolo.setObjectName(u"btn_cliente_tavolo")
        self.btn_cliente_tavolo.setMaximumSize(QSize(250, 16777215))
        self.btn_cliente_tavolo.setStyleSheet(u"QPushButton{ border: none;\n"
"background-color: transparent;\n"
"font: 500 10pt \"Poppins\";\n"
"color: rgb(43, 43, 43);\n"
"padding-left: 10px;\n"
"letter-spacing:0.2px ;\n"
"border-radius: 5px;\n"
"margin-right: 5px;}\n"
"QPushButton:focus:pressed{font: 500 10pt \"Poppins\";\n"
"	background-color: rgb(255, 170, 0);}\n"
"QPushButton:focus{ border: none;\n"
"background-color: transparent;\n"
"font: 500 10pt \"Poppins\";\n"
"padding: 10px; \n"
"border: 2px solid rgb(255, 170, 0);\n"
"border-radius: 5px;\n"
"margin-right: 5px;}\n"
"QPushButton:hover{ font: 500 10pt \"Poppins\";\n"
"	border: 2px solid rgb(255, 170, 0);}")

        self.horizontalLayout_5.addWidget(self.btn_cliente_tavolo)

        self.btn_delete_ordine_tavolo = QPushButton(self.frame_buttons_tavolo)
        self.btn_delete_ordine_tavolo.setObjectName(u"btn_delete_ordine_tavolo")
        self.btn_delete_ordine_tavolo.setMaximumSize(QSize(250, 16777215))
        self.btn_delete_ordine_tavolo.setStyleSheet(u"QPushButton{ border: none;\n"
"background-color: transparent;\n"
"font: 500 10pt \"Poppins\";\n"
"padding: 10px;\n"
"letter-spacing:0.2px ;\n"
"border: 2px solid rgb(255, 170, 0);\n"
"border-radius: 5px;\n"
"margin-right: 5px;}\n"
"QPushButton:focus:pressed{font: 500 10pt \"Poppins\";\n"
"	background-color: rgb(255, 170, 0);}\n"
"QPushButton:focus{ border: none;\n"
"background-color: transparent;\n"
"font: 500 10.5pt \"Poppins\";\n"
"padding: 10px; \n"
"border: 2px solid rgb(255, 170, 0);\n"
"border-radius: 5px;\n"
"margin-right: 5px;}\n"
"QPushButton:hover{ font: 500 11pt \"Poppins\";\n"
"	border: 2px solid rgb(255, 170, 0);}")

        self.horizontalLayout_5.addWidget(self.btn_delete_ordine_tavolo)


        self.verticalLayout_6.addWidget(self.frame_buttons_tavolo)

        self.frame_tavolo_ordine = QFrame(self.frame_tavolo_selected)
        self.frame_tavolo_ordine.setObjectName(u"frame_tavolo_ordine")
        self.frame_tavolo_ordine.setFrameShape(QFrame.NoFrame)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 414))
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

        self.label_datetime_ordine_tavolo = QLabel(self.scrollAreaWidgetContents)
        self.label_datetime_ordine_tavolo.setObjectName(u"label_datetime_ordine_tavolo")
        self.label_datetime_ordine_tavolo.setMaximumSize(QSize(16777215, 30))
        self.label_datetime_ordine_tavolo.setStyleSheet(u"font: 10pt \"Poppins\";\n"
"margin-top: 10px;\n"
"margin-bottom: 10px;\n"
"color: rgb(120, 120, 120)")

        self.verticalLayout_14.addWidget(self.label_datetime_ordine_tavolo)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_13.addWidget(self.scrollArea_2)


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
"font: 500 15pt \"Poppins\";\n"
"color: white;\n"
"padding: 9px;\n"
"letter-spacing:0.2px ;\n"
"/*border: 2px solid rgb(255, 170, 0);*/\n"
"border-radius: 5px;\n"
"margin-right: 5px;}\n"
"QPushButton:focus:pressed{font: 500 13.5pt \"Poppins\";\n"
"	background-color: rgb(255, 170, 0);}\n"
"QPushButton:focus{/*uguale allo stile normale*/}\n"
"QPushButton:hover{background-color: rgb(255, 170, 0);}")

        self.horizontalLayout_14.addWidget(self.btn_stampa_scontrino)


        self.verticalLayout_6.addWidget(self.frame_btn_stampa_scontrino)


        self.horizontalLayout_10.addWidget(self.frame_tavolo_selected)

        self.Pages_widget.addWidget(self.TavoliPage)
        self.MenuPage = QWidget()
        self.MenuPage.setObjectName(u"MenuPage")
        self.gridLayout_4 = QGridLayout(self.MenuPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(20, 10, 20, 0)
        self.frame_list_and_new_piatto = QFrame(self.MenuPage)
        self.frame_list_and_new_piatto.setObjectName(u"frame_list_and_new_piatto")
        self.frame_list_and_new_piatto.setMaximumSize(QSize(16777215, 16777215))
        self.frame_list_and_new_piatto.setFrameShape(QFrame.NoFrame)
        self.frame_list_and_new_piatto.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_list_and_new_piatto)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 10)
        self.frame_list_menu = QFrame(self.frame_list_and_new_piatto)
        self.frame_list_menu.setObjectName(u"frame_list_menu")
        self.frame_list_menu.setStyleSheet(u"background-color: #ffffff;\n"
"border-radius: 20px;")
        self.frame_list_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_list_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_list_menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 0, 20, 10)
        self.label_menu_info = QLabel(self.frame_list_menu)
        self.label_menu_info.setObjectName(u"label_menu_info")
        self.label_menu_info.setStyleSheet(u"font: 10pt \"Poppins\";\n"
"margin-top: 10px;\n"
"color: rgb(120, 120, 120)")

        self.verticalLayout.addWidget(self.label_menu_info)

        self.list_piatti = QListWidget(self.frame_list_menu)
        QListWidgetItem(self.list_piatti)
        QListWidgetItem(self.list_piatti)
        QListWidgetItem(self.list_piatti)
        self.list_piatti.setObjectName(u"list_piatti")
        self.list_piatti.setMaximumSize(QSize(16777215, 16777215))
        self.list_piatti.setStyleSheet(u"\n"
" QListWidget::item {\n"
"	color: black;\n"
"	border-bottom: 1px solid rgb(120, 120, 120);\n"
"	font: 400 11pt \"Poppins\";\n"
"	padding-bottom: 0px;\n"
"	margin-top: 10px;\n"
"	max-width: 100px;\n"
"}\n"
"QListWidget {\n"
"	font-size: 22px;\n"
"	margin-top: 10px;\n"
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

        self.verticalLayout.addWidget(self.list_piatti)

        self.btn_new_piatto = QPushButton(self.frame_list_menu)
        self.btn_new_piatto.setObjectName(u"btn_new_piatto")
        sizePolicy1.setHeightForWidth(self.btn_new_piatto.sizePolicy().hasHeightForWidth())
        self.btn_new_piatto.setSizePolicy(sizePolicy1)
        self.btn_new_piatto.setMinimumSize(QSize(0, 40))
        self.btn_new_piatto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new_piatto.setStyleSheet(u"QPushButton{ border: none;\n"
"background-color: #ff8c00;\n"
"font: 500 15pt \"Poppins\";\n"
"letter-spacing:0.2px;\n"
"/*border: 2px solid rgb(255, 170, 0);*/\n"
"border-radius: 15px;\n"
"color: #fff;\n"
"}\n"
"QPushButton:focus:pressed{font: 500 13.5pt \"Poppins\";\n"
"	background-color: #ff8c00;}\n"
"QPushButton:hover{background-color: #ff8c00;}")

        self.verticalLayout.addWidget(self.btn_new_piatto)


        self.horizontalLayout_18.addWidget(self.frame_list_menu)

        self.frame_view_ingridients_delete = QFrame(self.frame_list_and_new_piatto)
        self.frame_view_ingridients_delete.setObjectName(u"frame_view_ingridients_delete")
        self.frame_view_ingridients_delete.setMinimumSize(QSize(400, 0))
        self.frame_view_ingridients_delete.setStyleSheet(u"background-color: white;\n"
"border-radius: 20px;")
        self.frame_view_ingridients_delete.setFrameShape(QFrame.NoFrame)
        self.frame_view_ingridients_delete.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_view_ingridients_delete)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_portata_on_click = QFrame(self.frame_view_ingridients_delete)
        self.frame_portata_on_click.setObjectName(u"frame_portata_on_click")
        self.frame_portata_on_click.setFrameShape(QFrame.NoFrame)
        self.frame_portata_on_click.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_portata_on_click)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 10, 0, 0)
        self.frame_show_portata = QFrame(self.frame_portata_on_click)
        self.frame_show_portata.setObjectName(u"frame_show_portata")
        self.frame_show_portata.setMaximumSize(QSize(16777215, 16777215))
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


        self.gridLayout.addWidget(self.frame_show_portata, 1, 1, 1, 1)

        self.frame_title_portata = QFrame(self.frame_portata_on_click)
        self.frame_title_portata.setObjectName(u"frame_title_portata")
        self.frame_title_portata.setFrameShape(QFrame.StyledPanel)
        self.frame_title_portata.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_title_portata)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(10, 0, 0, 0)
        self.label_id = QLabel(self.frame_title_portata)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setMaximumSize(QSize(16777215, 16777215))
        self.label_id.setStyleSheet(u"font: 400 10pt \"Poppins\";")
        self.label_id.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_19.addWidget(self.label_id)

        self.label_categoria = QLabel(self.frame_title_portata)
        self.label_categoria.setObjectName(u"label_categoria")
        self.label_categoria.setMinimumSize(QSize(0, 0))
        self.label_categoria.setLayoutDirection(Qt.LeftToRight)
        self.label_categoria.setStyleSheet(u"font: 400 10pt \"Poppins\";")

        self.verticalLayout_19.addWidget(self.label_categoria)

        self.label_ingredienti = QLabel(self.frame_title_portata)
        self.label_ingredienti.setObjectName(u"label_ingredienti")
        self.label_ingredienti.setStyleSheet(u"font: 400 10pt \"Poppins\";")
        self.label_ingredienti.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_19.addWidget(self.label_ingredienti)

        self.label_prezzo = QLabel(self.frame_title_portata)
        self.label_prezzo.setObjectName(u"label_prezzo")
        self.label_prezzo.setStyleSheet(u"font: 400 10pt \"Poppins\";")

        self.verticalLayout_19.addWidget(self.label_prezzo)


        self.gridLayout.addWidget(self.frame_title_portata, 1, 0, 1, 1)

        self.frame_edit_portata = QFrame(self.frame_portata_on_click)
        self.frame_edit_portata.setObjectName(u"frame_edit_portata")
        self.frame_edit_portata.setMaximumSize(QSize(16777215, 25))
        self.frame_edit_portata.setStyleSheet(u"")
        self.frame_edit_portata.setFrameShape(QFrame.StyledPanel)
        self.frame_edit_portata.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_edit_portata)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(10, 0, 10, 0)
        self.icon_edit_portata = QToolButton(self.frame_edit_portata)
        self.icon_edit_portata.setObjectName(u"icon_edit_portata")

        self.horizontalLayout_20.addWidget(self.icon_edit_portata)


        self.gridLayout.addWidget(self.frame_edit_portata, 0, 0, 1, 2)


        self.verticalLayout_7.addWidget(self.frame_portata_on_click)

        self.frame_delete_portata = QFrame(self.frame_view_ingridients_delete)
        self.frame_delete_portata.setObjectName(u"frame_delete_portata")
        self.frame_delete_portata.setMaximumSize(QSize(16777215, 50))
        self.frame_delete_portata.setFrameShape(QFrame.NoFrame)
        self.frame_delete_portata.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_delete_portata)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(10, 0, 10, 10)
        self.btn_delete_piatto = QPushButton(self.frame_delete_portata)
        self.btn_delete_piatto.setObjectName(u"btn_delete_piatto")
        sizePolicy1.setHeightForWidth(self.btn_delete_piatto.sizePolicy().hasHeightForWidth())
        self.btn_delete_piatto.setSizePolicy(sizePolicy1)
        self.btn_delete_piatto.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_piatto.setStyleSheet(u"QPushButton{ border: none;\n"
"background-color: #ff8c00;\n"
"font: 500 15pt \"Poppins\";\n"
"letter-spacing:0.2px;\n"
"/*border: 2px solid rgb(255, 170, 0);*/\n"
"border-radius: 15px;\n"
"color: #fff;\n"
"}\n"
"QPushButton:focus:pressed{font: 500 13.5pt \"Poppins\";\n"
"	background-color: #ff8c00;}\n"
"QPushButton:hover{background-color: #ff8c00;}")
        self.btn_delete_piatto.setAutoRepeat(False)

        self.horizontalLayout_19.addWidget(self.btn_delete_piatto)


        self.verticalLayout_7.addWidget(self.frame_delete_portata)


        self.horizontalLayout_18.addWidget(self.frame_view_ingridients_delete)


        self.gridLayout_4.addWidget(self.frame_list_and_new_piatto, 1, 0, 1, 1)

        self.frame_categorie_menu = QFrame(self.MenuPage)
        self.frame_categorie_menu.setObjectName(u"frame_categorie_menu")
        self.frame_categorie_menu.setMinimumSize(QSize(0, 0))
        self.frame_categorie_menu.setMaximumSize(QSize(16777215, 65))
        self.frame_categorie_menu.setStyleSheet(u"background-color: #ffffff;\n"
"border-radius: 20px;")
        self.frame_categorie_menu.setFrameShape(QFrame.NoFrame)
        self.frame_categorie_menu.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_categorie_menu)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.table_categorie_menu = QTableWidget(self.frame_categorie_menu)
        if (self.table_categorie_menu.columnCount() < 10):
            self.table_categorie_menu.setColumnCount(10)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_categorie_menu.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_categorie_menu.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_categorie_menu.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_categorie_menu.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_categorie_menu.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_categorie_menu.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_categorie_menu.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_categorie_menu.setHorizontalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_categorie_menu.setHorizontalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_categorie_menu.setHorizontalHeaderItem(9, __qtablewidgetitem13)
        if (self.table_categorie_menu.rowCount() < 1):
            self.table_categorie_menu.setRowCount(1)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_categorie_menu.setVerticalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_categorie_menu.setItem(0, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_categorie_menu.setItem(0, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_categorie_menu.setItem(0, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_categorie_menu.setItem(0, 3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_categorie_menu.setItem(0, 4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_categorie_menu.setItem(0, 5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_categorie_menu.setItem(0, 6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_categorie_menu.setItem(0, 7, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_categorie_menu.setItem(0, 8, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_categorie_menu.setItem(0, 9, __qtablewidgetitem24)
        self.table_categorie_menu.setObjectName(u"table_categorie_menu")
        self.table_categorie_menu.setStyleSheet(u"QTableView::item {\n"
"	border-radius: 18px;\n"
"	background-color: rgb(255, 227, 195);\n"
"	margin-left: 10px;\n"
"	height: 20px!important;\n"
"	color: #ff8c00;\n"
"	margin-top: 10px;\n"
"}\n"
"\n"
"QTableView::item:focus {background-color: #ff8c00; color: #fff;}\n"
"QTableView::item:active {background-color: #ff8c00; color: #fff;}\n"
"QTableView::item:hover {background-color: #ff8c00; color: #fff;}\n"
"\n"
" QScrollBar:horizontal {\n"
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
        self.table_categorie_menu.setFrameShape(QFrame.NoFrame)
        self.table_categorie_menu.setGridStyle(Qt.NoPen)
        self.table_categorie_menu.horizontalHeader().setVisible(False)
        self.table_categorie_menu.verticalHeader().setVisible(False)
        self.table_categorie_menu.verticalHeader().setDefaultSectionSize(50)

        self.horizontalLayout_11.addWidget(self.table_categorie_menu)


        self.gridLayout_4.addWidget(self.frame_categorie_menu, 0, 0, 1, 1)

        self.Pages_widget.addWidget(self.MenuPage)
        self.PersonalePage = QWidget()
        self.PersonalePage.setObjectName(u"PersonalePage")
        self.verticalLayout_8 = QVBoxLayout(self.PersonalePage)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 0)
        self.main_frame_personal_page = QFrame(self.PersonalePage)
        self.main_frame_personal_page.setObjectName(u"main_frame_personal_page")
        self.main_frame_personal_page.setFrameShape(QFrame.NoFrame)
        self.main_frame_personal_page.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.main_frame_personal_page)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 10)
        self.content_frame_personal_page = QFrame(self.main_frame_personal_page)
        self.content_frame_personal_page.setObjectName(u"content_frame_personal_page")
        self.content_frame_personal_page.setFrameShape(QFrame.StyledPanel)
        self.content_frame_personal_page.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.content_frame_personal_page)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_top_content = QFrame(self.content_frame_personal_page)
        self.frame_top_content.setObjectName(u"frame_top_content")
        self.frame_top_content.setFrameShape(QFrame.StyledPanel)
        self.frame_top_content.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_top_content)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_search = QFrame(self.frame_top_content)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setMinimumSize(QSize(0, 60))
        self.frame_search.setMaximumSize(QSize(16777215, 16777215))
        self.frame_search.setStyleSheet(u"background-color: #fff;\n"
"border-radius: 20px;")
        self.frame_search.setFrameShape(QFrame.NoFrame)
        self.frame_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_search)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(10, 10, 0, 0)
        self.frame_title = QFrame(self.frame_search)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setMaximumSize(QSize(150, 16777215))
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(15, 0, 0, 0)
        self.label_titolo_personal_page = QLabel(self.frame_title)
        self.label_titolo_personal_page.setObjectName(u"label_titolo_personal_page")
        self.label_titolo_personal_page.setStyleSheet(u"font: 700 25pt \"Poppins\";\n"
"color: #1921FA;\n"
"letter-spacing: 1px;\n"
"")

        self.horizontalLayout_15.addWidget(self.label_titolo_personal_page, 0, Qt.AlignLeft)


        self.horizontalLayout_22.addWidget(self.frame_title, 0, Qt.AlignLeft)

        self.frame_btn_search = QFrame(self.frame_search)
        self.frame_btn_search.setObjectName(u"frame_btn_search")
        self.frame_btn_search.setMinimumSize(QSize(50, 0))
        self.frame_btn_search.setFrameShape(QFrame.StyledPanel)
        self.frame_btn_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_btn_search)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 10, 10, 10)
        self.frame_lineEdit = QFrame(self.frame_btn_search)
        self.frame_lineEdit.setObjectName(u"frame_lineEdit")
        self.frame_lineEdit.setMinimumSize(QSize(0, 0))
        self.frame_lineEdit.setMaximumSize(QSize(200, 16777215))
        self.frame_lineEdit.setFrameShape(QFrame.StyledPanel)
        self.frame_lineEdit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_lineEdit)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 30, 0)
        self.lineEdit = QLineEdit(self.frame_lineEdit)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"border: solid transparent;\n"
"border-bottom: 2px solid #1921FA;\n"
"font: 400 12pt \"Poppins\";")

        self.horizontalLayout_23.addWidget(self.lineEdit)

        self.btn_search = QToolButton(self.frame_lineEdit)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setStyleSheet(u"")

        self.horizontalLayout_23.addWidget(self.btn_search)


        self.horizontalLayout_24.addWidget(self.frame_lineEdit)

        self.add_nuovo_personale = QPushButton(self.frame_btn_search)
        self.add_nuovo_personale.setObjectName(u"add_nuovo_personale")
        self.add_nuovo_personale.setCursor(QCursor(Qt.PointingHandCursor))
        self.add_nuovo_personale.setStyleSheet(u"QPushButton{ background-color: #1921FA;\n"
"color: #fff;\n"
"font: 400 12pt \"Poppins\";\n"
"padding: 9px;\n"
"letter-spacing:0.2px ;\n"
"border-radius: 5px;\n"
"margin-right: 5px;\n"
"}\n"
"QPushButton:focus:pressed{font: 500 12pt \"Poppins\";}\n"
"QPushButton:hover{font: 500 12pt \"Poppins\";}\n"
"/*rgb(99, 159, 171)*/")

        self.horizontalLayout_24.addWidget(self.add_nuovo_personale, 0, Qt.AlignRight)


        self.horizontalLayout_22.addWidget(self.frame_btn_search, 0, Qt.AlignRight)


        self.gridLayout_6.addWidget(self.frame_search, 0, 0, 1, 1)

        self.table_personale = QTableWidget(self.frame_top_content)
        if (self.table_personale.columnCount() < 5):
            self.table_personale.setColumnCount(5)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_personale.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_personale.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_personale.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_personale.setHorizontalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_personale.setHorizontalHeaderItem(4, __qtablewidgetitem29)
        self.table_personale.setObjectName(u"table_personale")
        self.table_personale.setStyleSheet(u"QScrollBar:vertical {\n"
"width: 7px;\n"
"		background-color: white;\n"
"		margin: 0px 0px 0px 0px;\n"
"		border-radius: 10px;\n"
"    }\n"
"QScrollBar::handle {\n"
"        background: rgb(125, 125, 125);\n"
"        border-radius: 2px;\n"
"    }\n"
"QTableView {\n"
" background-color: #fff;\n"
" border-radius: 20px;\n"
"}\n"
"QTableView::item {\n"
"	background-color: rgb(249, 249, 249);\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"	margin-left: 10px;\n"
"	height: 20px!important;\n"
"	margin-top: 10px;\n"
"}\n"
"\n"
"QTableView::item:focus {background-color: rgb(255, 170, 0);}\n"
"QTableView::item:hover {background-color: rgb(255, 170, 0);}")
        self.table_personale.setFrameShape(QFrame.NoFrame)
        self.table_personale.setFrameShadow(QFrame.Plain)
        self.table_personale.setLineWidth(1)
        self.table_personale.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_personale.setTabKeyNavigation(False)
        self.table_personale.setProperty("showDropIndicator", False)
        self.table_personale.setShowGrid(True)
        self.table_personale.setGridStyle(Qt.SolidLine)
        self.table_personale.setCornerButtonEnabled(False)
        self.table_personale.setRowCount(0)
        self.table_personale.horizontalHeader().setVisible(False)
        self.table_personale.horizontalHeader().setCascadingSectionResizes(False)
        self.table_personale.horizontalHeader().setMinimumSectionSize(34)
        self.table_personale.horizontalHeader().setDefaultSectionSize(180)
        self.table_personale.horizontalHeader().setHighlightSections(True)
        self.table_personale.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_personale.horizontalHeader().setStretchLastSection(False)
        self.table_personale.verticalHeader().setVisible(False)
        self.table_personale.verticalHeader().setDefaultSectionSize(150)
        self.table_personale.verticalHeader().setHighlightSections(True)
        self.table_personale.verticalHeader().setStretchLastSection(False)

        self.gridLayout_6.addWidget(self.table_personale, 3, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_top_content, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.content_frame_personal_page, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.main_frame_personal_page)

        self.Pages_widget.addWidget(self.PersonalePage)
        self.StatistichePage = QWidget()
        self.StatistichePage.setObjectName(u"StatistichePage")
        self.verticalLayout_9 = QVBoxLayout(self.StatistichePage)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_statistiche = QLabel(self.StatistichePage)
        self.label_statistiche.setObjectName(u"label_statistiche")
        font = QFont()
        font.setFamily(u"Dubai")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_statistiche.setFont(font)
        self.label_statistiche.setStyleSheet(u"color:white;")
        self.label_statistiche.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_statistiche)

        self.Pages_widget.addWidget(self.StatistichePage)
        self.OrdiniPage = QWidget()
        self.OrdiniPage.setObjectName(u"OrdiniPage")
        self.horizontalLayout_6 = QHBoxLayout(self.OrdiniPage)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_aggiungi_ordine = QFrame(self.OrdiniPage)
        self.frame_aggiungi_ordine.setObjectName(u"frame_aggiungi_ordine")
        self.frame_aggiungi_ordine.setFrameShape(QFrame.StyledPanel)
        self.frame_aggiungi_ordine.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_aggiungi_ordine)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 10, 10, 0)
        self.frame_nuovo_ordine = QFrame(self.frame_aggiungi_ordine)
        self.frame_nuovo_ordine.setObjectName(u"frame_nuovo_ordine")
        self.frame_nuovo_ordine.setFrameShape(QFrame.StyledPanel)
        self.frame_nuovo_ordine.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_nuovo_ordine)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(10, 0, 10, 10)
        self.frame_seleziona_tavolo = QFrame(self.frame_nuovo_ordine)
        self.frame_seleziona_tavolo.setObjectName(u"frame_seleziona_tavolo")
        self.frame_seleziona_tavolo.setMinimumSize(QSize(0, 60))
        self.frame_seleziona_tavolo.setMaximumSize(QSize(16777215, 60))
        self.frame_seleziona_tavolo.setStyleSheet(u"background-color: #fff;\n"
"border-radius: 20px;")
        self.frame_seleziona_tavolo.setFrameShape(QFrame.NoFrame)
        self.frame_seleziona_tavolo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_seleziona_tavolo)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 30, 0)
        self.label_tavolo = QLabel(self.frame_seleziona_tavolo)
        self.label_tavolo.setObjectName(u"label_tavolo")
        self.label_tavolo.setStyleSheet(u"font: 500 12pt \"Poppins\";")

        self.horizontalLayout_7.addWidget(self.label_tavolo)

        self.comboBox_seleziona_tavolo = QComboBox(self.frame_seleziona_tavolo)
        self.comboBox_seleziona_tavolo.setObjectName(u"comboBox_seleziona_tavolo")
        sizePolicy1.setHeightForWidth(self.comboBox_seleziona_tavolo.sizePolicy().hasHeightForWidth())
        self.comboBox_seleziona_tavolo.setSizePolicy(sizePolicy1)
        self.comboBox_seleziona_tavolo.setMinimumSize(QSize(150, 30))
        self.comboBox_seleziona_tavolo.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox_seleziona_tavolo.setStyleSheet(u"border: 2px solid #ff8c00;\n"
"border-radius: 10px;\n"
"background-color:transparent;\n"
"box-shadow: none;")

        self.horizontalLayout_7.addWidget(self.comboBox_seleziona_tavolo, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_12.addWidget(self.frame_seleziona_tavolo)

        self.frame_seleziona_categoria = QFrame(self.frame_nuovo_ordine)
        self.frame_seleziona_categoria.setObjectName(u"frame_seleziona_categoria")
        self.frame_seleziona_categoria.setMinimumSize(QSize(0, 60))
        self.frame_seleziona_categoria.setMaximumSize(QSize(16777215, 60))
        self.frame_seleziona_categoria.setStyleSheet(u"background-color: #fff;\n"
"border-radius: 20px;")
        self.frame_seleziona_categoria.setFrameShape(QFrame.StyledPanel)
        self.frame_seleziona_categoria.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_seleziona_categoria)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.table_categorie = QTableWidget(self.frame_seleziona_categoria)
        if (self.table_categorie.rowCount() < 1):
            self.table_categorie.setRowCount(1)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_categorie.setVerticalHeaderItem(0, __qtablewidgetitem30)
        self.table_categorie.setObjectName(u"table_categorie")
        self.table_categorie.setStyleSheet(u"QTableView::item {\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 227, 195);;\n"
"	margin-left: 10px;\n"
"	height: 20px!important;\n"
"	color: #ff8c00;\n"
"	margin-top: 10px;\n"
"}\n"
"\n"
"QTableView::item:focus {background-color: #ff8c00; color: #fff;}\n"
"QTableView::item:hover {background-color: #ff8c00; color: #fff;}")
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
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(200)
        sizePolicy2.setVerticalStretch(200)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
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
"    border-radius: 10px;\n"
"	color: black;\n"
"	height: 20px!important;\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"QTableView::item:focus {background-color: rgb(255, 170, 0); color: white;}\n"
"QTableView::item:hover {background-color: rgb(255, 170, 0); color: white;}")
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.DoubleClicked)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.NoPen)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(100)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_9.addWidget(self.tableWidget)


        self.verticalLayout_12.addWidget(self.frame_seleziona_portata)


        self.horizontalLayout_13.addWidget(self.frame_nuovo_ordine)

        self.frame_ordine_view = QFrame(self.frame_aggiungi_ordine)
        self.frame_ordine_view.setObjectName(u"frame_ordine_view")
        self.frame_ordine_view.setMaximumSize(QSize(300, 16777215))
        self.frame_ordine_view.setStyleSheet(u"background-color: #fff;\n"
"border-radius: 20px;")
        self.frame_ordine_view.setFrameShape(QFrame.NoFrame)
        self.frame_ordine_view.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_ordine_view)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 10, 0, 10)
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
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 300, 451))
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
        self.verticalLayout_16.setContentsMargins(10, 0, 10, 0)
        self.btn_elimina_ordine = QPushButton(self.frame_8)
        self.btn_elimina_ordine.setObjectName(u"btn_elimina_ordine")
        self.btn_elimina_ordine.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_elimina_ordine.setStyleSheet(u"border-radius: 7px;\n"
"color: #fff;\n"
"font: 500 11pt \"Poppins\";\n"
"background-color: #ff8c00;\n"
"padding: 7px\n"
"")

        self.verticalLayout_16.addWidget(self.btn_elimina_ordine)

        self.btn_invio_ordine = QPushButton(self.frame_8)
        self.btn_invio_ordine.setObjectName(u"btn_invio_ordine")
        self.btn_invio_ordine.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_invio_ordine.setStyleSheet(u"border-radius: 7px;\n"
"color: #fff;\n"
"font: 500 11pt \"Poppins\";\n"
"background-color: #ff8c00;\n"
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
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.SettingsPage)
        self.label.setObjectName(u"label")

        self.verticalLayout_17.addWidget(self.label)

        self.Pages_widget.addWidget(self.SettingsPage)

        self.verticalLayout_5.addWidget(self.Pages_widget)


        self.horizontalLayout_2.addWidget(self.frame_pages)


        self.gridLayout_3.addWidget(self.content, 2, 2, 1, 1)

        self.frame_left_menu = QFrame(self.centralwidget)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy1.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy1)
        self.frame_left_menu.setMinimumSize(QSize(60, 0))
        self.frame_left_menu.setMaximumSize(QSize(60, 16777215))
        self.frame_left_menu.setStyleSheet(u"background-color: white;\n"
"color: black;\n"
"border-radius: 3px;")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.frame_left_menu)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy1.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy1)
        self.btn_toggle.setMinimumSize(QSize(0, 40))
        self.btn_toggle.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	background-color: transparent\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(123, 114, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_toggle)

        self.btn_home = QPushButton(self.frame_left_menu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(0, 0))
        self.btn_home.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	background-color: transparent;\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(123, 114, 255);\n"
"	border: 0px solid;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_home)

        self.btn_menu = QPushButton(self.frame_left_menu)
        self.btn_menu.setObjectName(u"btn_menu")
        sizePolicy1.setHeightForWidth(self.btn_menu.sizePolicy().hasHeightForWidth())
        self.btn_menu.setSizePolicy(sizePolicy1)
        self.btn_menu.setMinimumSize(QSize(0, 0))
        self.btn_menu.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	background-color: transparent;\n"
"	border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(123, 114, 255);\n"
"	border: 0px solid;\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_menu)

        self.btn_personale = QPushButton(self.frame_left_menu)
        self.btn_personale.setObjectName(u"btn_personale")
        sizePolicy1.setHeightForWidth(self.btn_personale.sizePolicy().hasHeightForWidth())
        self.btn_personale.setSizePolicy(sizePolicy1)
        self.btn_personale.setMinimumSize(QSize(0, 0))
        self.btn_personale.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	background-color: transparent\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(123, 114, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_personale)

        self.btn_statistiche = QPushButton(self.frame_left_menu)
        self.btn_statistiche.setObjectName(u"btn_statistiche")
        sizePolicy1.setHeightForWidth(self.btn_statistiche.sizePolicy().hasHeightForWidth())
        self.btn_statistiche.setSizePolicy(sizePolicy1)
        self.btn_statistiche.setMinimumSize(QSize(0, 0))
        self.btn_statistiche.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	background-color: transparent\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(123, 114, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_statistiche)

        self.btn_settings = QPushButton(self.frame_left_menu)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy1.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy1)
        self.btn_settings.setMinimumSize(QSize(0, 0))
        self.btn_settings.setContextMenuPolicy(Qt.PreventContextMenu)
        self.btn_settings.setStyleSheet(u"QPushButton {\n"
"	color:black;\n"
"	background-color: transparent\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(123, 114, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.btn_settings)


        self.gridLayout_3.addWidget(self.frame_left_menu, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_date_time.setText(QCoreApplication.translate("MainWindow", u"Date and Time", None))
        self.label_posti.setText(QCoreApplication.translate("MainWindow", u"25/50", None))
        self.btn_home_top.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_add_tavolo.setText(QCoreApplication.translate("MainWindow", u"iconaAggiungi Tavolo", None))
        self.btn_add_ordine.setText(QCoreApplication.translate("MainWindow", u"icona Aggiungi Ordine", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Icona Logout", None))
        ___qtablewidgetitem = self.tableWidget_tavoli.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem1 = self.tableWidget_tavoli.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget_tavoli.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem3 = self.tableWidget_tavoli.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        self.btn_cliente_tavolo.setText(QCoreApplication.translate("MainWindow", u"Visualizza Cliente del Tavolo", None))
        self.btn_delete_ordine_tavolo.setText(QCoreApplication.translate("MainWindow", u"Icona Cancella Ordini", None))
        self.label_ordine_tavolo.setText("")
        self.label_datetime_ordine_tavolo.setText("")
        self.btn_stampa_scontrino.setText(QCoreApplication.translate("MainWindow", u"Totale: 0\u20ac", None))
        self.label_menu_info.setText(QCoreApplication.translate("MainWindow", u"Clicca le portate per visualizzare le informazioni", None))

        __sortingEnabled = self.list_piatti.isSortingEnabled()
        self.list_piatti.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_piatti.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem1 = self.list_piatti.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem2 = self.list_piatti.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.list_piatti.setSortingEnabled(__sortingEnabled)

        self.btn_new_piatto.setText(QCoreApplication.translate("MainWindow", u"Aggiungi nuovo piatto", None))
        self.label_id_portata.setText("")
        self.label_categoria_portata.setText("")
        self.label_ingredienti_portata.setText("")
        self.label_prezzo_portata.setText("")
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"ID Portata", None))
        self.label_categoria.setText(QCoreApplication.translate("MainWindow", u"Categoria Portata", None))
        self.label_ingredienti.setText(QCoreApplication.translate("MainWindow", u"Ingredienti Portata", None))
        self.label_prezzo.setText(QCoreApplication.translate("MainWindow", u"Prezzo", None))
        self.icon_edit_portata.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.btn_delete_piatto.setText(QCoreApplication.translate("MainWindow", u"Elimina Piatto", None))
        ___qtablewidgetitem4 = self.table_categorie_menu.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem5 = self.table_categorie_menu.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem6 = self.table_categorie_menu.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem7 = self.table_categorie_menu.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem8 = self.table_categorie_menu.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem9 = self.table_categorie_menu.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem10 = self.table_categorie_menu.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem11 = self.table_categorie_menu.horizontalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem12 = self.table_categorie_menu.horizontalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem13 = self.table_categorie_menu.horizontalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem14 = self.table_categorie_menu.verticalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled1 = self.table_categorie_menu.isSortingEnabled()
        self.table_categorie_menu.setSortingEnabled(False)
        ___qtablewidgetitem15 = self.table_categorie_menu.item(0, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"ag", None));
        ___qtablewidgetitem16 = self.table_categorie_menu.item(0, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"asdlkj", None));
        ___qtablewidgetitem17 = self.table_categorie_menu.item(0, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"lkjlkjlk", None));
        ___qtablewidgetitem18 = self.table_categorie_menu.item(0, 3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"lkjlkjlkj", None));
        ___qtablewidgetitem19 = self.table_categorie_menu.item(0, 4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"lkjlkjlkj", None));
        ___qtablewidgetitem20 = self.table_categorie_menu.item(0, 5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"lkjlkjlk", None));
        ___qtablewidgetitem21 = self.table_categorie_menu.item(0, 6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"jlkj", None));
        ___qtablewidgetitem22 = self.table_categorie_menu.item(0, 7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"lkjlk", None));
        ___qtablewidgetitem23 = self.table_categorie_menu.item(0, 8)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"jlk", None));
        ___qtablewidgetitem24 = self.table_categorie_menu.item(0, 9)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"k", None));
        self.table_categorie_menu.setSortingEnabled(__sortingEnabled1)

        self.label_titolo_personal_page.setText(QCoreApplication.translate("MainWindow", u"Team", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cerca", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.add_nuovo_personale.setText(QCoreApplication.translate("MainWindow", u"Aggiungi", None))
        ___qtablewidgetitem25 = self.table_personale.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem26 = self.table_personale.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem27 = self.table_personale.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem28 = self.table_personale.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem29 = self.table_personale.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        self.label_statistiche.setText(QCoreApplication.translate("MainWindow", u"STATISTICHE", None))
        self.label_tavolo.setText(QCoreApplication.translate("MainWindow", u"Aggiungi Ordine", None))
        ___qtablewidgetitem30 = self.table_categorie.verticalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem31 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem32 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem33 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem34 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem35 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        self.btn_elimina_ordine.setText(QCoreApplication.translate("MainWindow", u"Elimina ultima aggiunta", None))
        self.btn_invio_ordine.setText(QCoreApplication.translate("MainWindow", u"Invia Ordine", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"TOGGLE", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Tavoli", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btn_personale.setText(QCoreApplication.translate("MainWindow", u"Personale", None))
        self.btn_statistiche.setText(QCoreApplication.translate("MainWindow", u"Statistiche", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

