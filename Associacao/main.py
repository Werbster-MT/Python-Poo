# Associação: as classes se relacionam, mas não dependem uma da outra para existirem

from classes import *

escritor = Escritor("Pedro")
caneta = Caneta('bic')
maquina = MaquinaDeEscrever('Positivo')

escritor.ferramenta = maquina

print(escritor.ferramenta.marca)
escritor.ferramenta.escrever()
