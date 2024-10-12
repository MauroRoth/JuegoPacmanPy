from mapa import Mapa
from pacman import Pacman
from posicion import Posicion


class Fantasma:
    # atributos de clase
    posicionInicial = Posicion(13,11)

    # método de inicialización
    def __init__(self, mapa: Mapa, color: str) -> None:
        # atributos de instancia
        self.__posicion = Fantasma.posicionInicial
        self.__mapa = mapa
        self.__color = color

    # comandos
    def mover(self, posicionDestino: Posicion) -> None:
        if self.__mapa.esBloqueNavegable(posicionDestino):
            if self.__posicion.esAdyacente(posicionDestino):
                self.__posicion = posicionDestino
            else:
                print(
                    "El fantasma no se puede mover desde "
                    + str(self.__posicion.obtenerPosicion())
                    + " hacia "
                    + str(posicionDestino.obtenerPosicion())
                )
        else:
            print(
                "La posición de destino " + str(posicionDestino.obtenerPosicion()) + " no es navegable!!!"
            )
    
    def comer(self, pacman: Pacman) -> None:
        if self.__posicion == pacman.obtenerPosicion():
            if (pacman.obtenerVidas() > 0):
                print("Fantasma comiendo al pacman!!!")
                pacman.establecerVidas(pacman.obtenerVidas() - 1)
                pacman.establecerPosicion(pacman.obtenerPosicionInicial())
            else:
                print("El pacman que intenta comer está muerto!!!")
        else:
            print("El fantasma se encuentra en una posicion distinta a la del pacman!!!")


    def establecerPosicion(self, posicion: Posicion) -> None:
        self.__posicion = posicion

    def establecerMapa(self, mapa: Mapa) -> None:
        self.__mapa = mapa

    def establecerColor(self, color: str) -> None:
        self.__color = color


    # consultas
    def puedeMover(self, posicionDestino: Posicion) -> bool:
        return (self.__mapa.esBloqueNavegable(posicionDestino)
            and self.__posicion.esAdyacente(posicionDestino))
    
    def obtenerPosicion(self):
        return self.__posicion

    def obtenerMapa(self):
        return self.__mapa
    
    def obtenerColor(self):
        return self.__color

