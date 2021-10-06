from Tavoli_list.model.tavolo_list_model import tavolo_list_model

class tavolo_list_controller:
    def __init__(self):
        self.list_model = tavolo_list_model()

#override metodi del model

    def get_tavolo_by_index(self, index):
        return self.list_model.get_tavolo_by_index(index)

    def delete_tavolo(self, tavolo):
        self.list_model.delete_tavolo(tavolo)

    def add_tavolo(self, tavolo):
        self.list_model.add_tavolo(tavolo)

    def get_lista(self):
        return self.list_model.get_lista()

    def save_tavoli_list(self):
        self.list_model.salva_tavoli_list()

    # add ordine a tavolo from id
    def add_ordine_from_id(self, id, ordine):
        for x in range(len(self.list_model.get_lista())):
            if self.list_model.get_lista()[x].codice_tavolo == id:
                self.list_model.get_lista()[x].add_ordine(ordine)

    def total_price_from_id(self, id):
        for x in range(len(self.list_model.get_lista())):
            if self.list_model.get_lista()[x].codice_tavolo == id:
                prezzo = self.list_model.get_lista()[x].total_price()
        return prezzo

