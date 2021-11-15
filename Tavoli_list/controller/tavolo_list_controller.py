from Tavoli_list.model.tavolo_list_model import tavolo_list_model

class tavolo_list_controller:
    def __init__(self):
        self.tavolo_list = tavolo_list_model()

#override metodi del model

    def get_tavolo_by_index(self, index):
        if index>(len(self.tavolo_list.lista_tavoli)+1): return False
        return self.tavolo_list.lista_tavoli[index]

    def delete_tavolo(self, tavolo):
        if tavolo in self.tavolo_list.lista_tavoli:
            self.tavolo_list.lista_tavoli.remove(tavolo)

    def add_tavolo(self, tavolo):
        self.tavolo_list.lista_tavoli.append(tavolo)

    def get_lista(self):
        return self.tavolo_list.lista_tavoli

    def save_tavoli_list(self):
        self.tavolo_list.salva_tavoli_list()

    # aggiungo l'ordine al tavolo corretto
    def add_ordine_from_id(self, id, ordine):
        for x in self.tavolo_list.lista_tavoli:
            if x.get_codice_tavolo() == id:
                x.add_ordine(ordine)

    def total_price_from_id(self, id):
        prezzo = 0
        for x in self.tavolo_list.lista_tavoli:
            if x.get_codice_tavolo() == id:
                prezzo = x.total_price()
        return prezzo

