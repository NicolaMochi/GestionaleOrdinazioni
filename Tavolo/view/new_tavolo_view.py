from PySide2.QtWidgets import QDialog

from Tavolo.view.gui_add_tavolo import gui_add_tavolo
from Tavolo.controller.ControllerTavolo import ControllerTavolo
from Tavolo.model.Tavolo import Tavolo
from Utilities.utilities import utilities


class new_tavolo_view(QDialog):
    def __init__(self, home, tavoli_controller, tavolo_view):
        super().__init__()
        #super(new_tavolo_view, self).__init__()
        #subclass(parent)
        self.gui = gui_add_tavolo()
        self.gui.setupUi(self)
        self.gui_home = home

        self.lista_tavoli_controller = tavoli_controller
        self.tavoli_widget_view = tavolo_view
        self.lista_tavoli = self.lista_tavoli_controller.get_lista()
        self.utility = utilities(self.lista_tavoli_controller, self.gui_home)

        self.gui.btn_ok_add_tavolo.clicked.connect(self.check_posti_tavolo)
        self.gui.btn_close_dialog.clicked.connect(self.close)

    def check_posti_tavolo(self):
        stringa = self.gui.lineEdit_posti_tavolo.text()
        try:
            posti_tavolo = int(stringa)
            self.add_tavolo_to_list(posti_tavolo)
        except:
            self.gui_home.label_2.setText("font: 9pt 'Poppins'; color: #ff8c00")

    def add_tavolo_to_list(self, posti_tavolo):
        self.close()
        self.gui.lineEdit_posti_tavolo.clear()
        if len(self.lista_tavoli) == 0:
            numero_tavoli = 0
        else: numero_tavoli = len(self.lista_tavoli)
        print(posti_tavolo)
        nuovo_tavolo = ControllerTavolo(Tavolo(numero_tavoli, posti_tavolo))
        self.lista_tavoli.append(nuovo_tavolo)
        self.tavoli_widget_view.add_tavolo_to_widget(nuovo_tavolo)
        self.lista_tavoli_controller.save_tavoli_list()
        self.utility.update_posti()
