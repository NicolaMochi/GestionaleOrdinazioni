from Categorie.model.categoria_model import categoria_model

class categoria_controller:
    def __init__(self):
        self.categoria = categoria_model()

    def get_nome_categoria(self):
        return self.categoria.get_nome_categoria()

    def get_codice_categoria(self):
        return self.categoria.get_codice_categoria()

