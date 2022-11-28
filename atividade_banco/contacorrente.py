from conta import Conta

class ContaCorrente(Conta):
    def deposita(self, valor):
        self.__saldo += valor - 0.10

    def atualiza(self, taxa):
        return super().atualiza(taxa * 2)