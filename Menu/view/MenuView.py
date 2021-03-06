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
            self.categorie_controller.save_categoria_list()
            self.uifunctions.fill_categorie_to_order(self.home, self.categorie_controller.get_lista())

        self.menu.delete_portata(portata_selected)
        self.menu.salva_menu()


    def update_portata(self):
        self.edit_portata_view.edit_portata(self.portata_selected)


    def show_portata(self, codice_personale):
        portata_nome = self.home.list_piatti.findItems(str(self.home.list_piatti.currentItem().text()), QtCore.Qt.MatchExactly)
        self.portata_selected = self.menu.get_portata_from_name(portata_nome[0].text())
        self.home.label_id_portata.setText(str(self.portata_selected.get_portata_id()))
        self.home.label_prezzo_portata.setText(str(self.portata_selected.get_prezzo()))
        self.home.label_categoria_portata.setText(self.portata_selected.get_categoria())
        self.home.label_ingredienti_portata.setText(self.portata_selected.get_ingredienti())
        #self.home.label_ingredienti_portata.setText(self.stampa_ingredienti_portata(self.portata_selected))
        if(codice_personale):
            self.home.btn_edit_portata.clicked.connect(lambda: self.update_portata())
            self.home.btn_delete_piatto.clicked.connect(self.delete_portata)


    def fill_table_to_order(self):
        self.uifunctions.inizialize_ui_table(self.home.tableWidget, 5, self.menu.get_menu(), True)


    def add_to_menu_widget_list(self, nuova_portata):
        self.home.list_piatti.addItem(str(nuova_portata.__str__()))
        self.uifunctions.fill_categorie_to_order(self.home, self.categorie_controller.get_lista())


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

    def view(self, new_portata_view, codice_personale):
        self.home.Pages_widget.setCurrentWidget(self.home.MenuPage)
        if(codice_personale): self.home.btn_new_piatto.clicked.connect(new_portata_view.show)
        self.home.list_piatti.itemClicked.connect(lambda: self.show_portata(codice_personale))
        self.uifunctions.fill_categorie_to_order(self.home, self.categorie_controller.get_lista())
        self.home.table_categorie_menu.cellClicked.connect(self.show_portate_from_categoria)
