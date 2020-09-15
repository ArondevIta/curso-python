from POO.associacao.classes import Escritor
from POO.associacao.classes import Caneta
from POO.associacao.classes import MaquinaDeEscrever

escritor = Escritor('João')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
