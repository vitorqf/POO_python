from conta import Conta

class ContaInvestimento(Conta):
    """Construtor da classe conta corrente, recebe todos os valores da classe pai e é adicionado o valor tipo"""
    def __init__(self, numero, titular, tipo, saldo=0, limite=1000):
        super().__init__(numero, titular, saldo, limite)
        self.__tipo = tipo

    """Imprime todas as informações fornecidas pela classe pai e adiciona o tipo de conta ao final"""
    def __str__(self):
        return f"{super().__str__()}\
               \n{'Tipo conta: ':<15}{self.tipo:>15}"

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, other):
        self.__tipo = other
        
    """Recebe o valor retornado pelo método atualiza da classe pai e multiplica por 5"""
    def atualiza(self, taxa):
        return super().atualiza(taxa * 5)

