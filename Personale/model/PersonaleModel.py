class PersonaleModel:
    def __init__(self, nome, cognome, password, codicePermessi, ruolo):
        self.nome = nome
        self.cognome = cognome
        self.password = password
        self.codice = codicePermessi ## 1 se il nuovo utente ha i permessi da amministratore
        self.ruolo = ruolo