
class Posicion:
    # atributos de clase
    # método de inicialización
    def __init__(self, posicionX: int, posicionY: int) -> None:
        # atributos de instancia
        self.__posicionX = posicionX
        self.__posicionY = posicionY

    # comandos
    def establecerPosicionX(self, posicionX: int) -> None:
        self.__posicionX = posicionX

    def establecerPosicionY(self, posicionY: int) -> None:
        self.__posicionY = posicionY

    # consultas
    def obtenerPosicionX(self) -> int:
        return self.__posicionX

    def obtenerPosicionY(self) -> int:
        return self.__posicionY
    
    def obtenerPosicion(self) -> list[int]:
        return [self.__posicionX,self.__posicionY]
    
    def esAdyacente(self, posicion) -> bool:
        posicionX = posicion.obtenerPosicionX()
        posicionY = posicion.obtenerPosicionY()
   
        sonAdyancentes = False
        if posicionX == self.__posicionX and (
            posicionY - 1 == self.__posicionY or posicionY + 1 == self.__posicionY
        ):
            sonAdyancentes = True
        elif posicionY == self.__posicionY and (
            posicionX - 1 == self.__posicionX or posicionX + 1 == self.__posicionX
        ):
            sonAdyancentes = True
        return sonAdyancentes
        
