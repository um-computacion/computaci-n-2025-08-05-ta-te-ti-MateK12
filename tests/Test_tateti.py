import unittest
from unittest.mock import patch
from src.models.Ficha import Ficha
from src.models.Jugador import Jugador
from src.models.Tablero import Tablero
from src.models.Tateti import Tateti
from src.enum.tipoFicha import TipoFicha
from src.exceptions.PosicionOcupadaException import PosOcupadaException
from src.exceptions.PosicionInvalidaException import PosInvalida


class TestFicha(unittest.TestCase):
    
    def test_crear_ficha_equis(self):
        ficha = Ficha(TipoFicha.EQUIS.value)
        self.assertEqual(ficha.tipo, TipoFicha.EQUIS.value)
    
    def test_crear_ficha_circulo(self):
        ficha = Ficha(TipoFicha.CIRCULO.value)
        self.assertEqual(ficha.tipo, TipoFicha.CIRCULO.value)
    
    def test_repr_ficha_equis(self):
        ficha = Ficha(TipoFicha.EQUIS.value)
        self.assertEqual(str(ficha), 'X')
    
    def test_repr_ficha_circulo(self):
        ficha = Ficha(TipoFicha.CIRCULO.value)
        self.assertEqual(str(ficha), 'O')


class TestJugador(unittest.TestCase):
    
    def test_crear_jugador(self):
        jugador = Jugador("Ana", TipoFicha.EQUIS.value)
        self.assertEqual(jugador.nombre, "Ana")
    
    def test_repr_jugador(self):
        jugador = Jugador("Pedro", TipoFicha.CIRCULO.value)
        self.assertEqual(str(jugador), "Pedro")


class TestTablero(unittest.TestCase):
    
    def setUp(self):
        self.tablero = Tablero()
        self.ficha_x = Ficha(TipoFicha.EQUIS.value)
        self.ficha_o = Ficha(TipoFicha.CIRCULO.value)
    
    def test_tablero_inicial_vacio(self):
        for fila in self.tablero.contenedor:
            for celda in fila:
                self.assertIsNone(celda)
    
    def test_poner_ficha_posicion_valida(self):
        self.tablero.poner_la_ficha(1, 1, self.ficha_x)
        self.assertEqual(self.tablero.contenedor[1][1], self.ficha_x)
    
    def test_poner_ficha_posicion_ocupada(self):
        self.tablero.poner_la_ficha(0, 0, self.ficha_x)
        with self.assertRaises(PosOcupadaException):
            self.tablero.poner_la_ficha(0, 0, self.ficha_o)
    
    def test_validar_posicion_invalida_mayor(self):
        with self.assertRaises(PosInvalida):
            self.tablero.validarPosicion(3, 1)
        with self.assertRaises(PosInvalida):
            self.tablero.validarPosicion(1, 3)
    
    def test_validar_posicion_invalida_negativa(self):
        with self.assertRaises(PosInvalida):
            self.tablero.validarPosicion(-1, 1)
        with self.assertRaises(PosInvalida):
            self.tablero.validarPosicion(1, -1)
    
    def test_validar_posicion_no_entero(self):
        with self.assertRaises(PosInvalida):
            self.tablero.validarPosicion(1.5, 1)
        with self.assertRaises(PosInvalida):
            self.tablero.validarPosicion(1, "2")
    
    def test_hay_ganador_fila(self):
        self.tablero.poner_la_ficha(0, 0, self.ficha_x)
        self.tablero.poner_la_ficha(0, 1, self.ficha_x)
        self.tablero.poner_la_ficha(0, 2, self.ficha_x)
        self.assertTrue(self.tablero.HayGanador())
    
    def test_hay_ganador_columna(self):
        self.tablero.poner_la_ficha(0, 0, self.ficha_o)
        self.tablero.poner_la_ficha(1, 0, self.ficha_o)
        self.tablero.poner_la_ficha(2, 0, self.ficha_o)
        self.assertTrue(self.tablero.HayGanador())
    
    def test_hay_ganador_diagonal_principal(self):
        self.tablero.poner_la_ficha(0, 0, self.ficha_x)
        self.tablero.poner_la_ficha(1, 1, self.ficha_x)
        self.tablero.poner_la_ficha(2, 2, self.ficha_x)
        self.assertTrue(self.tablero.HayGanador())
    
    def test_hay_ganador_diagonal_secundaria(self):
        self.tablero.poner_la_ficha(0, 2, self.ficha_o)
        self.tablero.poner_la_ficha(1, 1, self.ficha_o)
        self.tablero.poner_la_ficha(2, 0, self.ficha_o)
        self.assertTrue(self.tablero.HayGanador())
    
    def test_no_hay_ganador(self):
        self.tablero.poner_la_ficha(0, 0, self.ficha_x)
        self.tablero.poner_la_ficha(0, 1, self.ficha_o)
        self.assertFalse(self.tablero.HayGanador())
    
    def test_hay_empate(self):
        fichas = [
            [self.ficha_x, self.ficha_o, self.ficha_x],
            [self.ficha_o, self.ficha_o, self.ficha_x],
            [self.ficha_o, self.ficha_x, self.ficha_o]
        ]
        self.tablero.contenedor = fichas
        self.assertTrue(self.tablero.hayEmpate())
    
    def test_no_hay_empate_tablero_incompleto(self):
        self.tablero.poner_la_ficha(0, 0, self.ficha_x)
        self.assertFalse(self.tablero.hayEmpate())
    
    def test_no_hay_empate_con_ganador(self):
        self.tablero.poner_la_ficha(0, 0, self.ficha_x)
        self.tablero.poner_la_ficha(0, 1, self.ficha_x)
        self.tablero.poner_la_ficha(0, 2, self.ficha_x)
        self.tablero.poner_la_ficha(1, 0, self.ficha_o)
        self.tablero.poner_la_ficha(1, 1, self.ficha_o)
        self.tablero.poner_la_ficha(1, 2, self.ficha_o)
        self.tablero.poner_la_ficha(2, 0, self.ficha_x)
        self.tablero.poner_la_ficha(2, 1, self.ficha_x)
        self.tablero.poner_la_ficha(2, 2, self.ficha_o)
        self.assertFalse(self.tablero.hayEmpate())


