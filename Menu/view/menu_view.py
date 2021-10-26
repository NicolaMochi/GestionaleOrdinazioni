from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QTableWidgetItem, QAbstractItemView

from Utilities.UIFunctions import UIFunctions


class menu_view:
    def __init__(self, gui_home, menu, categoria_view, uifunctions):
        self.home = gui_home
        self.menu = menu
        self.portata_selected = None
        self.portata_id = None
        self.categoria_view = categoria_view
        self.uifunctions = uifunctions

        self.row = 0
        self.column = 0

    def update_menu_widget_list(self):
        for i in range(len(self.menu.get_menu())):
            self.home.list_piatti.addItem(str(self.menu.get_menu()[i].nome))

    def delete_portata(self):
        self.menu.delete_portata(self.portata_selected)
        portata_deleted = self.home.list_piatti.takeItem(self.portata_selected.piatto_id)
        self.home.label_ingredienti_portata.clear()
        self.home.label_id_portata.clear()
        self.home.label_prezzo_portata.clear()
        self.home.label_categoria_portata.clear()

    def show_portata(self):
        ## HO SBAGLIATO A CONSIDERARE LA RIGA PER PRENDERE LA PORTATA CLICCATA
        ## Vorrei che ci fosse un modo per prendere il testo
        self.portata_id = self.home.list_piatti.currentItem().text()
        self.portata_selected = self.menu.get_portata_from_name(self.portata_id)
        self.home.label_id_portata.setText(str(self.portata_selected.piatto_id))
        self.home.label_prezzo_portata.setText(str(self.portata_selected.prezzo))
        self.home.label_categoria_portata.setText(self.portata_selected.categoria)
        self.home.label_ingredienti_portata.setText(self.stampa_ingredienti_portata(self.portata_selected))
        self.home.btn_delete_piatto.clicked.connect(self.delete_portata)

    ## Questa funzione riempie la tabella delle portate con i dati
    def fill_menu_to_order(self):
        self.row = 0
        self.column = 0
        for x in range(len(self.menu.get_menu())):
            font_nuovo_item = QFont("Dubai", 14, QFont.Medium)
            nome_portata = self.menu.get_menu()[x].get_nome_portata()
            nuovo_item = QTableWidgetItem()
            nuovo_item.setText(nome_portata)
            nuovo_item.setTextAlignment(Qt.AlignHCenter)
            nuovo_item.setFont(font_nuovo_item)
            self.home.tableWidget.setItem(self.row, self.column, nuovo_item)
            self.column += 1
            if self.column % 5 == 0:
                self.row += 1
                self.column = 0

    ## Questa funzione setta le impostazioni grafiche della tabella e
    ## fa partire la funzione di inserimento dei dati
    def fill_table_to_order(self):
        # if len(self.menu.get_menu()) / 5 <= 1: self.home.tableWidget.setColumnCount(len(self.menu.get_menu()))
        # else: self.home.tableWidget.setColumnCount(5)
        # self.home.tableWidget.setRowCount((len(self.menu.get_menu()) / 5) + 1)
        # self.home.tableWidget.clear()
        # self.home.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.uifunctions.inizialize_ui_table(self.home.tableWidget, 5, self.menu.get_menu(), True)
        #self.fill_menu_to_order()

    ## funzione che prende il controller_menu e fa vedere la lista sul widget
    def add_to_menu_widget_list(self, nuova_portata):
        self.home.list_piatti.addItem(str(nuova_portata.__str__()))
        self.categoria_view.fill_categorie_to_order()

    def stampa_ingredienti_portata(self, portata):
        ingredienti_string = ''
        for i in range(len(portata.ingredienti)):
            ingredienti_string = ingredienti_string + portata.ingredienti[i].nome
        return ingredienti_string

    def show_portate_from_categorie_in_list(self):
        categoria_clicked = self.home.table_categorie_menu.currentItem()
        self.home.list_piatti.clear()
        if categoria_clicked.text() == "Vedi Tutti":
            self.update_menu_widget_list()
            return
        for i in range(len(self.menu.get_menu())):
            if self.menu.get_menu()[i].categoria == categoria_clicked.text():
                self.home.list_piatti.addItem(str(self.menu.get_menu()[i].nome))

    def view(self, nuova_portata):
        self.home.Pages_widget.setCurrentWidget(self.home.MenuPage)
        self.home.btn_new_piatto.clicked.connect(nuova_portata.show)
        self.home.list_piatti.itemClicked.connect(self.show_portata)
        self.categoria_view.fill_categorie_to_order()
        self.home.table_categorie_menu.cellClicked.connect(self.show_portate_from_categorie_in_list)
