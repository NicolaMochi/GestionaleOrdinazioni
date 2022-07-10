from PyQt5.QtWidgets import QMainWindow
from PySide2.QtCore import QSize, QTimer, QDateTime

from Categorie_list.controller.CategorieListController import CategorieListController
#from Categorie_list.view.categorie_list_view import categorie_list_view
from Menu.controller.MenuController import MenuController
from Menu.view.MenuView import MenuView
from Menu.view.NewPortataView import NewPortataView
#from Ordini_list.controller.OrdiniListController import OrdiniListController
from Ordine.view.NuovoOrdineView import NuovoOrdineView
from Personale.view.PersonaleView import PersonaleView
from Personale_list.view.PersonaleListView import PersonaleListView
from Tavoli_list.controller.TavoloListController import TavoloListController
from Tavolo.view.NewTavoloView import NewTavoloView
from Tavoli_list.view.TavoloListView import TavoloListView
from Utilities.UIFunctions import UIFunctions
from Utilities.Utilities import Utilities
from ui_home import ui_home
from Login.view.LoginView import LoginView
from Personale_list.controller.PersonaleListController import PersonaleListController
from PySide2.QtWidgets import *


class HomeView(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.home = ui_home()
        self.vista_login = LoginView()
        self.flag_primo_login = True
        self.uifunctions = UIFunctions()
        self.controller_lista_personale = PersonaleListController()
        self.add_personale_view = PersonaleView(self.home, self.controller_lista_personale)
        self.personale_view = PersonaleListView(self.home, self.controller_lista_personale, self.uifunctions)

        self.lista_tavoli_controller = TavoloListController()
        self.utility = Utilities(self.lista_tavoli_controller, self.home)
        self.lista_categorie = CategorieListController()
        self.menu = MenuController()
        #self.categorie_view = categorie_list_view(self.lista_categorie, self.home, self.menu)
        self.menu_vista = MenuView(self.home, self.menu, self.lista_categorie)
        self.nuova_portata_view = NewPortataView(self.menu_vista, self.menu, self.lista_categorie)

        #self.lista_ordini = OrdiniListController()
        self.vista_nuovo_ordine = NuovoOrdineView(self.lista_categorie, self.home, self.lista_tavoli_controller, self.menu)
        self.tavolo_view = TavoloListView(self.home, self.lista_tavoli_controller, self.vista_nuovo_ordine)
        self.add_tavolo_view = NewTavoloView(self.home, self.lista_tavoli_controller, self.tavolo_view)

        self.timer = QTimer()
        self.timer.timeout.connect(self.start_date_time)

        self.start_program()

    def start_program(self):
        self.timer.stop()
        self.vista_login.login.setupUi(self)
        self.vista_login.login.btn_enter.clicked.connect(self.controllo_login)
        self.setMinimumSize(QSize(353, 326))

    def start_date_time(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString("dddd, d MMMM hh:mm:ss")
        self.home.label_date_time.setText(timeDisplay)

    def controllo_login(self):
        username = self.vista_login.login.lineEdit_username.text()
        password = self.vista_login.login.lineEdit_password.text()
        codice_personale = self.controller_lista_personale.controllo_login(username, password)

        #if True:
        if codice_personale != 404:
            self.home.setupUi(self)
            self.show()
            self.timer.start(1000)
            ## Posiziono la schermata al centro del desktop
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())

            self.home.btn_add_ordine.clicked.connect(self.home.label_ordine_tavolo.setText("Devi prima selezionare un Tavolo"))
            if self.flag_primo_login:
                 self.tavolo_view.fill_list_tavoli_widget(self.lista_tavoli_controller.get_lista(), True)
                 self.flag_primo_login = False
            else:
                 self.tavolo_view.fill_list_tavoli_widget(self.lista_tavoli_controller.get_lista(), True)

        #richiama funzione di menu_view che popola il widget con le portate presenti nel menu

            self.home.btn_logout.clicked.connect(self.start_program)
            self.home.btn_menu.clicked.connect(lambda: self.menu_vista.view(self.nuova_portata_view, codice_personale))
            #self.home.btn_add_ordine.clicked.connect(self.vista_ordine)
            self.home.btn_home.clicked.connect(lambda: self.home.Pages_widget.setCurrentWidget(self.home.TavoliPage))
            self.home.btn_home_top.clicked.connect(lambda: self.home.Pages_widget.setCurrentWidget(self.home.TavoliPage))
            self.home.btn_personale.clicked.connect(lambda: self.personale_view.view(codice_personale))
            self.home.btn_add_tavolo.clicked.connect(lambda: self.add_tavolo_view.show())
            self.home.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 100, self.home, True))

            self.home.tableWidget.itemClicked.connect(self.vista_nuovo_ordine.add_to_order)
            self.home.btn_elimina_ordine.clicked.connect(self.vista_nuovo_ordine.elimina_ultima_aggiunta)
            #self.home.btn_invio_ordine.clicked.connect(self.send_order)
            self.home.btn_delete_ordine_tavolo.clicked.connect(self.tavolo_view.delete_ordine)
            self.home.btn_delete_tavolo.clicked.connect(self.tavolo_view.delete_tavolo)

            self.utility.start_posti()

        else:
            self.vista_login.login.label_message.setText("Dati non validi, riprova")
            self.vista_login.login.lineEdit_username.clear()
            self.vista_login.login.lineEdit_password.clear()






