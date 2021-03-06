from PySide2.QtWidgets import QDialog

from Categorie.controller.CategoriaController import CategoriaController
from Categorie.model.CategoriaModel import CategoriaModel
from Menu.view.gui_add_piatto import gui_add_piatto
from Portata.controller.PortataController import PortataController
from Portata.model.PortataModel import PortataModel
from Utilities.UIFunctions import UIFunctions


class NewPortataView(QDialog):
    def __init__(self, menu_vista, menu, lista_categorie):
        super().__init__()
        self.vista_menu = menu_vista
        self.menu_controller = menu
        self.menu_to_update = self.menu_controller.get_menu()
        self.lista_categorie_controller = lista_categorie
        self.codice_categoria = 0
        self.gui = gui_add_piatto()
        self.gui.setupUi(self)

        self.gui.btn_add_to_menu.clicked.connect(self.check_inserimento)


    def check_inserimento(self):
        nome_portata = self.gui.lineEdit_nome_piatto.text()
        if self.gui.lineEdit_categoria.text() == "" or nome_portata == "":
            self.gui.label_message.setText("Compila tutti i campi")
            return
        flag = True
        for x in self.menu_to_update:
            if x.__str__() == nome_portata:
                self.gui.label_message.setText("Nome non disponibile")
                flag = False
        if flag: self.aggiungi_portata()
        else: return


    #devo passare alla funzione la lista degli ingredienti già esistenti
    def aggiungi_portata(self):
        prezzo = self.gui.lineEdit_prezzo.text()
        if UIFunctions().check_prezzo_portata(self.gui, prezzo): return
        self.close()
        nome_portata = self.gui.lineEdit_nome_piatto.text()
        categoria = self.gui.lineEdit_categoria.text()
        stringa_ingredienti = self.gui.text_ingredienti.toPlainText()
        self.gui.lineEdit_prezzo.clear()
        self.gui.lineEdit_nome_piatto.clear()
        self.gui.lineEdit_categoria.clear()
        self.gui.text_ingredienti.clear()

        if not self.lista_categorie_controller.categoria_esiste(categoria):
            nuova_categoria = CategoriaController(CategoriaModel(categoria, self.codice_categoria))
            self.codice_categoria += 1
            self.lista_categorie_controller.add_categoria(nuova_categoria)
            self.lista_categorie_controller.save_categoria_list()

        id_piatto = len(self.menu_controller.get_menu())
        nuova_portata = PortataController(PortataModel(id_piatto, nome_portata, categoria, prezzo, stringa_ingredienti))
        id_piatto += 1
        self.menu_controller.add_portata(nuova_portata)

        self.menu_controller.salva_menu()
        self.vista_menu.add_to_menu_widget_list(nuova_portata)
