import pickle

class ordini_list_model:
    def __init__(self):
        self.lista_ordini = []

        # importa lista da file pickle
        try:
            with open('Ordini_list/data/data_lista_ordini.pickle', 'rb') as f:
                self.lista_ordini = pickle.load(f)
        except EOFError:
            self.lista_ordini = []

    # esporta lista su file pickle
    # def salva_ordini_list(self):
    #     with open('Ordini_list/data/data_lista_ordini.pickle', 'wb') as handle:
    #         pickle.dump(self.lista_ordini, handle, pickle.HIGHEST_PROTOCOL)

    def add_ordine(self, tavolo):
        self.lista_ordini.append(tavolo)

    def delete_ordine(self, tavolo):
            if tavolo in self.lista_ordini:
                self.lista_ordini.remove(tavolo)

    def get_ordine_by_index(self, index):
            return self.lista_ordini[index]

    def get_lista_ordini(self):
            return self.lista_ordini