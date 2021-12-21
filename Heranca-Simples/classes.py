class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__

    def falar(self):
        print('{} Está falando...'.format(self.nomeClasse))

class Cliente(Pessoa):
    def comprar(self):
        print('{} está comprando...'.format(self.nomeClasse))

class Aluno(Pessoa):
    def estudar(self):
        print('{} está estudando...'.format(self.nomeClasse))


