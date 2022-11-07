import re


class Persona():
    nombre = ""
    edad = 0
    dni = ""

    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.dni = ""

    def getNombre(self):
        return print(self.nombre)
    def getEdad(self):
        return print(self.edad)
    def getDNI(self):
        return print(self.dni)

    def setNombre(self, x):
        self.nombre = x
    def setEdad(self, x):
        self.edad = x
    def setDNI(self, x):
        self.dni = x

    def muestraDatos(self):
        return print("\nDatos de la persona:\nNombre: ",self.nombre,"\nEdad: ",self.edad,"\nDNI: ",self.dni)

    def esMayorEdad(self):
        if (self.edad >= 18):
            return print("¿Es mayor de edad?",True)
        else:
            return print("¿Es mayor de edad?",False)

    def validarDNI(self):
        import string
        numeroDNI = int(self.dni[0:7])
        letras = {0:"T",1:"R",2:"W",3:"A",4:"G",5:"M",6:"Y",7:"F",8:"P",9:"D",10:"X",
               11:"B",12:"N",13:"J",14:"Z",15:"S",16:"Q",17:"V",18:"H",19:"L",
               20:"C",21:"K",22:"E"}
        resto = numeroDNI % 23
        letra = letras[resto]

        letraDNI = str(self.dni[8])

        if letraDNI.equals(letra):
            return print("DNI correcto.")
        else:
            return print("DNI incorrecto.")

nombre = input("Introduce el nombre: ")
edad = int(input("Introduce la edad: "))
dni = input("Introduce el DNI: ")

alvaro = Persona()

alvaro.setNombre(nombre)
alvaro.setEdad(edad)
alvaro.setDNI(dni)

print("Comprobando datos...")
alvaro.validarDNI()

alvaro.muestraDatos()
alvaro.esMayorEdad()