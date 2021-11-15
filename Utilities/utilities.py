class utilities:
    def __init__(self, home, tavoli_list):
        self.home = home
        self.tavoli_list = tavoli_list.get_lista()
        self.posti_totali = 0
        self.posti_rimanenti = 0

    # def posti(self):
    #     for x in range(len(self.tavoli_list)):
    #         self.posti_totali += int(self.tavoli_list[x].get_posti_tavolo())
    #         self.home.label_posti.setText(str(self.posti_rimanenti) + '/' + str(self.posti_totali))

    def posti_rimanenti(self):
        for x in self.tavoli_list:
            if len(x.get_lista_ordini_tavolo()) != 0:
                print("posti del tavolo con l'ordine:" + str(x.get_posti_tavolo()))
                self.posti_rimanenti = self.posti_totali - int(x.get_posti_tavolo())
        self.home.label_posti.setText(str(self.posti_rimanenti)+'/'+str(self.posti_totali))

