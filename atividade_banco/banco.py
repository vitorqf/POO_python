class Banco:
    __lista_contas = []

    def __init__(self, numero, nome):
        self.__numero = numero
        self.__nome = nome
    
    def adiciona(self, Conta):
        self.__lista_contas.append(Conta)

    def pegaConta(self, index):
        return self.__lista_contas[index]

    def pegaTotalDeContas(self):
        return len(self.__lista_contas)

    @property
    def lista_contas(self):
        return self.__lista_contas

    @property
    def numero(self):
        return self.__numero
    
    @property
    def nome(self):
        return self.__nome

    @numero.setter
    def numero(self, other):
        self.__numero = other
    
    @nome.setter
    def nome(self, other):
        self.__nome = other