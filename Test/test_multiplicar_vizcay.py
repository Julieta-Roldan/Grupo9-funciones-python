# tests/test_multiplicar_vizcay.py

from Funciones.multiplicar_vizcay import multiplicar

def test_multiplicar():
    assert multiplicar(3, 4) == 12
    assert multiplicar(-2, 5) == -10
