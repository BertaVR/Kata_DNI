from src.tabla_asignacion import Tabla_asignacion

class Validar_DNI:

    def __init__(self, numero_DNI):
        self.numero_DNI = str(numero_DNI)

    def validar_formato(self):
        if len(numero_DNI) == 8:
            return True
        if len(numero_DNI) < 8:
            return False
            print ('Es demasiado corto')
            raise AssertionError
        if len(numero_DNI) > 8:
            return False
            print ('Es demasiado largo')
            raise AssertionError
        holahoal