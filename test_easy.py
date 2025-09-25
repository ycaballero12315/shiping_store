import pytest

class TestCalculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b
    
    def test_sumar(self):
        assert self.sumar(3, 5) == 8

    def test_restar(self):
        assert self.restar(10, 4) == 6

    def test_multiplicar(self):
        assert self.multiplicar(7, 6) == 42 

    def test_dividir(self):
        assert self.dividir(20, 4) == 5

    def test_dividir_por_cero(self):
        with pytest.raises(ValueError):
            self.dividir(10, 0) 

    def test_dividir_por_cero_mensaje(self):
        with pytest.raises(ValueError, match="No se puede dividir por cero"):
            self.dividir(15, 0)

    def test_sumar_numeros_negativos(self):
        assert self.sumar(-3, -7) == -10 

    def test_restar_numeros_negativos(self):
        assert self.restar(-10, -4) == -6

    def test_multiplicar_por_cero(self):
        assert self.multiplicar(7, 0) == 0

    def test_multiplicar_numeros_negativos(self):
        assert self.multiplicar(-7, 6) == -42

    def test_dividir_numeros_negativos(self):
        assert self.dividir(-20, 4) == -5
        
    def test_dividir_numeros_negativos_ambos(self):
        assert self.dividir(-20, -4) == 5