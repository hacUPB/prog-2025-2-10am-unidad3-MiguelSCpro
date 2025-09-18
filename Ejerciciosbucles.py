### Ejercicio 1: Conversor de Temperatura

#**Dificultad:** Principiante

#Crea un programa que convierta temperaturas entre Celsius y Fahrenheit. El programa debe:

#1. Preguntar al usuario si desea convertir de Celsius a Fahrenheit (ingresando 'C') o de Fahrenheit a Celsius (ingresando 'F')
#2. Aceptar un valor de temperatura como entrada
#3. Realizar la conversión usando la fórmula apropiada
#4. Continuar pidiendo conversiones hasta que el usuario ingrese 'Q' para salir

#**Entrada:** Un carácter ('C', 'F', o 'Q') y un valor numérico de temperatura
#**Salida:** El valor de temperatura convertido con las unidades correspondientes

'''
Variables de entrada
Nombre          tipo
opcion          str
temperatura     float

variables de salida
Nombre          Tipo
conversacion    float

variables de control
opcion 
'''
'''
opcion = "Z"                        #Asigno un valor diferente a Q
while opcion != "Q":
    opcion = input("F. Fahrenheit a celcius\nC. Celcius a Fahrenheit\nQ. Salir\n").upper()
    if opcion != "Q":
        temperatura = float(input("Ingrese la temperatura a convertir:  "))  
        match opcion:
            case "F":
                conversion = ((temperatura - 32) *(5/9))
                print(f"{temperatura}°F = {conversion}°C")
            case "C.":
                conversion = (temperatura*9/5) + 32
                print(f"{temperatura}°C = {conversion}°F")
            case _:
                print("opcion no válida")

    else:
        print("Saliendo del programa...")
'''
### Ejercicio 8: Verificador de Números Primos

#**Dificultad:** Intermedio

#Implementa un programa que determine si un número es primo y, en caso de no serlo, muestre sus factores. El programa debe:

#1. Solicitar al usuario un número entero positivo mayor que 1
#2. Determinar si el número es primo
#3. Si no es primo, mostrar todos sus factores
#4. Permitir al usuario verificar múltiples números

#**Entrada:** Un número entero positivo
#**Salida:** Mensaje indicando si el número es primo o no, y sus factores si corresponde

'''
Variable de entrada 
numero      int

Variable de salida
divisores
'''
numero= int(input("Ingrese un numero entero mayor que 1:  "))
if numero > 1:
    cont = 0
    for i in range (1, numero + 1):
        if numero % i == 0:
            cont += 1

    if cont == 2:
        print(f"{numero} es primo")
    else:
        print(f"Los divisores de {numero} son:")
        for i in range (1, numero + 1):
            if numero % i == 0:
                    print(i)
else:
    print(f"Lea que ahi dice un numero mayor que uno, {numero} es menor, aprenda a leer")
