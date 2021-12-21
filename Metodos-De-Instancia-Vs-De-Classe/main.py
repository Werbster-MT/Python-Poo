from pessoa import Pessoa

if __name__ == '__main__':
    p1 = Pessoa('Luiz', 23)
    # var de classe
    print(Pessoa.anoAtual)
    # var de instância
    p1.getAnoNascimento()

    p2 = Pessoa.porAnoNascimento('Pedro', 1987)
    print(p2)
    print(p2.idade)
    p2.getAnoNascimento()