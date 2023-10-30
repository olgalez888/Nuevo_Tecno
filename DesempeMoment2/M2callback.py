#EJERCICIO DE NOMINA
salario=float(input("ingrese el valor del salario: "))
def aux_trans(salario, pago_neto):
    if (salario<=2320000): 
         print(f"salario neto:{pago_neto + 140606}")
    else:
        print(f"salario neto:{pago_neto}") 

"""
def pago_neto(salario, aux_trans):
     eps=salario*0.04
     pension=salario*0.04
     pago_neto=salario-eps-pension
     aux_trans(pago_neto)"""

# con lambda
def pago_neto(salario, aux_trans):
     eps=lambda salario: salario*0.04 #eps se convierte en un metodo, no variable
     pension=lambda salario: salario*0.04
     pago_neto=salario-eps(salario)-pension(salario)
     aux_trans(salario,pago_neto)

pago_neto(salario, aux_trans)