from src.tabla_asignacion import Tabla_asignacion

class Calcular_letra_DNI:

    def __init__(self, numero_DNI):
        self.numero_DNI = str(numero_DNI)

    
    def validar_longitud(self):
        if len(self.numero_DNI) == Tabla_asignacion.longitud_numero:
            return True
        else:
            return False
    
    def validar_formato(self):
        if Calcular_letra_DNI.validar_longitud(self) == True and self.numero_DNI.isdigit():
            return True
        else:
            return False



    def calcular_letra(self):
        resto_num_cantidad_letras = int(self.numero_DNI)%(len(Tabla_asignacion.tabla_letras))
        letra = Tabla_asignacion.tabla_letras[resto_num_cantidad_letras]
        return letra

    
    def añadir_letra(self):
        if Calcular_letra_DNI.validar_formato(self) == True:
            DNI_con_letra = self.numero_DNI + Calcular_letra_DNI.calcular_letra(self)
            return DNI_con_letra
        else:
            return False
            print ('No es válido')




