
class personale_controller:
    def __init__(self, personale):
        self.personale = personale

    def __str__(self):
        return self.personale.nome+'\n'+self.personale.cognome+'\n\n'+self.personale.ruolo

    def get_nome_personale(self):
        return self.personale.nome
    def get_cognome_personale(self):
        return self.personale.cognome
    def get_password_personale(self):
        return self.personale.password
    def get_codice_personale(self):
        return self.personale.codice
    def get_ruolo_personale(self):
        return self.personale.ruolo

    def set_nome_personale(self, nome):
        self.personale.nome = nome
    def set_cognome_personale(self, cognome):
        self.personale.cognome = cognome
    def set_password_personale(self, password):
        self.personale.password = password
    def set_codice_personale(self, codice):
        self.personale.codice = int(codice)
    def set_ruolo_personale(self, ruolo):
        self.personale.ruolo = ruolo
