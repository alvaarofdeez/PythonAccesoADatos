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

    def validarDNI(self):
        if type(self.dni[0:8] == str) and type(self.dni[8] == int):
            n = int(self.dni[0:8])
            letras = "TRWAGMYFPDXBNJZSQVHLCKE"
            letra = str(letras[n % 23])

            letraDNI = str(self.dni[8].upper())

            if letraDNI == letra:
                return True
            else:
                return False
        else:
            return False

    def validarNombre(self):
        if self.nombre.isalpha():
            return True
        else:
            return False

    def validarEdad(self):
        if type(self.edad == str):
            return False
        elif int(self.edad) < 0 and int(self.edad) >= 125:
            return False
        else:
            return True

    def muestraDatos(self):
        return print("\nDatos de la persona:\nNombre: ", self.nombre, "\nEdad: ", self.edad, "\nDNI: ", self.dni)

    def esMayorEdad(self):
        if type(self.edad) == int:
            if (int(self.edad) >= 18):
                return print("¿Es mayor de edad?", True)
        else:
            return print("¿Es mayor de edad?", False)


nombre = input("Introduce el nombre: ")
edad = input("Introduce la edad: ")
dni = input("Introduce el DNI: ")

alvaro = Persona()

alvaro.setNombre(nombre)
alvaro.setEdad(edad)
alvaro.setDNI(dni)

contador = 0
if alvaro.validarDNI() == False:
    print("El DNI intorducido no es correcto.")
else:
    contador = contador + 1
if alvaro.validarNombre() == False:
    print("El nombre debe estar formado unicamente por letras.")
else:
    contador = contador + 1
if alvaro.validarEdad() == False:
    print("La edad debe estar formada unimanete por números postivios y deberá ir desde 0 a 125.")
else:
    contador = contador + 1

if contador == 3:
    alvaro.muestraDatos()
    alvaro.esMayorEdad()