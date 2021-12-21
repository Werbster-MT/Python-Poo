"""
Uma classe que utiliza a outra em sua composição, e uma vez que a instância
dessa primeira classe é apagada, todas as intâncias da classe que a compõem também serão
"""

from classes import *

if __name__ == "__main__":
    cliente1 = Cliente('Luiz', 32)
    cliente1.insereEndereco('Belo Horizante', 'MG')
    print(cliente1.nome)
    cliente1.listaEnderecos()
    print()

    cliente2 = Cliente('Maria', 24)
    cliente2.insereEndereco('Salvador', 'BA')
    cliente2.insereEndereco('Rio de Janeiro', 'RJ')
    print(cliente2.nome)
    cliente2.listaEnderecos()
    print()

    cliente3 = Cliente('Pedro', 19)
    cliente3.insereEndereco('São Paulo', 'SP')
    print(cliente3.nome)
    cliente3.listaEnderecos()
    print()

    print('#' * 50)