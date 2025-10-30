from Funciones.rodriguez_resta import rodriguez_resta

def test_rodriguez_resta():
    assert rodriguez_resta(10, 4) == 6
    assert rodriguez_resta(5, 10) == -5
