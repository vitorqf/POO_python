import datetime


class Jogador:
    def __init__(self, nome, posicao, nascimento, nacionalidade, altura, peso):
        self.__nome = nome.upper()
        self.__posicao = posicao.upper()
        self.__nascimento = nascimento  # dd/mm/yyyy
        self.__nacionalidade = nacionalidade.upper()
        self.__altura = altura  # cm
        self.__peso = peso  # kg
        self.__idade = (datetime.date.today().year) -  (int(self.__nascimento.split('/')[2]))

    def checarIdade(self):
        if ((self.__posicao == 'Atacante') or
            (self.__posicao.lower() == 'atacante')):

            if (self.__idade == 35):
                print("O jogador ja esta na media de aposentadoria para a sua posicao.")

            else:
                print("Faltando para chegar na media de aposentadoria: {} anos".format(35 - self.__idade))

        elif ((self.__posicao == 'Meio-campo') or
              (self.__posicao.lower() == 'meio-campo')):

            if (self.__idade == 38):
                print("O jogador ja esta na media de aposentadoria para a sua posicao.")

            else:
                print("Faltando para chegar na media de aposentadoria: {} anos".format(38 - self.__idade))

        elif ((self.__posicao == 'Defesa') or
              (self.__posicao.lower() == 'defesa')):

            if (self.__idade == 40):
                print("\nO jogador ja esta na media de aposentadoria para a sua posicao.")

            else:
                print("\nFaltando para chegar na media de aposentadoria: {} anos".format(40 - self.__idade))

        else:
            print("Posicao '{}' nao reconhecida.".format(self.__posicao))
            return False

    def imprime(self):
        print(
            "\n=-=-= Dados do Jogador =-=-=\n \
            \nNome: {} \
            \nPosicao: {} \
            \nNascimento: {} \
            \nNacionalidade: {} \
            \nAltura: {} cm \
            \nPeso: {} kg \
            \nIdade: {} anos\n \
            \n=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"
            .format(
                self.__nome.upper(),
                self.__posicao.upper(),
                self.__nascimento,
                self.__nacionalidade.upper(),
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


j1 = Jogador("Augusto", "ATacAnTe", "10/02/1995", "Brasileiro", 189, 82)

print("O que deseja realizar?\
        \n1 - Ver dados do jogador\
        \n2 - Verificar aposentadoria\
        \n3 - Alterar dados\
        \n4 - Sair")

while True:
    
    choice = int(input("\n=> "))

    match choice:

        case 1:
            j1.imprime()
        
        case 2:
            j1.checarIdade()

        case 3:

            print("\nQual dado deseja alterar?\
                \n1 - Nome\
                \n2 - Posicao\
                \n3 - Nascimento\
                \n4 - Nacionalidade\
                \n5 - Altura\
                \n6 - Peso\
                \n0 - Cancelar")

            action = int(input("\n> Acao: "))

            match action:
                case 1:
                    dado = input("\nNova informacao: ")
                    j1.setNome(dado)

                case 2:
                    dado = input("\nNova informacao: ")
                    j1.setPosicao(dado)

                case 3:
                    dado = input("\nNova informacao: ")
                    j1.setNascimento(dado)

                case 4:
                    dado = input("\nNova informacao: ")
                    j1.setNacionalidade(dado)

                case 5:
                    dado = int(input("\nNova informacao: "))
                    j1.setAltura(dado)

                case 6:
                    dado = float(input("\nNova informacao: "))
                    j1.setPeso(dado)

                case 0:
                    print("\nSaindo...")

                case _:
                    print("\nOpcao invalida. Saindo...")

            print("\n>>> Dados alterados <<<")
        
        case 4:
            print("\nSaindo...")
            break

        case _:
            print("\nOpcao invalida. Saindo...")
            break