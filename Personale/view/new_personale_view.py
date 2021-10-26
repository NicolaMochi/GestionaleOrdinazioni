from PySide2.QtWidgets import QDialog

from Personale.model.personale_model import personale_model
from Personale.view.gui_add_personale import gui_add_personale


class new_personale_view(QDialog):
    def __init__(self, home, lista_personale):
        super().__init__()
        self.gui = gui_add_personale()
        self.gui.setupUi(self)
        self.gui_home = home

        self.lista_personale_controller = lista_personale
        self.gui.btn_confirm_new_personale.clicked.connect(self.add_personale_to_list)

    def add_personale_to_list(self):
        self.close()
        nome = self.gui.lineEdit_nome_personale.text()
        cognome = self.gui.lineEdit_cognome_personale.text()
        password = self.gui.lineEdit_password_personale.text()
        amministratore = self.gui.checkBox_amministratore.isChecked()
        ## amministratore è 1 se il nuovo utente ha i permessi da amministratore

        nuovo_personale = personale_model(nome, cognome, password, int(amministratore))
        print(nome)
        print(cognome)
        print(password)
        print(int(amministratore))

        self.lista_personale_controller.add_personale(nuovo_personale)

