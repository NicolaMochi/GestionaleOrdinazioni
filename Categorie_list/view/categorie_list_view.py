from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QTableWidgetItem, QAbstractItemView

from Menu.view.menu_view import menu_view


class categorie_list_view:
    def __init__(self, lista_categorie, home, menu):
        self.lista_categorie = lista_categorie
        self.home = home
        self.menu = menu
        self.menu_vista = menu_view(self.home, menu, self)

        self.table = ""
        self.menu_to_view = ""


    def fill_categorie_to_order(self):
        ## Determino la tabella di categorie che devo modificare
        if self.home.Pages_widget.currentWidget() == self.home.OrdiniPage: self.table = self.home.table_categorie
        elif self.home.Pages_widget.currentWidget() == self.home.MenuPage: self.table = self.home.table_categorie_menu

        ## Aggiungo tutte le categorie nella tabella corretta
        column = 0
        self.table.clear()
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setColumnCount(len(self.lista_categorie.get_lista())+1)
        for x in range(len(self.lista_categorie.get_lista())+1):
            nuovo_item = QTableWidgetItem()
            if x == 0: nuovo_item.setText("Vedi Tutti")
            else:
                nuovo_item.setText(self.lista_categorie.get_lista()[x-1].get_nome_categoria())
            font_nuovo_item = QFont("Dubai", 14, QFont.Medium)
            nuovo_item.setFont(font_nuovo_item)
            nuovo_item.setTextAlignment(Qt.AlignHCenter)
            self.table.setItem(0, column, nuovo_item)
            column += 1