from CartaoMensagem import CartaoMensagem

class MensagemAniversario(CartaoMensagem):
    def __str__(self):
        return (
            f"{self.data}\
                \n\nEstimado(a) {self.nome},\
                \n\nQuero te desejar, com a maior vontade, um FELIZ ANIVERSÁRIO!\
                \nQue todos seus desejos se realizem.\
                \nE que possa comemorar a data por muitos e muitos anos\
                \n\nGrandes abraços!\
                \n\n{self.remetente}"
        )