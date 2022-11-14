from CartaoMensagem import CartaoMensagem

class MensagemDiaDosNamorados(CartaoMensagem):
    def __str__(self):
        return (
            f"{self.data}\n\nQuerido(a) {self.nome},\n\nVenho através dessa carta lhe desejar um excelente dia dos namorados.\nQue essa data possa se repetir por muitos anos!\nBeijos!\n\n{self.remetente}"
        )