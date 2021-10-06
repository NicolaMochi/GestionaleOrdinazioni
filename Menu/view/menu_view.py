class menu_view:
    def __init__(self, gui_home, menu):
        self.home = gui_home
        self.menu = menu
        self.portata_selected = None
        self.portata_id = None

    def update_menu_widget_list(self):
        for i in range(len(self.menu.get_menu())):
            self.home.list_piatti.addItem(str(self.menu.get_menu()[i].nome))

    def delete_portata(self):
        self.menu.delete_portata(self.portata_selected)
        portata_deleted = self.home.list_piatti.takeItem(self.portata_id)
        self.home.label_ingredienti_portata.clear()
        self.home.label_id_portata.clear()
        self.home.label_prezzo_portata.clear()
        self.home.label_categoria_portata.clear()

    def show_portata(self):
        self.portata_id = self.home.list_piatti.currentRow()
        self.portata_selected = self.menu.get_portata_from_id(self.portata_id)
        self.home.label_id_portata.setText(str(self.portata_selected.piatto_id))
        self.home.label_prezzo_portata.setText(str(self.portata_selected.prezzo))
        self.home.label_categoria_portata.setText(self.portata_selected.categoria)
        self.home.label_ingredienti_portata.setText(self.stampa_ingredienti_portata(self.portata_selected))
        self.home.btn_delete_piatto.clicked.connect(self.delete_portata)

    def view(self, nuova_portata):
        self.home.Pages_widget.setCurrentWidget(self.home.MenuPage)
        self.home.btn_new_piatto.clicked.connect(nuova_portata.show)
        self.home.list_piatti.itemClicked.connect(self.show_portata)

    ## funzione che prende il controller_menu e fa vedere la lista sul widget
    def add_to_menu_widget_list(self, nuova_portata):
        self.home.list_piatti.addItem(str(nuova_portata.nome))

    def stampa_ingredienti_portata(self, portata):
        ingredienti_string = ''
        for i in range(len(portata.ingredienti)):
            ingredienti_string = ingredienti_string + portata.ingredienti[i].nome
        return ingredienti_string
