from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QTableWidgetItem, QTableWidget, QAbstractItemView


class personale_list_view:
    def __init__(self, home, personale_controller, add_personale_view):
        self.row = 0
        self.column = 0
        self.home = home
        self.personale_controller = personale_controller.lista.lista_personale
        self.nuovo_item = None
        self.add_personale_view = add_personale_view

    def view(self, flag):
        self.home.Pages_widget.setCurrentWidget(self.home.PersonalePage)
        #self.fill_table_personale(flag)
        self.home.add_nuovo_personale.clicked.connect(self.add_personale_view.show)
