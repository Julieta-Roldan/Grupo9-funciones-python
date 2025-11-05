from funciones.resta_rodriguez import resta_rodriguez

def test_resta_rodriguez():
    assert resta_rodriguez(10, 4) == 6
    assert resta_rodriguez(5, 10) == -5