from PySide2.QtWidgets import QDialog

from Personale.controller.PersonaleController import PersonaleController
from Personale.model.PersonaleModel import PersonaleModel
from Personale.view.gui_add_personale import gui_add_personale
from Personale.view.gui_modifica_personale import gui_modifica_personale
from Utilities.UIFunctions import UIFunctions


class PersonaleView(QDialog):
    def __init__(self, home, lista_personale):
        super().__init__()
        self.gui = gui_add_personale()
        self.gui_modifica = gui_modifica_personale()
        self.gui_home = home
        self.uifunction = UIFunctions()
        self.credenziali_utente_selected = []
        self.lista_personale_controller = lista_personale

    def display_new_personale(self):
        self.gui.setupUi(self)
        self.gui.lineEdit_nome_personale.clear()
        self.gui.lineEdit_cognome_personale.clear()
        self.gui.checkBox_amministratore.setChecked(False)
        self.gui.btn_confirm_new_personale.clicked.connect(self.add_personale_to_list)
        self.gui.btn_close_new_personale.clicked.connect(self.close)
        self.open()

    def display_edit_item(self):
        self.gui_modifica.setupUi(self)
        self.credenziali_utente_selected = self.gui_home.table_personale.currentItem().text().split('\n', )
        self.gui_modifica.lineEdit_nome_personale.setText(self.credenziali_utente_selected[0])
        self.gui_modifica.lineEdit_cognome_personale.setText(self.credenziali_utente_selected[1])
        if self.credenziali_utente_selected[3] == "Amministr.": self.gui_modifica.checkBox_amministratore.setChecked(True)
        self.gui_modifica.btn_confirm_new_personale.clicked.connect(self.modify_user)
        self.gui_modifica.btn_elimina_personale.clicked.connect(self.delete_user)
        self.gui_modifica.btn_close_new_personale.clicked.connect(self.close)
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
        nuovo_personale = PersonaleController(PersonaleModel(nome, cognome, password, int(amministratore), ruolo))
        self.lista_personale_controller.add_personale(nuovo_personale)
        self.uifunction.add_to_table(self.gui_home.table_personale, nuovo_personale, False, 6, len(self.lista_personale_controller.get_lista()))

    def modify_user(self):
        print("pipo modify user entrato")
        self.close()
        user = self.lista_personale_controller.find_user(self.credenziali_utente_selected)
        nome = self.gui_modifica.lineEdit_nome_personale.text()
        cognome = self.gui_modifica.lineEdit_cognome_personale.text()
        password = self.gui_modifica.lineEdit_password_personale.displayText()
        self.gui_modifica.lineEdit_password_personale.clear()
        amministratore = self.gui_modifica.checkBox_amministratore.isChecked()
        new_credenziali_utente_selected = [nome, cognome, password, amministratore]
        self.lista_personale_controller.modifica_utente(user, new_credenziali_utente_selected)
        self.uifunction.inizialize_ui_table(self.gui_home.table_personale, 6, self.lista_personale_controller.get_lista(), True)

    def delete_user(self):
        user = self.lista_personale_controller.find_user(self.credenziali_utente_selected)
        self.lista_personale_controller.remove_personale(user)
        self.close()
        self.uifunction.inizialize_ui_table(self.gui_home.table_personale, 6, self.lista_personale_controller.get_lista(), True)
