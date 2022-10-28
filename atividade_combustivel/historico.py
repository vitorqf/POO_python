import datetime

class Historico:
    def __init__(self, nomePosto):
        if (nomePosto):
            self.data_abertura = datetime.datetime.today()
            self.transacoes = []

        else:
            return None

    def imprime(self):
        print("\n\n***** HISTORICO *****\n\nData abertura: {}".format(self.data_abertura))
        print("Transações: ")
        for t in self.transacoes:
            print("-", t)  