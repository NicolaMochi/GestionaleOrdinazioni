from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QTableWidgetItem, QAbstractItemView


class CategorieListView:
    def __init__(self, home, menu_view, lista_categorie, menu):
        self.home = home
        self.menu_view = menu_view
        self.lista_categorie =  lista_categorie
        self.menu = menu

    def show_categorie_in_table(self):
            clicked = self.home.table_categorie.currentItem()
            if clicked.text() == "Vedi Tutti":
                self.menu_view.fill_table_to_order()
                return

            categoria_selected = self.lista_categorie.get_categoria_from_text(clicked.text())
            nome_categoria = categoria_selected.__str__()
            row = 0
            column = 0
            self.home.tableWidget.clear()

            ## Visualizzo le portate della categoria cliccata sulla tabella
            for x in self.menu.get_menu():
                print(x.get_categoria())
                if x.get_categoria() == nome_categoria:
                    nome_portata = x.__str__()
                    nuovo_item = QTableWidgetItem()
                    nuovo_item.setText(nome_portata)
                    nuovo_item.setTextAlignment(Qt.AlignHCenter)
                    nuovo_item.setFont(QFont("Poppins", 14, QFont.Medium))
                    self.home.tableWidget.setItem(row, column, nuovo_item)
                    column += 1
                    if column % 5 == 0:
                        row += 1
                        column = 0