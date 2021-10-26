from PySide2.QtWidgets import QDialog

from Categorie.model.categoria_model import categoria_model
from Menu.view.gui_add_piatto import gui_add_piatto
from Portata.controller.portataController import portataController
from Portata.model.portata import portata


class new_portata_view(QDialog):
    def __init__(self, menu_vista, menu, lista_ingredienti, lista_categorie):
        super().__init__()
        self.vista_menu = menu_vista
        self.menu_controller = menu
        self.menu_to_update = self.menu_controller.get_menu()
        self.lista_ingredienti_controller = lista_ingredienti
        self.lista_categorie_controller = lista_categorie
        self.codice_categoria = 0

        self.gui = gui_add_piatto()
        self.gui.setupUi(self)

        self.gui.btn_add_to_menu.clicked.connect(self.check_prezzo_portata)

    def ingredienti_are_not_in_list(self, ingrediente):
        if len(self.lista_ingredienti_controller.get_lista_ingredienti()) == 0: return True
        for x in self.lista_ingredienti_controller.get_lista_ingredienti():
            print(self.lista_ingredienti_controller.get_lista_ingredienti()[x].nome)
            print(ingrediente.nome)
            if x.nome != ingrediente.nome:
                return True
            else: return False

    def add_nuovi_ingredienti(self, lista):
        for x in lista:
            flag = False
            if len(self.lista_ingredienti_controller.get_lista_ingredienti()) == 0: flag = True
            for i in self.lista_ingredienti_controller.get_lista_ingredienti():
                if x.nome == i.nome:
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                id_ingr = len(self.lista_ingredienti_controller.get_lista_ingredienti())+1
                x.id = id_ingr
                self.lista_ingredienti_controller.add_to_lista_ingredienti(x)

        #self.lista_ingredienti.SALVALISTASUFILEPICKLE

        print("La lista degli ingredienti aggiornata:")
        for x in range(len(self.lista_ingredienti_controller.get_lista_ingredienti())):
            print(self.lista_ingredienti_controller.get_lista_ingredienti()[x].nome)
        print("\n \n")

    def check_prezzo_portata(self):
        prezzo = self.gui.lineEdit_prezzo.text()
        if not prezzo.isnumeric():
            self.gui.lineEdit_prezzo.setText("Scrivi un numero")
            self.gui.lineEdit_prezzo.setStyleSheet("color:rgb(255, 85, 0); font: 8pt 'Dubai'; border: 2px solid black;border-radius: 5px;background-color:transparent;")
        else: self.aggiungi_portata(prezzo)

    #devo passare alla funzione la lista degli ingredienti già esistenti
    def aggiungi_portata(self, prezzo):
        self.close()
        nome_portata = self.gui.lineEdit_nome_piatto.text()
        categoria = self.gui.lineEdit_categoria.text()
        stringa_ingredienti = self.gui.text_ingredienti.toPlainText()
        self.gui.lineEdit_prezzo.clear()
        self.gui.lineEdit_nome_piatto.clear()
        self.gui.lineEdit_categoria.clear()
        self.gui.text_ingredienti.clear()

        lista_ingredienti = self.lista_ingredienti_controller.get_lista_ingredienti()
        lista_nuovi_ingredienti = self.lista_ingredienti_controller.ingredienti_from_string(stringa_ingredienti, lista_ingredienti)
        self.add_nuovi_ingredienti(lista_nuovi_ingredienti)

        if not self.lista_categorie_controller.categoria_esiste(categoria):
            nuova_categoria = categoria_model(categoria, self.codice_categoria)
            self.codice_categoria += 1
            self.lista_categorie_controller.add_categoria(nuova_categoria)

            # SALVA CATEGORIA NUOVA SU FILE
                # Fai partire la funzione di salvataggio da self.lista_categorie_controller

            #stampo categorie
            for x in range(len(self.lista_categorie_controller.get_lista())):
                print(self.lista_categorie_controller.get_lista()[x].get_nome_categoria())

        id_piatto = len(self.menu_controller.get_menu())
        nuova_portata = portataController(portata(id_piatto, nome_portata, categoria, prezzo, lista_nuovi_ingredienti))
        id_piatto += 1
        self.menu_controller.add_portata(nuova_portata)
        #self.menu.SALVAMENU
        self.vista_menu.add_to_menu_widget_list(nuova_portata)
