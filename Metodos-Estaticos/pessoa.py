import random

class Pessoa:
    anoAtual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # método de instância: está relacionado diretamete com a instância da classe
    def getAnoNascimento(self):
        print('Seu ano de nascimento é {}'.format(self.anoAtual - self.idade))

    # método de classe: referente a classe em si
    @classmethod
    def porAnoNascimento(cls, nome, anoNascimento):
        idade = cls.anoAtual - anoNascimento
        return cls(nome, idade) # retorna uma instância da classe (factory method)

    @staticmethod
    def gerarId():
        rand = random.randint(10000, 19999)
        return rand

