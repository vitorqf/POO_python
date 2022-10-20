import datetime

class Historico:
    def __init__(self, numero):
        if (numero):
            self.data_abertura = datetime.datetime.today()
            self.transacoes = []

        else:
            return None

    def imprime(self):
        print("*****HISTORICO*****\n\nData abertura: {}".format(self.data_abertura))
        print("Transações: ")
        for t in self.transacoes:
            print("-", t)  

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico(self.numero)
    
    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("Deposito de R$ {}".format(valor))

    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de R$ {}".format(valor))
            return True

    def extrato(self):
        print("*****EXTRATO*****\n\nDados do titular:\nNome: {}\nSobrenome: {}\nCPF: {}\n----------------------\nNumero da conta: {}\nSaldo bancario: R$ {}\n".format(self.titular.nome, self.titular.sobrenome, self.titular.cpf, self.numero, self.saldo))
        self.historico.transacoes.append("Feito extrato\n * saldo de R$ {}".format(self.saldo))

    def transfere_para(self, destino, valor):
        if (not self.saca(valor)):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("Transferencia de R$ {} para conta {}".format(valor, destino.numero))
            return True
