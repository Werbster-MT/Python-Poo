from pessoas import Pessoa

if __name__ == "__main__":
    p1 = Pessoa('Luiz', 19)
    p2 = Pessoa('João', 32)

    p1.falar('Poo')
    p2.comer('Churrasco')
    p1.comer('Pastel')

    print(p1.anoAtual)
    print(p1.getAnoNascimento())