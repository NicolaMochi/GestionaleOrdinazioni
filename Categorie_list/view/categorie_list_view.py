### SE ALLA FINE NON E' SERVITA ANCORA A NIENTE
# DELETE


from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QTableWidgetItem, QAbstractItemView


class categorie_list_view:
    # def __init__(self):
        # self.lista_categorie = lista_categorie
        # self.home = home
        # self.menu = menu
        # #self.menu_vista = menu_view(self.home, menu, self, self)
        #
        # self.table = ""
        # self.menu_to_view = ""
#
#
#     # def fill_categorie_to_order(self):
#     #     ## Determino la tabella di categorie che devo modificare
#     #     if self.home.Pages_widget.currentWidget() == self.home.OrdiniPage: self.table = self.home.table_categorie
#     #     elif self.home.Pages_widget.currentWidget() == self.home.MenuPage: self.table = self.home.table_categorie_menu
#     #
#     #     ## Aggiungo tutte le categorie nella tabella corretta
#     #     column = 0
#     #     self.table.clear()
#     #     self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
#     #     self.table.setColumnCount(len(self.lista_categorie.get_lista())+1)
#     #     for x in range(len(self.lista_categorie.get_lista())+1):
#     #         nuovo_item = QTableWidgetItem()
#     #         if x == 0: nuovo_item.setText("Vedi Tutti")
#     #         else:
#     #             nuovo_item.setText(self.lista_categorie.get_lista()[x-1].get_nome_categoria())
#     #         font_nuovo_item = QFont("Dubai", 14, QFont.Medium)
#     #         nuovo_item.setFont(font_nuovo_item)
#     #         nuovo_item.setTextAlignment(Qt.AlignHCenter)
#     #         self.table.setItem(0, column, nuovo_item)
#     #         column += 1


    def show_categorie_in_table(self, home, menu_view, lista_categorie, menu):
            clicked = home.table_categorie.currentItem()
            if clicked.text() == "Vedi Tutti":
                menu_view.fill_table_to_order()
                return

            categoria_selected = lista_categorie.get_categoria_from_text(clicked.text())
            nome_categoria = categoria_selected.get_nome_categoria()
            row = 0
            column = 0
            home.tableWidget.clear()

            ## Visualizzo le portate della categoria cliccata sulla tabella
            for x in menu.get_menu():
                print(x.get_categoria())
                if x.get_categoria() == nome_categoria:
                    nome_portata = x.__str__()
                    nuovo_item = QTableWidgetItem()
                    nuovo_item.setText(nome_portata)
                    nuovo_item.setTextAlignment(Qt.AlignHCenter)
                    nuovo_item.setFont(QFont("Poppins", 14, QFont.Medium))
                    home.tableWidget.setItem(row, column, nuovo_item)
                    column += 1
                    if column % 5 == 0:
                        row += 1
                        column = 0