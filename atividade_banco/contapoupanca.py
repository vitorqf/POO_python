from conta import Conta


class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        return super().atualiza(taxa * 3)