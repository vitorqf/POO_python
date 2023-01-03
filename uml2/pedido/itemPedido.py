from produto import Produto

class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int) -> None:
        self.__quantidade = quantidade
        self.__produto = produto

    def __str__(self) -> str:
        return f"CODIGO=[{self.__produto.codigo}]\
               \nDESCRICAO=[{self.__produto.descricao}]\
               \nVALOR=[{self.__produto.valor}]\
               \nQUANTIDADE=[{self.__quantidade}]"

    @property
    def quantidade(self) -> int:
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, other: int) -> None:
        self.__quantidade = other

    @property
    def produto(self) -> Produto:
        return self.__produto

    @produto.setter
    def produto(self, other: Produto) -> None:
        self.__produto = other