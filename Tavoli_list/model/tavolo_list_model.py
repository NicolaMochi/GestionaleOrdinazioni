import pickle

class tavolo_list_model:
    def __init__(self):
        self.lista_tavoli = []

        # importa lista da file pickle
        try:
            with open('Tavoli_list/data/data_lista_tavoli.pickle', 'rb') as f:
                self.lista_tavoli = pickle.load(f)
        except EOFError:
            self.lista_tavoli = []

    # esporta lista su file pickle
    def salva_tavoli_list(self):
        with open('Tavoli_list/data/data_lista_tavoli.pickle', 'wb') as handle:
            pickle.dump(self.lista_tavoli, handle, pickle.HIGHEST_PROTOCOL)
