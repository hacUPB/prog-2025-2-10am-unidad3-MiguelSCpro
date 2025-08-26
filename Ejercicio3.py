#Condicional Simple:
#Se le pide al usuario que ingrese un numero entero y que muestre un mensaje si el numero es divisible por 3.

numero = int(input("ingrese numero entero: "))
print(numero % 3)
if numero % 3 == 0:
    print("El numero es divisible entre 3")

