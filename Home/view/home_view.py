from PyQt5.QtWidgets import QMainWindow

from Categorie_list.controller.categorie_list_controller import categorie_list_controller
from Categorie_list.view.categorie_list_view import categorie_list_view
from Ingredienti_list.controller.ingredienti_list_controller import ingredienti_list_controller
from Menu.controller.menu_controller import menu_controller
from Menu.view.menu_view import menu_view
from Menu.view.new_portata_view import new_portata_view
from Ordini_list.controller.ordini_list_controller import ordini_list_controller
from Ordini_list.view.nuovo_ordine_view import nuovo_ordine_view
from Tavoli_list.controller.tavolo_list_controller import tavolo_list_controller
from Tavoli_list.view.new_tavolo_view import new_tavolo_view
from Tavoli_list.view.tavolo_list_view import tavolo_list_view
from Utilities.UIFunctions import UIFunctions
from Utilities.utilities import utilities
from ui_home import ui_home
from Login.view.login_view import login_view
from Personale_credenziali_list.controller.personale_list_controller import personale_list_controller
from PySide2.QtWidgets import *


class home_view(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.home = ui_home()
        self.vista_login = login_view()
        self.controller_lista_personale = personale_list_controller()

        self.lista_tavoli_controller = tavolo_list_controller()
        self.tavolo_view = tavolo_list_view(self.home, self.lista_tavoli_controller)
        self.add_tavolo_view = new_tavolo_view(self.home, self.lista_tavoli_controller, self.tavolo_view)

        self.lista_categorie = categorie_list_controller()
        self.lista_ingredienti = ingredienti_list_controller()
        self.menu = menu_controller()
        self.categorie_view = categorie_list_view(self.lista_categorie, self.home, self.menu)
        self.menu_vista = menu_view(self.home, self.menu, self.categorie_view)
        self.nuova_portata_view = new_portata_view(self.menu_vista, self.menu, self.lista_ingredienti, self.lista_categorie)

        self.lista_ordini = ordini_list_controller()
        self.utility = utilities(self.home, self.lista_tavoli_controller)
        self.vista_nuovo_ordine = nuovo_ordine_view(self.categorie_view, self.lista_categorie, self.utility, self.home, self.lista_ordini, self.lista_tavoli_controller, self.menu, self.menu_vista)


        self.partenza()

    def partenza(self):
        self.vista_login.login.setupUi(self)
        self.vista_login.login.btn_enter.clicked.connect(self.controllo_login)

    def aggiungiTavolo(self):
        self.add_tavolo_view.show()

    def vista_menu(self):
        self.menu_vista.view(self.nuova_portata_view)

    def vista_ordine(self):
         self.vista_nuovo_ordine.view()

    def send_order(self):
        self.vista_nuovo_ordine.invia_ordine()
        #self.utility.posti_rimanenti()

    def controllo_login(self):
        username = self.vista_login.login.lineEdit_username.text()
        password = self.vista_login.login.lineEdit_password.text()
        controllo_result = self.controller_lista_personale.controllo_login(username, password)

        if True:
        #if controllo_result != 0:
            self.home.setupUi(self)
            self.show()

            self.tavolo_view.fill_list_tavoli_widget(self.lista_tavoli_controller.get_lista())
            #richiama funzione di menu_view che popola il widget con le portate presenti nel menu

            self.home.btn_logout.clicked.connect(self.partenza)
            self.home.btn_menu.clicked.connect(self.vista_menu)
            self.home.btn_add_ordine.clicked.connect(self.vista_ordine)
            self.home.btn_statistiche.clicked.connect(lambda: self.home.Pages_widget.setCurrentWidget(self.home.StatistichePage))
            self.home.btn_home.clicked.connect(lambda: self.home.Pages_widget.setCurrentWidget(self.home.TavoliPage))
            self.home.btn_home_top.clicked.connect(lambda: self.home.Pages_widget.setCurrentWidget(self.home.TavoliPage))
            self.home.btn_personale.clicked.connect(lambda: self.home.Pages_widget.setCurrentWidget(self.home.PersonalePage))
            self.home.btn_settings.clicked.connect(lambda: self.home.Pages_widget.setCurrentWidget(self.home.SettingsPage))
            self.home.btn_add_tavolo.clicked.connect(self.aggiungiTavolo)
            #self.home.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, self.home, True))
            self.home.tableWidget.itemClicked.connect(self.vista_nuovo_ordine.add_to_order)
            self.home.btn_elimina_ordine.clicked.connect(self.vista_nuovo_ordine.elimina_ultima_aggiunta)
            self.home.btn_invio_ordine.clicked.connect(self.send_order)
            self.home.btn_delete_ordine_tavolo.clicked.connect(self.tavolo_view.delete_ordine)
            self.utility.posti()

        else:
            self.vista_login.login.label_message.setText("Dati non validi, riprova")
            self.vista_login.login.label_message.setStyleSheet("color: #fd4902; font: 11pt 'Dubai';")
            self.vista_login.login.lineEdit_username.clear()
            self.vista_login.login.lineEdit_password.clear()





