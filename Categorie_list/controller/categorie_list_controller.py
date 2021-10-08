from Categorie_list.model.categorie_list_model import categorie_list_model

class categorie_list_controller:
    def __init__(self):
        self.list_model = categorie_list_model()

#override metodi del model

    def get_categoria_by_index(self, index):
        return self.list_model.get_categoria_by_index(index)

    def delete_categoria(self, categoria):
        self.list_model.delete_categoria(categoria)

    def add_categoria(self, categoria):
        self.list_model.add_categoria(categoria)

    def get_lista(self):
        return self.list_model.get_lista()

    def save_categoria_list(self):
        self.list_model.salva_categoria_list()

    def categoria_esiste(self, categoria):
        for x in range(len(self.list_model.get_lista())):
            if self.list_model.get_lista()[x].get_nome_categoria() == categoria: return True
        return False

    def get_categoria_from_text(self, nome_categoria):
        categoria = None
        for x in range(len(self.list_model.get_lista())):
            if self.list_model.get_lista()[x].nome == nome_categoria:
                categoria = self.list_model.get_lista()[x]
        return categoria



