from src.models.Tateti import Tateti
from src.models.Jugador import Jugador
from src.enum.tipoFicha import TipoFicha
from src.models.Ficha import Ficha
from src.models.Tablero import Tablero
def main():
    print("Bienvenidos al Tateti")
    nombre1 = input('ingrese el nombre de las X: ')
    nombre2 = input('ingrese el nombre de los O: ')
    Final = False

    jugador1 = Jugador(nombre1,TipoFicha.EQUIS.value)
    jugador2 = Jugador(nombre2,TipoFicha.CIRCULO.value)
    juego = Tateti(jugador1,jugador2)
    while not Final:
        print("Tablero: ")
        juego.tablero.mostrar_tablero()
        print("Turno: ",juego.getTurno())

        try:
            fil = int(input("Ingrese fila: "))
            col = int(input("Ingrese columna: "))
            juego.ocupar_una_de_las_casillas(fil, col)
            if juego.ganador==TipoFicha.EQUIS.value:
                print('El ganador es el jugador de la Xs:',jugador1)
                juego.tablero.mostrar_tablero()
                Final = True
            elif  juego.ganador==TipoFicha.CIRCULO.value:
                print('El ganador es el jugador de los circulos: ',jugador2)
                juego.tablero.mostrar_tablero()
                Final = True
            elif juego.empate:
                print('Empate, ya no hay mas lugar')
                juego.tablero.mostrar_tablero()
                Final=True
            else:
                print('Nadie ha ganado, todavia...')
            if juego.turno==TipoFicha.EQUIS.value:
                juego.turno = TipoFicha.CIRCULO.value
            else:
                juego.turno =TipoFicha.EQUIS.value
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
