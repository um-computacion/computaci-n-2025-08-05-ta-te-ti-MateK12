from src.models.Tablero import Tablero
from ..enum.tipoFicha import TipoFicha
from src.models.Jugador import Jugador
from src.models.Ficha import Ficha


class Tateti:
    def __init__(self,jugador1:Jugador,jugador2:Jugador):
        self.turno:TipoFicha = TipoFicha.EQUIS.value
        self.tablero = Tablero()
        self.ganador:TipoFicha = None
        self.jugador1:Jugador = jugador1
        self.jugador2:Jugador = jugador2

    def ocupar_una_de_las_casillas(self, fil, col):
        if self.turno==TipoFicha.EQUIS.value:
            equis = Ficha(TipoFicha.EQUIS.value)
            self.tablero.poner_la_ficha(fil, col,equis)
            if self.tablero.HayGanador():
                self.ganador = TipoFicha.EQUIS.value
        else:
            circulo = Ficha(TipoFicha.CIRCULO.value)
            self.tablero.poner_la_ficha(fil, col,circulo)
            if self.tablero.HayGanador():
                self.ganador = TipoFicha.CIRCULO.value
        if self.tablero.HayGanador():
            print('Hay ganadorrrrr')
    def getTurno(self)->str:
        if self.turno==TipoFicha.EQUIS.value:
            return 'X'
        else:
            return 'O'