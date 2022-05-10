class CategoriaController:
    def __init__(self, categoria):
        self.categoria = categoria

    def __str__(self):
        return self.categoria.nome

    def get_codice_categoria(self):
        return self.categoria.codice


