from funciones.lucas_multiplicar import lucas_multiplicar

def test_lucas_multiplicar():
    assert lucas_multiplicar(3, 4) == 12
    assert lucas_multiplicar(-2, 5) == -10

