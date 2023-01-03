class Produto:
    def __init__(self, codigo: int, valor: float, descricao: str) -> None:
        self.__codigo = codigo
        self.__valor = valor
        self.__descricao = descricao

    @property
    def codigo(self) -> int:
        return self.__codigo

    @codigo.setter
    def codigo(self, other: int) -> None:
        self.__codigo = other

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, other: float) -> None:
        self.__valor = other

    @property
    def descricao(self) -> str:
        return self.__descricao

    @descricao.setter
    def descricao(self, other: str) -> None:
        self.__descricao = other