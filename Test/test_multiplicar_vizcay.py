# tests/test_multiplicar_vizcay.py

from Funciones.multiplicar_vizcay import multiplicar_vizcay

def test_multiplicar_vizcay():
    assert multiplicar_vizcay(3, 4) == 12
    assert multiplicar_vizcay(-2, 5) == -10
