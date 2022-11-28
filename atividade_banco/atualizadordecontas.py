class AtualizadorDeContas:
    def __init__(self, selic, saldo_total=0):
        self.__selic = selic
        self.__saldo_total = saldo_total

    def exec(self, conta):
        try:
            print(f"\nSaldo da Conta: {conta.saldo}")
            self.__saldo_total += conta.atualiza(self.__selic)
            print(f"Saldo Final: {self.__saldo_total}")

        except AttributeError as e: 
            print(e)

    @property
    def selic(self):
        return self.__selic

    @property
    def saldo_total(self):
        return self.__saldo_total

    @selic.setter
    def numero(self, other):
        self.selic = other

    @saldo_total.setter
    def numero(self, other):
        self.saldo_total = other