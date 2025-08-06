from ..enum.tipoFicha import TipoFicha
class Ficha():
    def __init__(self,tipo:TipoFicha):
        self.tipo:TipoFicha = tipo
    def __repr__ (self):
        if self.tipo ==TipoFicha.EQUIS.value:
            return 'X'
        else:
            return 'O'