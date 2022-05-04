from PySide2.QtWidgets import QDialog

from Personale.controller.personale_controller import personale_controller
from Personale.model.personale_model import personale_model
from Personale.view.gui_add_personale import gui_add_personale
from Utilities.UIFunctions import UIFunctions


class personale_view_add(QDialog):
    def __init__(self, home, lista_personale):
        super().__init__()
        self.gui = gui_add_personale()
        self.gui_home = home
        self.uifunction = UIFunctions()
        self.credenziali_utente_selected = []
        self.lista_personale_controller = lista_personale
        self.gui.setupUi(self)

    def display_new_personale(self):

        self.gui.lineEdit_nome_personale.clear()
        self.gui.lineEdit_cognome_personale.clear()
        self.gui.checkBox_amministratore.setChecked(False)
        self.gui.btn_confirm_new_personale.clicked.connect(self.add_personale_to_list)
        self.gui.btn_close_new_personale.clicked.connect(self.close)
        self.show()

    def add_personale_to_list(self):
        print("entrato in aggiungi nuovo personale funzione")
        nome = self.gui.lineEdit_nome_personale.text()
        cognome = self.gui.lineEdit_cognome_personale.text()
        password = self.gui.lineEdit_password_personale.text()
        if self.uifunction.check([nome, cognome, password], self.gui_home.label_message_personale): return
        self.close()
        amministratore = self.gui.checkBox_amministratore.isChecked()
        ## Cancello i dati dalla schermata
        self.gui.lineEdit_nome_personale.clear()
        self.gui.lineEdit_cognome_personale.clear()
        self.gui.lineEdit_password_personale.clear()
        self.gui.checkBox_amministratore.setChecked(False)
        ruolo_function = lambda amministratore: "Amministr." if amministratore==1 else "Dipendente"
        ruolo = ruolo_function(amministratore)
        nuovo_personale = personale_controller(personale_model(nome, cognome, password, int(amministratore), ruolo))
        self.lista_personale_controller.add_personale(nuovo_personale)
        self.uifunction.add_to_table(self.gui_home.table_personale, nuovo_personale, False, 6, len(self.lista_personale_controller.get_lista()))
