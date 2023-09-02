nombreUsuario=""
EmailUsuario=""
passwordUsuario=""
codigoCaptcha=456
opc = 0
while opc < 3:

    opc = int(input("1. Registro\n 2. Login \n 3. Salir"))

    if opc == 1:
        print("Registro")
        nombreUsuario=input("Ingrese nombre usuario")
        EmailUsuario=input("Ingrese correo del usuario")
        passwordUsuario=input("Ingrese contraseña")
        print("Usuario ingresado")

    elif opc == 2: 
        print("Login")
        EmailUser=input("Ingrese correo")
        passwordUser=input("Ingrese contraseña")

        if EmailUsuario == "" or passwordUsuario == "":
            print("Primero debe registrarse")
        elif EmailUsuario == EmailUser and passwordUsuario ==passwordUser and codigoCaptcha==456:

            print("Email y contraseña validos")
            print("compras")
            valorCompra=int(input("ingrese el valor compra"))
            nroCuotas=int(input("ingrese las cuotas"))
            valorCuota=valorCompra/nroCuotas
            cuotActual=0
            saldoActual=valorCompra
            while cuotActual<nroCuotas:
                cuotActual+=1
                saldoActual-=valorCuota
                print("cuota",cuotActual,"=",valorCuota, " saldo: ", saldoActual)

        else:
            print("Email y contraseña invalidos")

    elif opc == 3: 
        print("salir")

    else:
        print("Seleccione una opcion Valida")  