from pedido import Pedido
from itemPedido import ItemPedido
from produto import Produto

produto1 = Produto(2001, 129.99, 'Pneu Pretinho')
produto2 = Produto(2002, 8.99, 'Escova de Dentes')

itempedido1 = ItemPedido(produto1, 2)
itempedido2 = ItemPedido(produto2, 1)

pedido1 = Pedido()

pedido1.adicionar_item(itempedido1)
pedido1.adicionar_item(itempedido2)

print(f"== Valor total ==\nR$ {pedido1.obter_total():.2f}")