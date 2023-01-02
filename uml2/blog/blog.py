import datetime
from postagem import Postagem

class Blog():
    """Inicia a lista de postagem vazia"""
    def __init__(self) -> None:
        self.__postagens = []

    """Adiciona uma nova postagem na lista de postagens"""
    def adicionarPostagem(self, postagem: Postagem) -> None:
        self.__postagens.append(postagem)

    """Verifica se já existe uma postagem com mesmo da @params postagem caso sim, exclui a existente e por fim adiciona a postagem com a data de publicação atual"""
    def publicarPostagem(self, postagem: Postagem) -> None:
        postagem.dataPublicacao = datetime.datetime.now()

        for existente in self.__postagens:
            if postagem.id == existente.id:
                self.__postagens.remove(existente)

        self.__postagens.append(postagem)

    """Verifica se existe alguma postagem publicada, caso não, retorna none, caso sim, retorna a lista de postagens publicadas"""
    def listarPostagensPublicadas(self) -> list[Postagem] or None:
        postagensPublicadas = [postagem for postagem in self.__postagens if postagem.dataPublicacao < datetime.datetime.now()]

        if len(postagensPublicadas) == 0:
            return None
            
        return postagensPublicadas

    """Verifica se existe alguma postagem existente, caso não, retorna none, caso sim, retorna a lista de postagens"""
    def listarTodasAsPostagens(self) -> list[Postagem] or None:
        if len(self.__postagens) == 0:
            return None

        return self.__postagens

    def apagarPostagem(self, postagem: Postagem) -> None:
        def checkId(existente):
            if existente.id == postagem.id:
                return False

            return True

        self.__postagens = list(filter(checkId, self.__postagens))


    @property
    def postagens(self) -> list[Postagem]:
        return self.__postagens

    @postagens.setter
    def postagens(self, other: list[Postagem]) -> None:
        self.__postagens = other