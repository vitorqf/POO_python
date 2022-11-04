import datetime


class Jogador:
    def __init__(self, nome, posicao, nascimento, nacionalidade, altura, peso):
        self.__nome = nome
        self.__posicao = posicao
        self.__nascimento = nascimento  # dd/mm/yyyy
        self.__nacionalidade = nacionalidade
        self.__altura = altura  # cm
        self.__peso = peso  # kg
        self.__idade = (datetime.date.today().year) - \
            (int(self.__nascimento.split('/')[2]))

    def checarIdade(self):
        if ((self.__posicao == 'Atacante') or
            (self.__posicao.lower() == 'atacante') or
                ((self.__posicao.upper() == 'ATACANTE'))):

            if (self.__idade == 35):
                print("O jogador ja esta na media de aposentadoria para a sua posicao.")
            else:
                print("Faltando para chegar na media de aposentadoria: {} anos".format(
                    35 - self.__idade))

        elif ((self.__posicao == 'Meio-campo') or
              (self.__posicao.lower() == 'meio-campo') or
              ((self.__posicao.upper() == 'MEIO-CAMPO'))):

            if (self.__idade == 38):
                print("O jogador ja esta na media de aposentadoria para a sua posicao.")
            else:
                print("Faltando para chegar na media de aposentadoria: {} anos".format(
                    38 - self.__idade))

        elif ((self.__posicao == 'Defesa') or
              (self.__posicao.lower() == 'defesa') or
              ((self.__posicao.upper() == 'DEFESA'))):

            if (self.__idade == 40):
                print("O jogador ja esta na media de aposentadoria para a sua posicao.")
            else:
                print("Faltando para chegar na media de aposentadoria: {} anos".format(
                    40 - self.__idade))

        else:
            print("Posicao '{}' nao reconhecida.".format(self.__posicao))
            return False

    def imprime(self):
        print(
            "\n=-=-= Dados do Jogador =-=-=\n \
            \nNOME: {} \
            \nPOSICAO: {} \
            \nNASCIMENTO: {} \
            \nNACIONALIDADE: {} \
            \nALTURA: {} cm \
            \nPESO: {} kg \
            \nIDADE: {} anos\n \
            \n=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
            .format(
                self.__nome,
                self.__posicao,
                self.__nascimento,
                self.__nacionalidade,
                self.__altura,
                self.__peso,
                self.__idade
            )
        )

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getPeso(self):
        return self.__peso

    def setPeso(self, peso):
        self.__peso = peso

    def getPosicao(self):
        return self.__posicao

    def setPosicao(self, posicao):
        self.__posicao = posicao

    def getNascimento(self):
        return self.__nascimento

    def setNascimento(self, nascimento):
        self.__nascimento = nascimento

    def getNacionalidade(self):
        return self.__nacionalidade

    def setNacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    def getAltura(self):
        return self.__altura

    def setAltura(self, altura):
        self.__altura = altura


j1 = Jogador("Augusto", "ATacante", "10/02/1995", "Brasileiro", 189, 82)
j1.imprime()
j1.checarIdade()
