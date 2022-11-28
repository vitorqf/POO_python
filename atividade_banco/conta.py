class Conta:

    def __init__(self, numero, titular, saldo=0, limite=1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def atualiza(self, taxa):
        self.__saldo += self.__saldo * taxa
        return self.__saldo

    def __str__(self):
        return f"\
               \n{' DADOS DA CONTA ':=^30}\
               \n{'Numero: ':<15}{self.numero:>15}\
               \n{'Titular: ':<15}{self.titular:>15}\
               \n{'Saldo: ':<15}{self.saldo:>15}\
               \n{'Limite: ':<15}{self.limite:>15}\
               "


    # Getters n Setters {

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @numero.setter
    def numero(self, other):
        self.__numero = other

    @titular.setter
    def titular(self, other):
        self.__titular = other

    @saldo.setter
    def saldo(self, other):
        self.__saldo = other

    @limite.setter
    def limite(self, other):
        self.__limite = other

    # } Getters n Setters