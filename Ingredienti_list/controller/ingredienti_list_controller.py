import pickle

from Ingrediente.controller.ingrediente_controller import ingrediente_controller
from Ingrediente.model.ingrediente import ingrediente
from Ingredienti_list.model.ingredienti_list_model import ingredienti_list_model


class ingredienti_list_controller:
    def __init__(self):
        self.lista_ingredienti = ingredienti_list_model()

    def salva_lista_ingredienti(self):
        with open('Ingredienti_list/data/data_lista_ingredienti.pickle', 'wb') as handle:
            pickle.dump(self.lista_ingredienti, handle, pickle.HIGHEST_PROTOCOL)

    def add_to_lista_ingredienti(self, ingrediente):
        self.lista_ingredienti.lista.append(ingrediente)

    def delete_ingrediente(self, ingrediente):
        if ingrediente in self.lista_ingredienti:
            self.lista_ingredienti.lista.remove(ingrediente)

    def get_lista_ingredienti(self):
        return self.lista_ingredienti.lista

    # funzione che prende le parole e ne fa una lista di oggetti ingrediente

    def ingredienti_from_string(self, str_ingredienti):
        lista_ingredienti_scritti = str_ingredienti.split()
        lista_ingredienti_portata = []
        id_ingr = 0
        for i in range(len(lista_ingredienti_scritti)):
            nuovo_ingr = ingrediente_controller(ingrediente(id_ingr, lista_ingredienti_scritti[i]))
            id_ingr += 1
            lista_ingredienti_portata.append(nuovo_ingr)
        return lista_ingredienti_portata

    def add_nuovi_ingredienti(self, lista):
        for x in lista:
            flag = False
            if len(self.lista_ingredienti.lista) == 0: flag = True
            for i in self.lista_ingredienti.lista:
                if x.get_ingrediente_nome() == i.get_ingrediente_nome():
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                id_ingr = len(self.lista_ingredienti.lista)+1
                x.id = id_ingr
                self.lista_ingredienti.lista.append(x)


