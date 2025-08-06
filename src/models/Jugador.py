from ..enum.tipoFicha import TipoFicha


class Jugador():
    def __init__(self,nombre:str,ficha:TipoFicha):
        self.nombre:str= nombre
        ficha:TipoFicha = ficha

    def __repr__(self):
        return self.nombre