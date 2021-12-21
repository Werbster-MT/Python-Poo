# Na agregação as classes existem por sí só, mas uma classe precisa da outra para fazer sentido/funcionar

from classes import *

carrinho = CarinhoDeCompras()
print(carrinho)

p1 = Produto("Camiseta", 50.0)
p2 = Produto("Iphone", 1550.0)
p3 = Produto("Caneca", 15.0)

carrinho.inserirProduto(p1)
carrinho.inserirProduto(p2)
carrinho.inserirProduto(p3)
carrinho.listaProdutos()
print(carrinho.somaTotal())