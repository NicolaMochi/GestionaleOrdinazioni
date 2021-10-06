import pickle


class ingredienti_list:
    def __init__(self):
        self.lista_ingredienti = []

        try:
            with open('Ingredienti_list/data/data_lista_ingredienti.pickle', 'rb') as f:
                self.lista_ingredienti = pickle.load(f)
        except EOFError:
            self.lista_tavoli = []

    def salva_ingredienti_list(self):
        with open('Ingredienti_list/data/data_lista_ingredienti.pickle', 'wb') as handle:
            pickle.dump(self.lista_ingredienti, handle, pickle.HIGHEST_PROTOCOL)

    def get_lista(self):
        return self.lista_ingredienti

    def add_to_lista_ingredienti(self, ingrediente):
        self.lista_ingredienti.append(ingrediente)