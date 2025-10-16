import unittest
from calculadora import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):
    
    def test_sumar(self):
        """Prueba la función sumar"""
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(0, 0), 0)
    
    def test_restar(self):
        """Prueba la función restar"""
        self.assertEqual(restar(5, 3), 2)
        self.assertEqual(restar(0, 5), -5)
        self.assertEqual(restar(10, 10), 0)
    
    def test_multiplicar(self):
        """Prueba la función multiplicar"""
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(5, 0), 0)
        self.assertEqual(multiplicar(-2, 3), -6)
    
    def test_dividir(self):
        """Prueba la función dividir"""
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)
        self.assertAlmostEqual(dividir(7, 2), 3.5)
    
    def test_dividir_por_cero(self):
        """Prueba que dividir por cero lance un error"""
        with self.assertRaises(ValueError):
            dividir(10, 0)

if __name__ == '__main__':
    unittest.main()