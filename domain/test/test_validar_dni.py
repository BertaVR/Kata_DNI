from src.validar_dni import Calcular_letra_DNI

def test_validar_longitud():
    assert Calcular_letra_DNI('41569305').validar_longitud() == True
    assert Calcular_letra_DNI('41567873829305').validar_longitud() == False
    assert Calcular_letra_DNI('41567').validar_longitud() == False


def test_validar_formato():
    assert Calcular_letra_DNI('41569305').validar_formato() == True
    assert Calcular_letra_DNI('41567873829305').validar_formato() == False
    assert Calcular_letra_DNI('41567').validar_formato() == False
    assert Calcular_letra_DNI('41567fff').validar_formato() == False
    assert Calcular_letra_DNI('abcdefgh').validar_formato() == False




def test_calcular_letra():
    assert Calcular_letra_DNI('41509405').calcular_letra() == 'V'
    assert Calcular_letra_DNI('72376173').calcular_letra() == 'A'
    assert Calcular_letra_DNI('01817200').calcular_letra() == 'Q'
    assert Calcular_letra_DNI('95882054').calcular_letra() == 'E'
    assert Calcular_letra_DNI('63587725').calcular_letra() == 'Q'
    assert Calcular_letra_DNI('26861694').calcular_letra() == 'V'
    assert Calcular_letra_DNI('66714505').calcular_letra() == 'S'
    assert Calcular_letra_DNI('76857238').calcular_letra() == 'R'
    assert Calcular_letra_DNI('80117501').calcular_letra() == 'Z'
    assert Calcular_letra_DNI('40135330').calcular_letra() == 'P'
    assert Calcular_letra_DNI('66499420').calcular_letra() == 'A'
    assert Calcular_letra_DNI('26868974').calcular_letra() == 'Y'


def test_añadir_letra():
    assert Calcular_letra_DNI('41509405').añadir_letra() == '41509405V'
    assert Calcular_letra_DNI('72376173').añadir_letra() == '72376173A'
    assert Calcular_letra_DNI('01817200').añadir_letra() == '01817200Q'
    assert Calcular_letra_DNI('95882054').añadir_letra() == '95882054E'
    assert Calcular_letra_DNI('63587725').añadir_letra() == '63587725Q'
    assert Calcular_letra_DNI('26861694').añadir_letra() == '26861694V'
    assert Calcular_letra_DNI('66714505').añadir_letra() == '66714505S'
    assert Calcular_letra_DNI('76857238').añadir_letra() == '76857238R'
    assert Calcular_letra_DNI('80117501').añadir_letra() == '80117501Z'
    assert Calcular_letra_DNI('40135330').añadir_letra() == '40135330P'
    assert Calcular_letra_DNI('66499420').añadir_letra() == '66499420A'
    assert Calcular_letra_DNI('26868974').añadir_letra() == '26868974Y'






