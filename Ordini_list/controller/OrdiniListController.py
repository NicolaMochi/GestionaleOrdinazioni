from Ordini_list.model.OrdiniListModel import OrdiniListModel

class OrdiniListController:
    def __init__(self):
        self.list_model = OrdiniListModel()

    def get_ordine_by_index(self, index):
        return self.list_model.get_ordine_by_index(index)

    def delete_ordine(self, tavolo):
        self.list_model.delete_ordine(tavolo)

    def add_ordine(self, ordine):
        self.list_model.add_ordine(ordine)

    def get_lista_ordini(self):
        return self.list_model.get_lista_ordini()

    def save_ordini_list(self):
        self.list_model.salva_ordini_list()