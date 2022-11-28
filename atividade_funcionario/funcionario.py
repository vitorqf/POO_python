class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        
    def get_bonificacao(self):
        return self._salario * 0.10   

class ControleDeBonificacoes:

    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes = total_bonificacoes

    def registra(self, obj):
        try:
            self._total_bonificacoes += obj.get_bonificacao()

        except AttributeError as e:
            print(e)    
            
    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes