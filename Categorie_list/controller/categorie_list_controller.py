from Categorie_list.model.categorie_list_model import categorie_list_model

class categorie_list_controller:
    def __init__(self):
        self.list_model = categorie_list_model()

#override metodi del model

    def get_categoria_by_index(self, index):
        return self.list_model.lista_categorie(index)

    def delete_categoria(self, categoria):
        if categoria in self.list_model.lista_categorie:
            self.list_model.lista_categorie.remove(categoria)

    def add_categoria(self, categoria):
        self.list_model.lista_categorie.append(categoria)

    def get_lista(self):
        return self.list_model.lista_categorie

    def save_categoria_list(self):
        self.list_model.salva_categoria_list()

    def categoria_esiste(self, categoria):
        for x in self.list_model.lista_categorie:
            if x.get_nome_categoria() == categoria: return True
        return False

    def get_categoria_from_text(self, nome_categoria):
        categoria = None
        for x in self.list_model.lista_categorie:
            if x.get_nome_categoria() == nome_categoria:
                categoria = x
        return categoria



