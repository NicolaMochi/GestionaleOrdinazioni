from Tavoli_list.model.tavolo_list_model import tavolo_list_model

class tavolo_list_controller:
    def __init__(self):
        self.tavolo_list = tavolo_list_model()

#override metodi del model

    def get_tavolo_by_index(self, index):
        return self.tavolo_list.get_tavolo_by_index(index)

    def delete_tavolo(self, tavolo):
        self.tavolo_list.delete_tavolo(tavolo)

    def add_tavolo(self, tavolo):
        self.tavolo_list.add_tavolo(tavolo)

    def get_lista(self):
        return self.tavolo_list.get_lista()

    def save_tavoli_list(self):
        self.tavolo_list.salva_tavoli_list()

    # aggiungo l'ordine al tavolo corretto
    def add_ordine_from_id(self, id, ordine):
        for x in self.tavolo_list.get_lista():
            if x.codice_tavolo == id:
                x.add_ordine(ordine)

    def total_price_from_id(self, id):
        for x in range(len(self.tavolo_list.get_lista())):
            if self.tavolo_list.get_lista()[x].codice_tavolo == id:
                prezzo = self.tavolo_list.get_lista()[x].total_price()
        return prezzo

