import pickle

from Menu.model.menu_model import menu_model


class menu_controller:
    def __init__(self):
        self.lista_portate = menu_model()

    def salva_menu(self):
        with open('Menu/data/menu.pickle', 'wb') as handle:
            pickle.dump(self.lista_portate, handle, pickle.HIGHEST_PROTOCOL)

    def add_portata(self, portata):
        self.lista_portate.menu.append(portata)

    def delete_portata(self, portata):
        if portata in self.lista_portate.menu:
            self.lista_portate.menu.remove(portata)

    def get_menu(self):
        return self.lista_portate.menu

    def get_portata_from_id(self, id):
        portata = None
        for x in range(len(self.lista_portate.get_menu())):
            if self.lista_portate.get_menu()[x].piatto_id == id:
                portata = self.lista_portate.get_menu()[x]
        return portata

    def get_portata_from_name(self, nome):
        portata = None
        for x in self.lista_portate.menu:
           if x.__str__() == nome:
                portata = x
        return portata



