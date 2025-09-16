'''
import repositoriofunciones

#Función principal
numero = int(input("Ingrese un número entero mayor que 1: "))
repositoriofunciones.primo(numero)
variable = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
repositoriofunciones.fibonacci(variable)
multiplicando = int(input("Ingrese el número entero: "))
repositoriofunciones.tabla(multiplicando)
'''
'''
from repositoriofunciones import *

primo(456)
tabla(9)
fibonacci(8)
'''
from modulos.repositoriofunciones import*

def main():
    while True:
        opc= menu()
        match opc:
                case 1:
                    print("calcula si un numero es primo")
                    valor = int(input("Ingresa un numero entero mayor que 1 >> "))
                    primo(valor)
                case 2:
                    print("Imprime la serie de Fibonacci")
                    num = int(input("Ingresa el numero de terminos >> "))
                    fibonacci(num)
                case 3:
                    print("Imprime la tabla de multiplicar")
                    num = int(input("Ingresa el numero entero >> "))
                    tabla(num)
                case 4:
                    break
                case _:
                    print("Intente de nuevo")

if __name__ =="__main__":
    main()

