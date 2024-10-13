from mapa import Mapa
from pacman import Pacman
from fantasma import Fantasma
from posicion import Posicion

mapa = Mapa()
#list(map(lambda x: print(x),mapa.obtenerPosiciones()))
posicionDestino = Posicion(1,5)
print(mapa.esBloqueNavegable(posicionDestino))
pacman = Pacman(mapa)
#print(pacman.obtenerMapa().obtenerPosiciones())
print(pacman.obtenerPosicion().obtenerPosicion())
pacman.mover(posicionDestino)
fantasma = Fantasma(mapa,'azul')
print('color fantasma: ',fantasma.obtenerColor())
print('posición fantasma: ',fantasma.obtenerPosicion().obtenerPosicion())
fantasma.comer(pacman)
print('fantasma puedeMover: ',fantasma.puedeMover(posicionDestino))




