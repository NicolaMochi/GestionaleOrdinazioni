import pickle

class categorie_list_model:
    def __init__(self):
        self.lista_categorie = []

        # importa lista da file pickle
        try:
            with open('Categorie_list/data/data_lista_categorie.pickle', 'rb') as f:
                self.lista_categorie = pickle.load(f)
        except EOFError:
            self.lista_categorie = []

    # esporta lista su file pickle
    def salva_categoria_list(self):
        with open('Categorie_list/data/data_lista_categorie.pickle', 'wb') as handle:
            pickle.dump(self.lista_categorie, handle, pickle.HIGHEST_PROTOCOL)
