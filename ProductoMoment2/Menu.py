
from Empleado import Empleado
from Cliente import Cliente

empleados = []
clientes = []

def empleado_added_callback(empleado):
    print(f"Empleado {empleado.getNombre()} {empleado.getApellido()} ha sido asignado.")

empleadosPorEdad = lambda age: [empleado for empleado in empleados if empleado.calcular_edad() > age]

def insert_empleado():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    fecha_nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD): ")
    direccion = input("Dirección: ")
    cargo = input("Cargo: ")
    antiguedad = input("Antigüedad: ")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    empleado = Empleado(nombre, apellido, fecha_nacimiento, direccion, cargo, antiguedad, usuario, clave)
    empleados.append(empleado)
    empleado_added_callback(empleado)

def insert_cliente():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    fecha_nacimiento = input("Fecha de Nacimiento (YYYY-MM-DD): ")
    direccion = input("Dirección: ")
    ciudad = input("Ciudad: ")
    telefono = input("Teléfono: ")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    cliente = Cliente(nombre, apellido, fecha_nacimiento, direccion, ciudad, telefono, usuario, clave)
    clientes.append(cliente)
    print("Cliente creado:", cliente)

def login():
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    type_of_persona = input("Tipo de Persona (Cliente/Empleado): ").capitalize()

    if type_of_persona == "Cliente":
        collection = clientes
    elif type_of_persona == "Empleado":
        collection = empleados
    else:
        print("Tipo de Persona no válido. Use 'Cliente' o 'Empleado'.")
        return

    for persona in collection:
        if persona.getUsuario() == usuario and persona.getClave() == clave:
            print(f"Usuario {usuario} ha iniciado sesión como {type_of_persona}.")
            return

    print(f"Usuario {usuario} no se encontró en la colección de {type_of_persona}s.")


def print_list(collection, collection_name):
    if not collection:
        print(f"No {collection_name} para mostrar.")
    else:
        print(f"Lista de {collection_name}:")
        for idx, item in enumerate(collection, start=1):
            print(f"{idx}. {item}")


while True:
    print("\nMenu:")
    print("1. Insertar Empleado")
    print("2. Insertar Cliente")
    print("3. Iniciar sesión")
    print("4. Imprimir lista de Empleados")
    print("5. Imprimir lista de Clientes")
    print("6. Imprimir lista de Empleados por edad")
    print("7. Salir")

    choice = input("Seleccione una opción 1, 2, 3, 4, 5, 6, 7: ")

    if choice == '1':
        insert_empleado()
    elif choice == '2':
        insert_cliente()
    elif choice == '3':
        login()
    elif choice == '4':
        print_list(empleados, "Empleados")
    elif choice == '5':
        print_list(clientes, "Clientes")
    elif choice == '6':
        edad = int(input("Digite una edad: "))
        filtered_empleados = empleadosPorEdad(edad)
        for empleado in filtered_empleados:
            print(empleado)
    elif choice == '7':
        print("Salir")
        break
    else:
        print("Error, seleccione una opción entre 1 y 7.")
