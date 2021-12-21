class Escritor:
    # Construtor fucionando com set
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    # Get
    @property
    def ferramenta(self):
        return self.__ferramenta

    # Set
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        if isinstance(ferramenta, Caneta) or isinstance(ferramenta, MaquinaDeEscrever):
            self.__ferramenta = ferramenta

    # Get
    @property
    def nome(self):
        return self.__nome




class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')




class MaquinaDeEscrever:
    def __init__(self, marca):
        self.__marca = marca
        pass

    # get
    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Máquina está escrevendo...')