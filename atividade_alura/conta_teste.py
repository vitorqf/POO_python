from conta import Conta, Cliente, Historico

cliente1 = Cliente('João', 'Oliveira', '1111111111-1')
cliente2 = Cliente('Alberto', 'Augusto', '1111222333-4')

conta1 = Conta('123-4', cliente1, 120.0, 1000.0)
conta2 = Conta('456-7', cliente2, 360.50, 800.0)

conta1.deposita(50.0)
conta1.saca(20.0)
conta1.extrato()
conta1.transfere_para(conta2, 60.0)
conta1.historico.imprime()

try:
    historico = Historico()

except TypeError:
    print("\n****ERRO****\n\nNao eh possivel criar um historico sem uma conta")
