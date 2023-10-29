from datetime import datetime

class Persona:
    def __init__(self, Nombre, Apellido, FechaNacimiento, Direccion, Usuario, Clave):
        self.__Nombre = Nombre
        self.__Apellido = Apellido
        self.__FechaNacimiento = FechaNacimiento
        self.__Direccion = Direccion
        self.__Usuario = Usuario
        self.__Clave = Clave

    def getNombre(self):
        return self.__Nombre

    def getApellido(self):
        return self.__Apellido

    def getFechaNacimiento(self):
        return self.__FechaNacimiento

    def getDireccion(self):
        return self.__Direccion

    def getUsuario(self):
        return self.__Usuario

    def getClave(self):
        return self.__Clave

    def setNombre(self, Nombre):
        self.__Nombre = Nombre

    def setApellido(self, Apellido):
        self.__Apellido = Apellido

    def setFechaNacimiento(self, FechaNacimiento):
        self.__FechaNacimiento = FechaNacimiento

    def setDireccion(self, Direccion):
        self.__Direccion = Direccion

    def setUsuario(self, Usuario):
        self.__Usuario = Usuario

    def setClave(self, Clave):
        self.__Clave = Clave

    def calcular_edad(self):
        # Calcular la edad basado en la FechaNacimiento
        today = datetime.today()
        fecha_nacimiento = datetime.strptime(self.__FechaNacimiento, "%Y-%m-%d")
        edad = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        return edad

    def __str__(self):
        return f"Nombre: {self.__Nombre}, Apellido: {self.__Apellido}, Edad: {self.calcular_edad()}, Direccion: {self.__Direccion}, Usuario: {self.__Usuario}, Clave: {self.__Clave}"
