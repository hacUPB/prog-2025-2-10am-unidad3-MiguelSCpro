#Determinar si el numero es par i impar
numero = int(input("ingrese un numero entero: "))
residuo = numero % 2
#Si residuo 0 es par
if residuo == 0: 
    print(numero, "es par")
#si no es par
else:
    print (numero, "es impar")


