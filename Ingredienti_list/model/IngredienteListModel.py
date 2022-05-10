import pickle


class IngredienteListModel:
    def __init__(self):
        self.lista = []

        try:
            with open('Ingredienti_list/data/data_lista_ingredienti.pickle', 'rb') as f:
                self.lista = pickle.load(f)
        except EOFError:
            self.lista = []

    def salva_ingredienti_list(self):
        with open('Ingredienti_list/data/data_lista_ingredienti.pickle', 'wb') as handle:
            pickle.dump(self.lista, handle, pickle.HIGHEST_PROTOCOL)