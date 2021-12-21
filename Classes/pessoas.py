from datetime import *

class Pessoa(object):
    # Atributo da classe, valor comum a todas as instâncias
    anoAtual = int(date.today().year)

    # Método construtor
    def __init__(self, nome, idade, comendo = False, falando = False):
        # Variáveis de instância são atributos da classe, com valores próprios para cada instância!
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    # Métodos da classe

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo!')
            return
        elif self.falando:
            print(f'{self.nome} já está falando!')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def pararFalar(self):
        if not self.falando:
            print(f'{self.nome} não está falando!')
            return

        print(f'{self.nome} parou de falar.')
        self.falando = False

    def comer(self, alimento):
        if self.comendo == True:
            print(f'{self.nome} já está comendo!')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando!')
            return

        self.comendo = True
        print(f'{self.nome} está comendo {alimento}.')

    def pararComer(self):
        # if self.comendo == False:
        if not self.comendo:
            print(f'{self.nome} não está comendo!')
            return
        print('{} parou de comer.'.format(self.nome))
        self.comendo = False

    def getAnoNascimento(self):
        return self.anoAtual - self.idade


