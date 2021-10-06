import pickle


class menu_model:
    def __init__(self):
        self.menu = []

        try:
            with open('Menu/data/menu.pickle', 'rb') as f:
                self.menu = pickle.load(f)
        except EOFError:
            self.menu = []

    # esporta lista su file pickle
    def salva_menu(self):
        with open('Menu/data/menu.pickle', 'wb') as handle:
            pickle.dump(self.menu, handle, pickle.HIGHEST_PROTOCOL)

    def add_portata(self, tavolo):
        self.menu.append(tavolo)

    def delete_portata(self, portata):
            if portata in self.menu:
                self.menu.remove(portata)

    def get_menu(self):
        return self.menu