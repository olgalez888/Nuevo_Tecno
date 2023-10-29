from Persona import Persona

class Empleado(Persona):
    def __init__(self, Nombre, Apellido, FechaNacimiento, Direccion, Cargo, Antiguedad, Usuario, Clave):
        super().__init__(Nombre, Apellido, FechaNacimiento, Direccion, Usuario, Clave)
        self.Cargo = Cargo
        self.Antiguedad = Antiguedad

    def getCargo(self):
        return self.Cargo

    def getAntiguedad(self):
        return self.Antiguedad

    def setCargo(self, Cargo):
        self.Cargo = Cargo

    def setAntiguedad(self, Antiguedad):
        self.Antiguedad = Antiguedad

    def __str__(self):
        return f"{super().__str__()}, Cargo: {self.Cargo}, Antiguedad: {self.Antiguedad}"
