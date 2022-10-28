from veiculo import Veiculo
from historico import Historico

def checarTanque(veiculo, bomba, valor, litros):
    if (veiculo.abastecer(litros)):
        print("\nValor total: R$ {:.2f}\nTotal de litros: {:.2f} L".format(valor, litros))
        print("\n**** Abastecimento concluido!")

    else:
        print("\n**** O veiculo nao suporta a quantidade de combustivel")
        print("\nQuantidade disponivel no tanque: {:.2f} L\nQuantidade de combustivel comprada: {:.2f} L".format((veiculo.get_tanqueMax() - veiculo.get_tanqueAtual()), litros))

        bomba.alterarQuantidadeCombustivel(bomba.get_quantidadeCombustivel() + litros)

        opcao = int(input("\nDeseja encher o tanque? 1 - Sim, 2 - Nao\nEscolha: "))

        if (opcao == 1):
            litragemDisponivel = veiculo.get_tanqueMax() - veiculo.get_tanqueAtual()
            valorASerPago, litragemUtilizada = bomba.abastecerPorLitro(litragemDisponivel)
            print("\nQuantidade de litros utilizada: {:.2f} L\nValor a ser pago: R$ {:.2f}".format(litragemUtilizada, valorASerPago))

        else:
            print("\n**** Finalizando...")

class BombaCombustivel:
    def __init__(self, postoResponsavel, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.__postoResponsavel = postoResponsavel
        self.__tipoCombustivel = tipoCombustivel
        self.__quantidadeCombustivel = quantidadeCombustivel
        self.__valorLitro =  valorLitro
        self.__historico = Historico(self.get_postoResponsavel)

    def abastecerPorLitro(self, litros):
        valor = litros * self.__valorLitro
        self.alterarQuantidadeCombustivel(self.__quantidadeCombustivel - litros)
        self.__historico.transacoes.append("Compra efetuada no valor de R$ {:.2f}, equivalente a {:.2f} litro(s).".format(valor, litros))

        return valor, litros

    def abastecerPorValor(self, valor):
        litros = valor/self.__valorLitro
        self.alterarQuantidadeCombustivel(self.__quantidadeCombustivel - litros)
        self.__historico.transacoes.append("Compra efetuada no valor de R$ {:.2f}, equivalente a {:.2f} litro(s).".format(valor, litros))

        return valor, litros

    def alterarQuantidadeCombustivel(self, novaQuantidade):
        self.__historico.transacoes.append("Efetuada alteracao na quantidade de combustivel da bomba de {:.2f} litro(s) para {:.2f} litro(s).".format(self.get_quantidadeCombustivel(), novaQuantidade))
        self.__quantidadeCombustivel = novaQuantidade

        return self.__quantidadeCombustivel

    def alterarValorLitro(self, novoValor):
        self.__historico.transacoes.append("Efetuada troca de valor/litro da bomba de R$ {:.2f} para {:.2f}.".format(self.get_valorLitro(), novoValor))
        self.__valorLitro = novoValor

        return self.__valorLitro

    def alterarTipoCombustivel(self, novoTipo):
        self.__historico.append("Efetuada troca de combustivel da bomba de {} para {}.".format(self.get_tipoCombustivel(), novoTipo))
        self.__tipoCombustivel = novoTipo

        return self.__tipoCombustivel

    def get_quantidadeCombustivel(self):
        return self.__quantidadeCombustivel

    def get_tipoCombustivel(self):
        return self.__tipoCombustivel

    def get_postoResponsavel(self):
        return self.__postoResponsavel

    def get_valorLitro(self):
        return self.__valorLitro

    def get_historico(self):
        return self.__historico

bomba = BombaCombustivel('Carioca', 'Gasolina', 7.59, 500)

# modelo, ano, potencia, peso, consumo, tanqueMax, tanqueAtual, velocidadeMax
carro1 = Veiculo('Civic LXS 1.8', 2008, 140, 1260, 12, 50, 2.5, 200)


# --- Testes dos metodos

carro1.acelerar(10)
print("Velocidade atual: {} km/h".format(carro1.get_velocidade()))

carro1.acelerar(10)
print("Velocidade atual: {} km/h".format(carro1.get_velocidade()))

carro1.acelerar(10)
print("Velocidade atual: {} km/h".format(carro1.get_velocidade()))


valor, litros = bomba.abastecerPorLitro(40)
print("\n--- Novo abastecimento solicitado, verificando tanque do veiculo...")
checarTanque(carro1, bomba, valor, litros)

print("\n--- Novo abastecimento solicitado, verificando tanque do veiculo...")
valor, litros = bomba.abastecerPorLitro(40)
checarTanque(carro1, bomba, valor, litros)


carro1.acelerar(20)
print("\nVelocidade atual: {} km/h".format(carro1.get_velocidade()))

carro1.frear(10)
print("Velocidade atual: {} km/h".format(carro1.get_velocidade()))

print(bomba.get_historico().imprime())
# Fim dos testes