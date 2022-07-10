from PySide2 import QtCore
from PySide2.QtWidgets import QDialog

from Categorie.controller.CategoriaController import CategoriaController
from Categorie.model.CategoriaModel import CategoriaModel
from Menu.view.gui_modifica_portata import gui_modifica_portata
from Utilities.UIFunctions import UIFunctions


class EditPortataView(QDialog):
    def __init__(self , categorie_controller, home, menu):
        super().__init__()
        self.menu = menu
        self.categorie_list_controller = categorie_controller
        self.home = home
        # self.portata_selected = None
        self.gui = gui_modifica_portata()
        self.gui.setupUi(self)


    def edit_portata(self, portata_selected):
        try:
            portata_nome = self.home.list_piatti.findItems(str(self.home.list_piatti.currentItem().text()),
                                                           QtCore.Qt.MatchExactly)
        except:
            print("Non hai selezionato nessuna categoria")
            #SCRIVILO NEL DESIGN
            return
        self.categoria_before = portata_selected.get_categoria()
        self.show()
        self.gui.lineEdit_nome_piatto.setText(portata_selected.__str__())
        self.gui.lineEdit_categoria.setText(portata_selected.get_categoria())
        self.gui.lineEdit_prezzo.setText(str(portata_selected.get_prezzo()))
        self.gui.plainTextEdit.setPlainText(portata_selected.get_ingredienti())
        self.gui.btn_modifica_portata.clicked.connect(lambda :self.portata_modificata(portata_selected))


    def portata_modificata(self, portata_selected):
        portata_item = self.home.list_piatti.findItems(str(self.home.list_piatti.currentItem().text()), QtCore.Qt.MatchExactly)
        print(portata_item[0].text())
        nome_portata = self.gui.lineEdit_nome_piatto.text()
        categoria_portata = self.gui.lineEdit_categoria.text()
        prezzo_portata = self.gui.lineEdit_prezzo.text()
        ingredienti_portata = self.gui.plainTextEdit.toPlainText()

        if nome_portata != "" and categoria_portata != "":
            self.gui.label_message.setText("Compila tutti i campi")

            if not UIFunctions().check_prezzo_portata(self.gui, prezzo_portata):

                if portata_selected.__str__() != nome_portata:
                    portata_selected.set_nome(nome_portata)
                    portata_item[0].setText(nome_portata)
                    self.home.label_id_portata.setText(str(nome_portata))


                aggiunta = self.categorie_list_controller.update_categoria(categoria_portata, self.categoria_before, self.menu.get_menu())
                if aggiunta:
                    self.categorie_list_controller.add_categoria(CategoriaController(CategoriaModel(categoria_portata, len(self.categorie_list_controller.get_lista()))))
                portata_selected.set_categoria(categoria_portata)
                self.home.label_categoria_portata.setText(str(categoria_portata))

                if portata_selected.get_prezzo != prezzo_portata:
                    portata_selected.set_prezzo(prezzo_portata)
                    self.home.label_prezzo_portata.setText(str(prezzo_portata))

                if portata_selected.get_ingredienti != ingredienti_portata:
                    portata_selected.set_ingredienti(ingredienti_portata)
                    self.home.label_ingredienti_portata.setText(str(ingredienti_portata))

                self.close()
                UIFunctions().fill_categorie_to_order(self.home, self.categorie_list_controller.get_lista())
                self.menu.substitute_portata(portata_selected.get_portata_id(), portata_selected)
                self.menu.salva_menu()