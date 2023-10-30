#CONJUNTOS
#son inmutables, son desordenados osea que cuando se llama no se tiene certeza
#el orden en que los mostrara
#sin orden especifico porque no son indexados, no podemos acceder print(vocales[1]) 
#No permite duplicados

vocales={"a","e","i","o","u"}
print(len(vocales))
print(type(vocales))

#print(vocales[0])#no podemos acceder, no hay indices 

#para recorrer los conjuntos se usa in
for i in vocales:
    print(vocales)
print("-------------")

for i in vocales:
    print(vocales)
print("-------------")

for i in vocales:
    print(vocales)

#los conjuntos tienen el metodo add y el metodo remove

vocales.add("@")

for i in vocales:
    print(vocales)

#podemos remover
vocales.remove("@")

for i in vocales:
    print(vocales)

vocales.pop()  

