#bancolombia requiere calcular los salarios de su nueva start up pagui:
#Que inicia sesion
#que pueda registrar id nombre apellido cargo area salario 

listaEmpleados = []
sesionIniciada = False
idUsuarioIniciado = 0
perfil = ""

def registrarEmpleado():
    print("Registro de empleado")
    idUsuario=int(input("Ingrese id usuario: "))
    contrasena=input("Ingrese contraseña: ")
    nombreUsuario=input("Ingrese nombre usuario: ")
    apellidoUsuario=input("Ingrese apellido usuario: ")
    cargoUsuario=input("Ingrese cargo usuario: ")
    areausuario=input("Ingrese area usuario: ")
    salarioUsuario=int(input("Ingrese salario usuario: "))
    registro=idUsuario, contrasena, nombreUsuario, apellidoUsuario, cargoUsuario, areausuario, salarioUsuario
    listaEmpleados.append(registro)
    return registro

def iniciarSesion():
    idUsuario=int(input("Ingrese id usuario: "))
    contrasena=input("Ingrese contraseña: ")
    global sesionIniciada
    global perfil
    global idUsuarioIniciado
    sesionIniciada = False
    perfil = ""
    idUsuarioIniciado = 0
    for empleado in listaEmpleados:
        if idUsuario == empleado[0] and contrasena == empleado[1]:
            print("Sesion iniciada")
            sesionIniciada = True
            perfil = empleado[4]
            idUsuarioIniciado = empleado[0]
            return
    print("No se encontró el usuario")


#requiere calcular el salario neto de cada uno 

def calcularSalud(salarioUsuario):
    eps=salarioUsuario*0.08
    return eps
    
def calcularPension(salarioUsuario):
    pension=salarioUsuario*0.04
    return pension

#requiere calcular el salario neto de cada uno, teniendo presente que 
    # se gana <2 salarios minimos se le paga aux de transporte

def calcularSalarioNeto(salarioUsuario,eps,pension):
    if (salarioUsuario<=2320000): 
         salarioUsuario_neto=salarioUsuario-eps-pension
    else:
        salarioUsuario_neto=salarioUsuario-eps-pension
    return salarioUsuario_neto

def imprimirColilla():
    if not sesionIniciada:
        print("Primero inicie sesion")
        return
    if perfil == "RecursosHuman":
        idUsuario = int(input("Digite el id del usuario o 0 para todos: "))
        for empleado in listaEmpleados:
            if idUsuario == 0 or idUsuario == empleado[0]:
                imprimirColillaEmpleado(empleado)
    else:
        for empleado in listaEmpleados:
            if idUsuarioIniciado == empleado[0]:
                imprimirColillaEmpleado(empleado)

def imprimirColillaEmpleado(empleado):
    print("---------------------------------------------")
    print(empleado[2] + " " + empleado[3])
    salud=calcularSalud(empleado[6])
    print("Salud es: ",salud)
    pension=calcularPension(empleado[6])
    print("Pension es: ",pension)
    neto=calcularSalarioNeto(empleado[6], salud, pension)
    print("Salario neto es: ",neto)
    print("Salario total es: ", empleado[6])

def imrpimirEmpleados():
    if not sesionIniciada:
        print("Primero inicie sesion")
        return
    if perfil == "RecursosHuman":
        idUsuario = int(input("Digite el id del usuario o 0 para todos: "))
        for empleado in listaEmpleados:
            if idUsuario == 0 or idUsuario == empleado[0]:
                print(empleado)
    else:
        for empleado in listaEmpleados:
            if idUsuarioIniciado == empleado[0]:
                print(empleado)

def verPagoTotalNomina():
    if not sesionIniciada:
        print("Primero inicie sesion")
        return
    pagoTotal = 0
    if perfil == "RecursosHuman":
        for empleado in listaEmpleados:
            pagoTotal = pagoTotal + empleado[6]
        print(f"El pago total es: {pagoTotal}")
    else:
        print("Opcion no disponible")

def menu():
    while True:
        print("\nMenu:")
        print("1. Registrar Empleado")
        print("2. Iniciar sesión")
        print("3. Imprimir Colilla")
        print("4. Imprimir lista de Empleados")
        print("5. Imprimir pago total nomina")
        print("6. Salir")    

        choice = input("Seleccione una opción 1, 2, 3, 4, 5, 6: ")

        if choice == '1':
            registrarEmpleado()
        elif choice == '2':
            iniciarSesion()
        elif choice == '3':
            imprimirColilla()
        elif choice == '4':
            imrpimirEmpleados()
        elif choice == '5':
            verPagoTotalNomina()
        elif choice == '6':
            print("Salir")
            break
        else:
            print("Error, seleccione una opción entre 1 y 6.")

# menu
menu()


# un empleado podra ingresar al sistema y buscar su colilla de pago e imprimirla

# un analista de recursos humanos podra visualizar todos los empleados 
# y todas las colillas ademas filtar, ademas buscar por empleado, pueda ver el pago total nomina

# el sistema solo debe ser llamado por una sola funcion
# la fn menu llama la fn ppal de todo el programa que contiene las otras funciones
# hacer callback y llamada de fn dentro de otra