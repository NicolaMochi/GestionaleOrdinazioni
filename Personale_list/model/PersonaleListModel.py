import pickle

class PersonaleListModel:
    def __init__(self):
        self.lista_personale = []

        try:
            with open('Personale_list/data/personale.pickle', 'rb') as f:
                self.lista_personale = pickle.load(f)
        except EOFError:
            self.lista_personale = []

    ## Manca il salvataggio
    def add_credenziale(self, personale):
        self.lista_personale.append(personale)

    def salva_personale_list(self):
        with open('Personale_list/data/personale.pickle', 'wb') as handle:
            pickle.dump(self.lista_personale, handle, pickle.HIGHEST_PROTOCOL)