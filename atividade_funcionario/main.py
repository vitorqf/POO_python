from gerente import Gerente
import funcionario as f

# gerente = Gerente('José', '222222222-22', 5000.0, '1234', 0)
# print(gerente.get_bonificacao())

funcionario = f.Funcionario('João', '111111111-11', 2000.0)
print("bonificacao funcionario: {}".format(funcionario.get_bonificacao()))

gerente = Gerente("José", "222222222-22", 5000.0, '1234', 0)
print("bonificacao gerente: {}".format(gerente.get_bonificacao()))

controle = f.ControleDeBonificacoes()
controle.registra(funcionario)
controle.registra(gerente)

print("total: {}".format(controle.total_bonificacoes))