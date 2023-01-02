from datetime import datetime

class Postagem():
    def __init__(self, id: int, titulo: str, texto: str, dataPublicacao: datetime.today()) -> None:
        self.__id = id
        self.__titulo = titulo
        self.__texto = texto
        self.__dataPublicacao = dataPublicacao

    def __str__(self) -> str:
        return f"\n{'':-^80} \
            \n{f'[{self.id}]':<40}{f'[{self.dataPublicacao}]':>40} \
            \n{self.titulo} \
            \n{self.texto} \
            \n{'':-^80}"
            
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, other: int) -> None:
        self.__id = other

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, other: str) -> None:
        self.__titulo = other

    @property
    def texto(self) -> str:
        return self.__texto

    @texto.setter
    def texto(self, other: str) -> None:
        self.__texto = other

    @property
    def dataPublicacao(self) -> datetime:
        return self.__dataPublicacao

    @dataPublicacao.setter
    def dataPublicacao(self, other: datetime) -> None:
        self.__dataPublicacao = other