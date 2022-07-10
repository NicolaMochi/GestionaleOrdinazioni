import pickle

from Menu.model.MenuModel import MenuModel


class MenuController:
    def __init__(self):
        self.lista_portate = MenuModel()

    def salva_menu(self):
        self.lista_portate.salva_menu()

    def add_portata(self, portata):
        self.lista_portate.menu.append(portata)

    def delete_portata(self, portata):
        if portata in self.lista_portate.menu:
            print("entrato")
            self.lista_portate.menu.remove(portata)
        else: print("non entrato")

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

    #Quante portate di questa categoria sono ancora presenti
    def check_categorie_after_delete(self, nome_categoria, menu):
        count = 0
        for x in menu:
           if x.get_categoria() == nome_categoria: count+=1
        print("il count è" + str(count))
        return count

    def substitute_portata(self, id, portata_modificata):
        self.get_menu()[id] = portata_modificata




