from Personale.model.personale_model import personale_model


class personale_controller:
    def __init__(self):
        self.personale = personale_model()

    def get_nome_personale(self):
        return self.personale.get_nome()
    def get_cognome_personale(self):
        return self.personale.get_cognome()
    def get_utente_personale(self):
        return self.personale.get_utente()
    def get_password_personale(self):
        return self.personale.get_password()
    def get_codice_personale(self):
        return self.personale.get_codice()