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