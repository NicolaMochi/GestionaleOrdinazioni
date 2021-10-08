from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QDialog, QTableWidgetItem

from Tavoli_list.controller.tavolo_list_controller import tavolo_list_controller
from Tavoli_list.view.gui_add_tavolo import gui_add_tavolo
from Tavoli_list.view.tavolo_list_view import tavolo_list_view
from Tavolo.model.tavolo import tavolo

class new_tavolo_view(QDialog):
    def __init__(self, home, tavoli_controller, tavolo_view):
        super().__init__()
        #super(new_tavolo_view, self).__init__()
        #subclass(parent)
        self.gui = gui_add_tavolo()
        self.gui.setupUi(self)
        self.gui_home = home

        self.lista_tavoli_controller = tavoli_controller
        self.lista_tavoli = self.lista_tavoli_controller.get_lista()
        self.gui.btn_ok_add_tavolo.clicked.connect(self.check_posti_tavolo)
        self.gui.btn_close_dialog.clicked.connect(self.close)

        self.tavoli_widget_view = tavolo_view


    def check_posti_tavolo(self):
        stringa = self.gui.btn_ok_add_tavolo.text()
        if isinstance(stringa, int):
            self.add_tavolo_to_list()
        else: self.gui.label.setText("Devi scrivere un numero intero")

    def add_tavolo_to_list(self):
        self.close()
        if len(self.lista_tavoli) == 0:
            numero_tavoli = 0
        else: numero_tavoli = len(self.lista_tavoli)
        posti_tavolo = self.gui.lineEdit_posti_tavolo.text()
        nuovo_tavolo = tavolo(numero_tavoli, posti_tavolo)
        self.lista_tavoli.append(nuovo_tavolo)
        self.tavoli_widget_view.add_tavolo_to_widget(numero_tavoli+1)
        self.lista_tavoli_controller.save_tavoli_list()