from PySide2.QtWidgets import QDialog

from Personale.view.gui_add_personale import gui_add_personale


class new_personale_view(QDialog):
    def __init__(self, home, personale_controller):
        super().__init__()
        self.gui = gui_add_personale()
        self.gui.setupUi(self)
        self.gui_home = home

        self.lista_personale_controller = personale_controller