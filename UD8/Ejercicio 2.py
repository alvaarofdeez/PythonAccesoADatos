class Cuenta():
    titular = ""
    cantidad = 0.0

    def __init__(self, titular):
        self.titular = titular
        self.cantidad = 0.0

    def getTitular(self):
        return print(self.titular)

    def getCantidad(self):
        return print(self.cantidad)

    def setNombre(self, x):
        self.titular = x

    def setEdad(self, x):
        self.cantidad = x

    def muestraDatos(self):
        return print("\nDatos de la cuenta:\nTitular: ", self.titular, "\nCantidad: ", self.cantidad,"€.")

    def ingresar(self, x):
        if x >= 0:
            self.cantidad = self.cantidad + x

    def retirar(self, x):
        if x >= 0:
            self.cantidad = self.cantidad - x


titular = str(input("Introduce el nombre del titular de la cuenta: "))

Alvaro = Cuenta(titular)

cantidad = float(input("Introduce la cantidad a ingresar: "))

Alvaro.ingresar(cantidad)
Alvaro.muestraDatos()

cantidad = float(input("Introduce la cantidad a retirar: "))

Alvaro.retirar(cantidad)
Alvaro.muestraDatos()

