class Funcionario:
    """Classe pai responsável pela criação dos funcionários, é a responsável por gerar heranças para as demais"""
    
    def __init__(self, nome, salario, horas_trabalho, senha):
        self.__nome = nome
        self.__salario = salario
        self.__horas_trabalho = horas_trabalho
        self.__senha = senha

    def __str__(self):
        return self.__nome
    

    #### Getters and Setters ####
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value
    
    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, value):
        self.__salario = value
    
    @property
    def horas_trabalho(self):
        return self.__horas_trabalho

    @horas_trabalho.setter
    def horas_trabalho(self, value):
        self.__horas_trabalho = value

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, value):
        self.__senha = value

"""Classe que verifica se a senha fornecida é válida"""
class AutenticavelMixIn:
    def autentica(self, senha_autentica):
        if self.senha == senha_autentica:
            return True

        else:
            return False

"""Classe utilizada para prosseguir com o atendimento ao cliente"""
class AtendimentoMixIn:
    
    """Cadastra um novo atendimento com o cliente"""
    def cadastra_atendimento(self, nome, protocolo):
        self.nome_cliente = nome
        self.protocolo_cliente = protocolo

    """Permite operar um novo atendimento"""
    def atende_cliente(self, operacao_desejada):
        self.operacao_desejada = operacao_desejada

"""Classe utilizada para calcular o total de hora extras"""        
class HoraExtraMixIn:

    def calcula_hora_extra(self, horas):
       hora_extra = horas - self.horas_trabalho
       return f'{hora_extra} horas extras trabalhadas'

"""Classe responsável por autenticar um funcionário diretor"""        
class Diretor(Funcionario,AutenticavelMixIn):

    def autentica(self, senha_autentica):
        if self.senha == senha_autentica:
            return True
        else:
            return False
 
"""Classe responsável por autenticar um funcionário gerente, além de possuir a funcionalidade de calcular horas extras"""
class Gerente(Funcionario,AutenticavelMixIn, HoraExtraMixIn):

    def autentica(self, senha_autentica):
        if self.senha == senha_autentica:
            return True
        else:
            return False
        
"""Classe que gera um cliente autenticavel"""        
class Cliente(AutenticavelMixIn):     
    def autentica(self, senha_autentica):
        if self.senha == senha_autentica:
            return True
        else:
            return False

class TributavelMixIn:
    def get_valor_imposto(self, bem_tributavel):
        if bem_tributavel == 'cc':
            valor_imposto = (bem_tributavel * 0.01) + 50 + (0.05 * bem_tributavel)
            return valor_imposto

        elif bem_tributavel == 'cp':
            return 'Impossivel essa operação com conta poupança'

        else:
            raise ValueError('Operacao invalida!')

"""Classe responsável por fazer o login no sistema, verificando se é um usuário autenticável e retornando um erro caso contrário."""
class SistemaInterno:

    def login(self, obj):
        if (hasattr(obj, 'autentica')):
            obj.autentica(obj.senha)
            return True
        else:
            print(f'{__class__.__name__} não é autenticavel')
            return False
        
diretor = Diretor('João', 3000.0, 8, '1234')
gerente = Gerente('José', 5000.0, 8, '1235')
cliente = Funcionario('Rian', 2000.0, 4, '1245')

sistema = SistemaInterno()
sistema.login(diretor)
sistema.login(gerente)
sistema.login(cliente)
