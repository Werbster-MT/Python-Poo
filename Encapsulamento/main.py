"""
    public, protected, private
    private/protected (public _): _
    private (__NomeDaClasse__nomeAtributo): __
"""

class BaseDeDados:
    # Construtor
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserirCliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id:nome})

    def listarClientes(self):
        for id,nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagarCliente(self, id):
        del self.__dados['clientes'][id]

bd = BaseDeDados()
bd.inserirCliente(1, 'Otávio')
bd.inserirCliente(2, 'Miranda')
bd.inserirCliente(3, 'Rose')

bd.__dados = 'Outra coisa'
print(bd.dados)
