from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QTableWidgetItem, QAbstractItemView

from Categorie_list.view.CategorieListView import CategorieListView
from Menu.view.EditPortataView import EditPortataView
from Utilities.UIFunctions import UIFunctions


class MenuView:
    def __init__(self, gui_home, menu_controller, categorie_controller):
        self.home = gui_home
        self.menu = menu_controller
        self.portata_selected = None
        self.portata_id = None
        self.categorie_controller = categorie_controller
        self.uifunctions = UIFunctions()
        self.edit_portata_view = EditPortataView(self.categorie_controller, self.home, self.menu)
        #self.categoria_view = categorie_list_view(self.lista_categorie, self.home, self.menu)

        self.categorie_view = CategorieListView(self.home, self, self.categorie_controller, self.menu)
        self.row = 0
        self.column = 0

    def update_menu_widget_list(self):
        for i in self.menu.get_menu():
            self.home.list_piatti.addItem(str(i.__str__()))

    def delete_portata(self):
        try:
            portata_nome = self.home.list_piatti.findItems(str(self.home.list_piatti.currentItem().text()),
                                                           QtCore.Qt.MatchExactly)
            portata_selected = self.menu.get_portata_from_name(portata_nome[0].text())
        except:
            print("non hai selezionato nessuna portata")
            #SCRIVILO NEL DESIGN
            return
        portata_deleted = self.home.list_piatti.takeItem(portata_selected.get_portata_id())
        self.home.label_ingredienti_portata.clear()
        self.home.label_id_portata.clear()
        self.home.label_prezzo_portata.clear()
        self.home.label_categoria_portata.clear()
        if(self.menu.check_categorie_after_delete(portata_selected.get_categoria(), self.menu.get_menu()))==1:
            self.categorie_controller.delete_categoria(self.categorie_controller.get_categoria_from_text(portata_selected.get_categoria()))
            self.uifunctions.fill_categorie_to_order(self.home, self.categorie_controller.get_lista())
        self.menu.delete_portata(portata_selected)
        print("Dopo aver eliminato le portate sono: \n")
        for x in self.menu.get_menu():
            print(x.__str__()+'\n')
        #self.update_menu_widget_list()
        #self.fill_menu_to_order()


    def show_portata(self):
        portata_nome = self.home.list_piatti.findItems(str(self.home.list_piatti.currentItem().text()), QtCore.Qt.MatchExactly)
        self.portata_selected = self.menu.get_portata_from_name(portata_nome[0].text())
        self.home.btn_edit_portata.clicked.connect(lambda: self.edit_portata_view.edit_portata(self.portata_selected))
        self.home.label_id_portata.setText(str(self.portata_selected.get_portata_id()))
        self.home.label_prezzo_portata.setText(str(self.portata_selected.get_prezzo()))
        self.home.label_categoria_portata.setText(self.portata_selected.get_categoria())
        self.home.label_ingredienti_portata.setText(self.portata_selected.stampa_ingredienti_portata())
        #self.home.label_ingredienti_portata.setText(self.stampa_ingredienti_portata(self.portata_selected))
        self.home.btn_delete_piatto.clicked.connect(self.delete_portata)


    ## Questa funzione riempie la tabella delle portate con i dati
    # def fill_menu_to_order(self):
    #      self.row = 0
    #      self.column = 0
    #      for x in range(len(self.menu.get_menu())):
    #          font_nuovo_item = QFont("Dubai", 14, QFont.Medium)
    #          nome_portata = self.menu.get_menu()[x].__str__()
    #          nuovo_item = QTableWidgetItem()
    #          nuovo_item.setText(nome_portata)
    #          nuovo_item.setTextAlignment(Qt.AlignHCenter)
    #          nuovo_item.setFont(font_nuovo_item)
    #          self.home.tableWidget.setItem(self.row, self.column, nuovo_item)
    #          self.column += 1
    #          if self.column % 5 == 0:
    #              self.row += 1
    #              self.column = 0

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
        self.uifunctions.fill_categorie_to_order(self.home, self.categorie_controller.get_lista())

    # def stampa_ingredienti_portata(self, portata):
    #     ingredienti_string = ''
    #     for i in portata.get_ingredienti():
    #         ingredienti_string = ingredienti_string + ' ' + i.get_ingrediente_nome()
    #     return ingredienti_string

    def show_portate_from_categoria(self):
        print("pipo")
        categoria_clicked = self.home.table_categorie_menu.currentItem()
        self.home.list_piatti.clear()
        if categoria_clicked.text() == "Vedi Tutti":
            self.update_menu_widget_list()
            return
        for i in self.menu.get_menu():
            if i.get_categoria() == categoria_clicked.text():
                self.home.list_piatti.addItem(str(i.__str__()))

    def view(self, new_portata_view):
        self.home.Pages_widget.setCurrentWidget(self.home.MenuPage)
        self.home.btn_new_piatto.clicked.connect(new_portata_view.show)
        self.home.list_piatti.itemClicked.connect(self.show_portata)
        self.uifunctions.fill_categorie_to_order(self.home, self.categorie_controller.get_lista())
        self.home.table_categorie_menu.cellClicked.connect(self.show_portate_from_categoria)
