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