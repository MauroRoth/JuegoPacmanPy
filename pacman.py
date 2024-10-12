from mapa import Mapa
from posicion import Posicion

class Pacman:

    posicionInicial = Posicion(1,1)
    vidasIniciales = 3

    def __init__(self, mapa: Mapa):
        self.__posicion = Pacman.posicionInicial
        self.__mapa = mapa
        self.__vidas = Pacman.vidasIniciales

    def mover(self, posicionDestino: Posicion):
        if self.__mapa.esBloqueNavegable(posicionDestino):
            if self.__posicion.esAdyacente(posicionDestino):
                self.__posicion = posicionDestino
            else:
                print(
                    "El pacman no se puede mover desde "
                    + str(self.__posicion.obtenerPosicion())
                    + " hacia "
                    + str(posicionDestino.obtenerPosicion())
                )
        else:
            print(
                "La posición de destino " + str(posicionDestino.obtenerPosicion()) + " no es navegable!!!"
            )

    def establecerPosicion(self, posicion: Posicion) -> None:
        self.__posicion = posicion

    def obtenerPosicion(self) -> Posicion:
        return self.__posicion

    def establecerMapa(self, mapa: Mapa) -> None:
        self.__mapa = mapa

    def obtenerMapa(self) -> Mapa:
        return self.__mapa
    
    def establecerVidas(self, vidas: int) -> None:
        self.__vidas = vidas
    
    def obtenerVidas(self) -> int:
        return self.__vidas
    
    def obtenerPosicionInicial(self) -> Posicion:
        return Pacman.posicionInicial

    def copy(self, pacman2) -> None:
        self.__posicion = pacman2.obtenerPosicion()
        self.__mapa = pacman2.obtenerMapa()
        self.__vidas = pacman2.obtenerVidas()

    def clone(self):
        pacman2 = Pacman(self.__mapa)
        pacman2.establecerPosicion(self.__posicion)
        pacman2.establecerVidas(self.__vidas)
        return pacman2

    def equals(self, pacman2) -> bool:
        return (
            self.__posicion == pacman2.obtenerPosicion()
            and self.__mapa == pacman2.obtenerMapa()
            and self.__vidas == pacman2.obtenerVidas()
        )

mapa = Mapa()
pacman = Pacman(mapa)
posicionDestino = Posicion(1,5)
pacman.mover(posicionDestino)