from datetime import date


class CartaoMensagem: 
    listaMsg = []

    def __init__(self, nome, remetente, data = date.today().strftime("%d/%m/%Y")):
        self.nome = nome
        self.data = data
        self.remetente = remetente
        self.listaMsg.append(self)

    def printMsgs(self):
        for msg in self.listaMsg:
            print(f"{msg}\n{'':-^80}\n")

    def set_nome(self, info):
        self.nome = info

    def set_nome(self, info):
        self.data = info
        
    def set_remetente(self, info):
        self.remetente = info

    def get_remetente(self):
        return self.remetente

    def get_data(self):
        return self.data

    def get_nome(self):
        return self.nome