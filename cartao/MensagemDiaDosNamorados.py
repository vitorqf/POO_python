from CartaoMensagem import CartaoMensagem

class MensagemDiaDosNamorados(CartaoMensagem):
    def __init__(self, remetente, nome):
        super().__init__(remetente)
        self.nome = nome
        
    def __str__(self):
        return (
            f"{self.data}\
                \n\nQuerido(a) {self.nome},\
                \n\nVenho através dessa carta lhe desejar um excelente dia dos namorados.\
                \nQue essa data possa se repetir por muitos anos!\
                \n\nBeijos!\
                \n\n{self.remetente}"
        )