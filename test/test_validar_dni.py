from src.validar_dni import Validar_DNI

def test_validar_formato():
    assert Validar_DNI('41569305').validar_formato == True
    assert Validar_DNI('4155965').validar_formato == False, 'es demasiado corto'

