from Persona import Persona

class Cliente(Persona):
    def __init__(self, Nombre, Apellido, FechaNacimiento, Direccion, Ciudad, Telefono, Usuario, Clave):
        super().__init__(Nombre, Apellido, FechaNacimiento, Direccion, Usuario, Clave)
        self.Ciudad = Ciudad
        self.Telefono = Telefono

    def getCiudad(self):
        return self.Ciudad

    def getTelefono(self):
        return self.Telefono

    def setCiudad(self, Ciudad):
        self.Ciudad = Ciudad

    def setTelefono(self, Telefono):
        self.Telefono = Telefono

    def __str__(self):
        return f"{super().__str__()}, Ciudad: {self.Ciudad}, Telefono: {self.Telefono}"