class TestTateti(unittest.TestCase):
    
    def setUp(self):
        self.jugador1 = Jugador("Ana", TipoFicha.EQUIS.value)
        self.jugador2 = Jugador("Pedro", TipoFicha.CIRCULO.value)
        self.tateti = Tateti(self.jugador1, self.jugador2)
    
    def test_inicializacion_tateti(self):
        self.assertEqual(self.tateti.turno, TipoFicha.EQUIS.value)
        self.assertIsNone(self.tateti.ganador)
        self.assertFalse(self.tateti.empate)
        self.assertEqual(self.tateti.jugador1, self.jugador1)
        self.assertEqual(self.tateti.jugador2, self.jugador2)
    
    def test_get_turno_equis(self):
        self.assertEqual(self.tateti.getTurno(), 'X')
    
    def test_get_turno_circulo(self):
        self.tateti.turno = TipoFicha.CIRCULO.value
        self.assertEqual(self.tateti.getTurno(), 'O')
    
    def test_ocupar_casilla_turno_equis(self):
        self.tateti.ocupar_una_de_las_casillas(1, 1)
        ficha_colocada = self.tateti.tablero.contenedor[1][1]
        self.assertIsNotNone(ficha_colocada)
        self.assertEqual(ficha_colocada.tipo, TipoFicha.EQUIS.value)
    
    def test_ocupar_casilla_turno_circulo(self):
        self.tateti.turno = TipoFicha.CIRCULO.value
        self.tateti.ocupar_una_de_las_casillas(1, 1)
        ficha_colocada = self.tateti.tablero.contenedor[1][1]
        self.assertIsNotNone(ficha_colocada)
        self.assertEqual(ficha_colocada.tipo, TipoFicha.CIRCULO.value)
    
    def test_detectar_ganador_equis(self):
        self.tateti.ocupar_una_de_las_casillas(0, 0)  
        self.tateti.turno = TipoFicha.CIRCULO.value
        self.tateti.ocupar_una_de_las_casillas(1, 0)  
        self.tateti.turno = TipoFicha.EQUIS.value
        self.tateti.ocupar_una_de_las_casillas(0, 1)  
        self.tateti.turno = TipoFicha.CIRCULO.value
        self.tateti.ocupar_una_de_las_casillas(1, 1)  
        self.tateti.turno = TipoFicha.EQUIS.value
        self.tateti.ocupar_una_de_las_casillas(0, 2)  
        
        self.assertEqual(self.tateti.ganador, TipoFicha.EQUIS.value)
    
    def test_detectar_empate(self):
        movimientos = [
            (0, 0), (0, 1), (0, 2),
            (1, 1), (1, 0), (1, 2),
            (2, 1), (2, 0), (2, 2)
        ]
        turno_actual = TipoFicha.EQUIS.value
        
        for fil, col in movimientos:
            self.tateti.turno = turno_actual
            self.tateti.ocupar_una_de_las_casillas(fil, col)
            turno_actual = TipoFicha.CIRCULO.value if turno_actual == TipoFicha.EQUIS.value else TipoFicha.EQUIS.value
        
        self.assertTrue(self.tateti.empate)
        self.assertIsNone(self.tateti.ganador)


if __name__ == '__main__':
    unittest.main()