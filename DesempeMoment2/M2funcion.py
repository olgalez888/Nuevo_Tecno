#funcion que recibe un parametro y lo imprime
def imprimir(a):
    print(a)

saludo="hola python"
imprimir(saludo)

#calcular masa corporal

def calcularImc(peso,estatura):
    imc=peso/(estatura*estatura)
    print(imc)

calcularImc(74,1.74)


#empleado

salario=1160000
def calcularSalud(salario):
    eps=salario*0.04
    return eps
    
def calcularPension(salario):
    pension=salario*0.04
    return pension


def calcularSalarioNeto(salario,eps,pension):
    salario_neto=salario-eps-pension
    print(salario_neto)

    eps=calcularSalud(salario)
    pension=calcularPension(salario)

    calcularSalarioNeto(salario,eps,pension) 


def calcularSalarioNeto2(salario,eps,pension):
        eps=calcularSalud(salario)
        pension=calcularPension(salario)
        salario_neto=salario-eps-pension
        print(salario_neto)

calcularSalarioNeto2(salario)

def registro(*items):
    print(f"los datos son:{items[:4]}")

    registro("pepito","perez",25,"pepito@mail.com")

def calcularPagoNomina(salario):
    pago_eps=lambda sal : salario*0.04
    pago_pension =lambda sal: salario*0.04
    salario_neto= salario-pago_eps(salario)-pago_pension
    print(salario_neto)

    calcularPagoNomina(1000000)
    
    #un callback es un llamado de funcion dentro de una funcion
    #una funcion lambda siempre sera una fn local, la estructura es la sgte
    # recibo el argumento y hago la operacion, todo eso en una variable que quedaron siendo funciones
    #pago=lambda salary: salaro*0.04, pago queda siendo una funcion, todo esto son los 
    #paradigmas de la prog funcional.


#EJERCICIO TAREA Y SUBIR A GITHUB
    #que inica sesion
    #bancolombia requiere calcular los salarios de su nueva start up pagui:
    #que pueda registrar id nombre apellido cargo area salario 
    #requiere calcular el salario neto de cada uno 
    # requiere listar a los empleados

    #requiere calcular el salario neto de cada uno, teniendo presente que 
    # se gana <2 salarios minimos se le paga aux de transporte

    #imprimir colilla de pago 

    # un empleado podra ingresar al sistema y buscar su colilla de pago e imprimirla

    #un analista de recursos humanos podra visualizar todos los empleados 
    # y todas las colillas ademas filtar, ademas buscar por empleado

    #que el de recursos humanos pueda ver el pago total nomina

    #el sistema solo debe ser llamado por una sola funcion
    #la fn menu llama la fn ppal de todo el programa que contiene las otras funciones
    #hacer callback y llamada de fn dentro de otra

#ejercicio callback

def imprimir(valor):
         print(valor)

    #def calcular_area(base, altura, callback):
    # return base*altura
    #nombre de la funcion que queremos
    # recibe el callback como argumento este scaso es imprimir

def calcular_area(base, altura, imprimir):#nombre de la funcion que queremos,
    # llamo la fn imprimir
 
    area = base*altura
    imprimir(area)
    base=50
    altura=5
    calcular_area(base, altura, imprimir)

















