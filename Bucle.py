numero = 1
while numero <= 100:
    print(numero)
    numero += 2
numero= 100
while numero >=0:
    print(numero)
    numero -= 5


#solicitar 2 numeros al usuario e imprimir los pares
#entre ellos

num1 =int(input("ingrese un numero entero: "))
num2 =int(input("ingrese otro numero entero: "))

if num1 > num2:
    mayor = num1
    menor = num2
else:
    mayor = num2
    menor = num1

while menor <= mayor:
    if menor % 2 == 0:
        print(menor)
    menor += 1
    


    
