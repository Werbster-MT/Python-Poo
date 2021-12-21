"""
Ato de herdar atributos, métodos de uma classe pai (superclasse)
"""
from classes import *

if __name__ == '__main__':

    c1 = Cliente('Luiz', 45)
    print(c1.nome)
    c1.falar()
    c1.comprar()
    print()

    a1 = Aluno('Pedro', 20)
    print(a1.nome)
    a1.falar()
    a1.estudar()