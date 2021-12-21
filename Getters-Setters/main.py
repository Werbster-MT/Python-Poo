class Produto:
    # Método Construtor
    def __init__(self, preco):
        self.nome
        self.preco = preco

    # Método de instância
    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def nome(self):
        return self.nome

    # Setter
    @nome.setter
    def nome(self, valor):
        self.nome = valor.lower()

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

p1 = Produto(50)
p1.desconto(10)
p1.nome = 'Bola'
print(p1._nome, p1.preco)
