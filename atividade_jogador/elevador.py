class Admin:
    def mudanca():
        print("\nEscolha o que deseja alterar:\
            \n1 - Andar\
            \n2 - Total andares\
            \n3 - Capacidade\
            \n4 - Ocupantes\
            \n0 - Sair"
        )

        action = int(input("\n--> "))

        match action:
            case 1:
                dado = int(input("\nInsira o novo dado: "))
                e1.set_andarAtual(dado)

            case 2:
                dado = int(input("\nInsira o novo dado: "))
                e1.set_andarTotal(dado)

            case 3:
                dado = int(input("\nInsira o novo dado: "))
                e1.set_capacidade(dado)

            case 4:
                dado = int(input("\nInsira o novo dado: "))
                e1.set_ocupantes(dado)

            case 0:
                print("\n> Saindo...")

            case _:
                print("\n> Opcao inexistente! Saindo...")

        print("\n> Alteracoes concluidas! \n")

    def extrair():
        print("\n*** Dados do Elevador ***\
            \nANDAR ATUAL => {}\
            \nTOTAL DE ANDARES => {}\
            \nCAPACIDADE => {}\
            \nOCUPANTES => {}\n"\
            .format(
                e1.get_andarAtual(),
                e1.get_andarTotal(),
                e1.get_capacidade(),
                e1.get_ocupantes()
            )
        )

class Elevador:
    def __init__(self, capacidade, andarTotal):
        self.__andarAtual = 0
        self.__andarTotal = andarTotal
        self.__capacidade = capacidade
        self.__ocupantes = 0

    def entrar(self):
        if (self.__capacidade > self.__ocupantes):
            self.__ocupantes += 1
            print("\nEntrou uma pessoa no elevador! Quantidade de pessoas: ", self.__ocupantes)

        else:
            print("\nElevador com capacidade maxima! Capacidade: ", self.__capacidade)

    def sair(self):
        if (self.__ocupantes > 0):
            self.__ocupantes -= 1
            print("\nSaiu uma pessoa do elevador! Espaco restante: ", (self.__capacidade - self.__ocupantes))

        else:
            print("\nNao ha ninguem no elevador.")

    def subir(self):
        if (self.__andarAtual < self.__andarTotal):
            print("\nSubindooo! Destino: {}º andar".format(self.__andarAtual + 1))
            self.__andarAtual += 1

        else:
            print("\nVoce ja esta no ultimo andar")

    def descer(self):
        if (self.__andarAtual > 0):
            print("\nDescendooo! Destino: {}º andar".format(self.__andarAtual - 1)) if self.__andarAtual - 1 > 0 else print("\nDescendooo! Destino: Terreo")
            self.__andarAtual -= 1

        else:
            print("\nVoce ja esta no terreo")

    def get_andarAtual(self):
        return self.__andarAtual

    def set_andarAtual(self, dado):
        self.__andarAtual = dado

    def get_andarTotal(self):
        return self.__andarTotal

    def set_andarTotal(self, dado):
        self.__andarTotal = dado

    def get_capacidade(self):
        return self.__capacidade

    def set_capacidade(self, dado):
        self.__capacidade = dado

    def get_ocupantes(self):
        return self.__ocupantes

    def set_ocupantes(self, dado):
        self.__ocupantes = dado


e1 = Elevador(5, 3)

print("\nQual acao deseja realizar?\
        \n1 - Entrar\
        \n2 - Sair\
        \n3 - Subir\
        \n4 - Descer\
        \n0 - Cancelar \
        \n\n< Administracao >\
        \n5 - Extrair dados do elevador\
        \n6 - Alterar dados do elevador")


senha = 'admin123'
usuarioLogado = False

while True:
    choice = int(input("\n==> "))

    match choice:
        case 1:
            e1.entrar()

        case 2:
            e1.sair()

        case 3:
            e1.subir()

        case 4:
            e1.descer()

        case 5:
            if (usuarioLogado):

                Admin.extrair()
            
            else:
                login = input("\nInsira a senha de administrador\nSenha: ")

                if (login == senha):
                    usuarioLogado = True
                    
                    Admin.extrair()

                else:
                    print("\n=> Senha invalida! Finalizando operacoes...")
                    break

        case 6:
            if (usuarioLogado):

                Admin.mudanca()
            
            else:
                login = input("\nInsira a senha de administrador\nSenha: ")

                if (login == senha):
                    usuarioLogado = True
                    
                    Admin.mudanca()

                else:
                    print("\n=> Senha invalida! Finalizando operacoes...")
                    break

        case 0:
            print("\nOperacoes finalizadas. Saindo...")
            break

        case _:
            print("\nOpcao inexistente. Finalizando.")
            break
