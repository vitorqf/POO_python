from CartaoMensagem import CartaoMensagem

class MensagemNatal(CartaoMensagem):
    def __init__(self, remetente, nome):
        super().__init__(remetente)
        self.nome = nome
        
    def __str__(self):
        return (
            f"{self.data}\
                \n\nOlá!!!! {self.nome},\
                \n\nQuanto tempo não nos vemos, hein? Enfim...\
                \nEspero que receba a carta o quantos antes\
                \nTe desejo um ótimo natal, na verdade, para você e toda sua família!\
                \n\nAbraços!\
                \n\n{self.remetente}"
        )