from Ingrediente.model.ingrediente import ingrediente

class ingrediente_controller:
    def __init__(self, ingrediente):
        self.ingrediente = ingrediente

    def get_ingrediente_id(self):
        return self.ingrediente.id

    def get_ingrediente_nome(self):
        return self.ingrediente.nome