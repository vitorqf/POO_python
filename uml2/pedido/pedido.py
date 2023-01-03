from itemPedido import ItemPedido


class Pedido:
    def __init__(self, valor_total: float = 0.0) -> None:
        self.__valor_total = valor_total
        self.__carrinho = list()

    def adicionar_item(self, item: ItemPedido) -> None:
        self.__carrinho.append(item)

    def obter_total(self) -> float or None:
        
        if len(self.__carrinho) < 1:
            return None

        for item in self.__carrinho:
            self.__valor_total += (item.produto.valor * item.quantidade)

        return self.__valor_total

    @property
    def valor_total(self) -> float:
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, other: float) -> None:
        self.__valor_total = other