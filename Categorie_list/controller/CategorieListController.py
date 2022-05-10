from Categorie_list.model.CategorieListModel import CategorieListModel

class CategorieListController:
    def __init__(self):
        self.list_model = CategorieListModel()

#override metodi del model

    def get_categoria_by_index(self, index):
        return self.list_model.lista_categorie(index)

    def delete_categoria(self, categoria):
        # if categoria in self.list_model.lista_categorie:
        #     print("entrato")
            self.list_model.lista_categorie.remove(categoria)

    def add_categoria(self, categoria):
        self.list_model.lista_categorie.append(categoria)

    def get_lista(self):
        return self.list_model.lista_categorie

    def save_categoria_list(self):
        self.list_model.salva_categoria_list()

    def categoria_esiste(self, categoria):
        for x in self.list_model.lista_categorie:
            if x.__str__() == categoria: return True
        return False


    def update_categoria(self, categoria_new, categoria_old, menu):
        count_old = 0
        count_new = 0
        flag = False
        for x in menu:
            if x.get_categoria() == categoria_old: count_old +=1
            if x.get_categoria() == categoria_new: count_new +=1
        if count_new==0:
            flag = True
        if count_old==1 and count_old!=count_new:
            self.delete_categoria(self.get_categoria_from_text(categoria_old))
            print("categoria cancellata")
        return flag


    def get_categoria_from_text(self, nome_categoria):
        categoria = None
        for x in self.list_model.lista_categorie:
            if x.__str__() == nome_categoria:
                categoria = x
        return categoria




