import pickle

from Ingrediente.model.ingrediente import ingrediente
from Ingredienti_list.model.ingredienti_list import ingredienti_list


class ingredienti_list_controller:
    def __init__(self):
        self.lista_ingredienti = ingredienti_list()

    def salva_lista_ingredienti(self):
        with open('Ingredienti_list/data/data_lista_ingredienti.pickle', 'wb') as handle:
            pickle.dump(self.lista_ingredienti, handle, pickle.HIGHEST_PROTOCOL)

    def add_to_lista_ingredienti(self, ingrediente):
        self.lista_ingredienti.add_to_lista_ingredienti(ingrediente)

    def delete_ingrediente(self, ingrediente):
        if ingrediente in self.lista_ingredienti:
            self.lista_ingredienti.remove(ingrediente)

    def get_lista_ingredienti(self):
        return self.lista_ingredienti.get_lista()

    # funzione che prende le parole e ne fa una lista di oggetti ingrediente

    def ingredienti_from_string(self, str_ingredienti, lista_ingredienti_presenti):
        lista_ingredienti_scritti = str_ingredienti.split()
        lista_ingredienti_portata = []
        #id_ingr = len(lista_ingredienti_presenti)
        id_ingr = 0
        for i in range(len(lista_ingredienti_scritti)):
            nuovo_ingr = ingrediente(id_ingr, lista_ingredienti_scritti[i])
            id_ingr += 1
            lista_ingredienti_portata.append(nuovo_ingr)
        return lista_ingredienti_portata
