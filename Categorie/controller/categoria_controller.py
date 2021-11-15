from Categorie.model.categoria_model import categoria_model

class categoria_controller:
    def __init__(self, categoria):
        self.categoria = categoria

    def get_nome_categoria(self):
        return self.categoria.nome

    def get_codice_categoria(self):
        return self.categoria.codice

