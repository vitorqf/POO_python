from datetime import datetime

class Pessoa:
    def __init__(self, nome, sexo, data_nasc):
        self.__nome = nome
        self.__sexo = sexo
        self.__data_nasc = data_nasc

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, other):
        self.__nome = other
        
    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, other):
        self.__sexo = other

    @property
    def data_nasc(self):
        return self.__data_nasc

    @data_nasc.setter
    def data_nasc(self, other):
        self.__data_nasc = other

class Ator(Pessoa):
    class Contrato:
        def __init__(self,inicio, fim, salario):
            self.__inicio = inicio
            self.__fim = fim
            self.__salario = salario

        @property
        def inicio(self):
            return self.__inicio

        @inicio.setter
        def inicio(self, other):
            self.__inicio = other

        @property
        def fim(self):
            return self.__fim

        @fim.setter
        def fim(self, other):
            self.__fim = other

        @property
        def salario(self):
            return self.__salario

        @salario.setter
        def salario(self, other):
            self.__salario = other

    def __init__(self, inicio, fim, salario, nome, sexo, data_nasc):
        super().__init__(nome, sexo, data_nasc)
        self.__contrato = self.Contrato(inicio, fim, salario)

    @property
    def contrato(self):
        return self.__contrato

    @contrato.setter
    def contrato(self, other: Contrato):
        self.__contrato = other

class Personagem(Ator):
    def __init__(self, caracterizacao, novela, inicio, fim, salario, nome, sexo, data_nasc):
        super().__init__(inicio, fim, salario, nome, sexo, data_nasc)
        self.__caracterizacao = caracterizacao
        self.__novela = novela

    @property
    def caracterizacao(self):
        return self.__caracterizacao

    @caracterizacao.setter
    def caracterizacao(self, other):
        self.__caracterizacao = other

    @property
    def novela(self):
        return self.__novela

    @novela.setter
    def novela(self, other):
        self.__novela = other
    

class Aluno(Pessoa):
    def __init__(self, matric, nome, sexo, data_nasc):
        super().__init__(nome, sexo, data_nasc)
        self.__matric = matric

    @property
    def matric(self):
        return self.__matric

    @matric.setter
    def matric(self, other):
        self.__matric = other


inicio = datetime(2020, 5, 17)
fim = datetime(2023, 1, 1)
salario = 6000

ator = Ator(inicio, fim, salario, 'Antonio', 'm', datetime(1978, 1, 1))
aluno = Aluno(20221094040023, 'Vitor', 'm', datetime(2002, 3, 20))
personagem = Personagem('Duble', 'Caminho das Indias', inicio, fim, salario, 'Marilia', 'f', datetime(1988, 3, 1))

print(ator.nome)
print(ator.contrato.fim)
print('')

print(aluno.nome)
print(aluno.matric)
print('')

print(personagem.nome)
print(personagem.caracterizacao)
print(personagem.novela)
