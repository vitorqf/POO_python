# Questao 01
from conta import Conta

# Questao 02
from contacorrente import ContaCorrente
from contapoupanca import ContaPoupanca
from containvestimento import ContaInvestimento

from atualizadordecontas import AtualizadorDeContas
from banco import Banco

if __name__ == '__main__':
    # Questao 03
    # Numero / Titular / Saldo
    try:
        c = Conta('123-4', 'Joao', 1000.0)

    except TypeError as e:
        print(e)

    cc = ContaCorrente('123-5', 'Jose', 'Corrente', 1000.0)
    cp = ContaPoupanca('123-6', 'Maria', 'Poupanca', 1000.0)
    ci = ContaInvestimento('123-6', 'Maria', 'Investimento', 1000.0)

    bb = Banco('0001', 'Banco do Brasil')

    ci.deposita(1000.0)

    ci.atualiza(0.01)
    cc.atualiza(0.01)
    cp.atualiza(0.01)

    print(cc.saldo)
    print(cp.saldo)
    print(ci.saldo)

    # Questao 04
    print(cc)
    print(cp)

    # Fim Questao 03

    # Questao 05
    adc = AtualizadorDeContas(0.01)
    adc.exec(cc)
    adc.exec(cp)

    # (opcional) Questao 02 
    # Ao criar uma classe ContaInvestimento que tivesse um método atualiza complicado - isto é, que utilizasse de diversas operações, não seria necessário alterar o atualizador de contas visto que o método atualiza continuaria retornando um valor final.

    # (opcional) Questao 03 
    print(f"\nTotal de contas no {bb.nome}: {bb.pegaTotalDeContas()}")

    bb.adiciona(cc)
    bb.adiciona(cp)

    print(f"\nPrimeira conta do {bb.nome}: \n{bb.pegaConta(0)}")

    print(f"\nTotal de contas no {bb.nome}: {bb.pegaTotalDeContas()}")

    for conta in bb.lista_contas:
        adc.exec(conta)

    # (opcional) Questao 04, como foi escrito:
    """
    def atualiza(self, taxa):
        return super().atualiza(taxa * 2)    
    """ 
    # e
    """
    def atualiza(self, taxa):
        return super().atualiza(taxa * 3)    
    """

    # (opcional) Questao 05, pode ser feito um bloco try/except





