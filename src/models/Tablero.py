from ..exceptions.PosicionOcupadaException import PosOcupadaException
from ..exceptions.PosicionInvalidaException import PosInvalida
from src.models.Ficha import Ficha

class Tablero:
    def __init__(self):
        self.contenedor:list[Ficha|None] = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def poner_la_ficha(self, fil:int, col:int, ficha:Ficha):
        self.validarPosicion(fil,col)
        if self.contenedor[fil][col] == None:
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("POSICION OCUPADA!! Por favor elija otra")
    
    def validarPosicion(self,fil:int,col:int):
        if not isinstance(col, int) or not isinstance(fil,int):
            raise PosInvalida("POSICION INVALIDA!! Por favor elija una posicion valida (entre 0y2 para filas y columnas)")
        if fil>2 or col>2:
            raise PosInvalida("POSICION INVALIDA!! Por favor elija una posicion valida (entre 0y2 para filas y columnas)")
        if col<0 or fil<0:
            raise PosInvalida("POSICION INVALIDA!! Por favor elija una posicion valida (entre 0y2 para filas y columnas)")
    def hayEmpate(self) -> bool:
       if self.HayGanador():
           return False
       for fila in self.contenedor:
           for celda in fila:
               if celda is None:
                   return False
       return True
    def HayGanador(self) -> bool:
       # Verificar filas
       for fila in self.contenedor:
           if (fila[0] is not None and fila[1] is not None and fila[2] is not None and
               fila[0].tipo == fila[1].tipo == fila[2].tipo):
               return True
    
       # Verificar columnas
       for col in range(3):
           if (self.contenedor[0][col] is not None and 
               self.contenedor[1][col] is not None and 
               self.contenedor[2][col] is not None and
               self.contenedor[0][col].tipo == self.contenedor[1][col].tipo == self.contenedor[2][col].tipo):
               return True
    
       # Verificar diagonal principal
       if (self.contenedor[0][0] is not None and 
           self.contenedor[1][1] is not None and 
           self.contenedor[2][2] is not None and
           self.contenedor[0][0].tipo == self.contenedor[1][1].tipo == self.contenedor[2][2].tipo):
           return True
    
       # Verificar diagonal secundaria
       if (self.contenedor[0][2] is not None and 
           self.contenedor[1][1] is not None and 
           self.contenedor[2][0] is not None and
           self.contenedor[0][2].tipo == self.contenedor[1][1].tipo == self.contenedor[2][0].tipo):
           return True
    
       return False
    def mostrar_tablero(self):
        print("  0   1   2")
        for i, fila in enumerate(self.contenedor):
           print(f"{i} ", end="")
           for j, celda in enumerate(fila):
               if celda is None:
                   print(" ", end="")
               else:
                   print(celda, end="")
               
               if j < 2:
                   print(" | ", end="")
           print()
           
           if i < 2:
               print("  -----------")