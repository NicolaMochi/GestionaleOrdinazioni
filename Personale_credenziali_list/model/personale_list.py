import json
import os

from Personale.model.personale import personale

class personale_list:
    def __init__(self):
        self.lista_personale = []

        with open('Personale_credenziali_list/data/personale.json') as f:
            lista_credenziali = json.load(f)
        for credenziale in lista_credenziali:
            self.add_credenziale(personale(credenziale["nome"], credenziale["cognome"], credenziale["utente"], credenziale["password"], credenziale["codice"]))

    def add_credenziale(self, personale):
        self.lista_personale.append(personale)