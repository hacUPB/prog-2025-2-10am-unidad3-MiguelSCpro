nombre = input("ingresa tu nombre y apellido: ")
#Opcion 2
print ("Bienvenido: ",nombre)
#Calcular el IMC de esa persona
#Leer peso, altura
peso = input ("ingresa tu peso en kilo gramos: ")
peso= float(peso) 
altura= input ("ingresa tu altura en metros: ")
altura= float(altura)
#calculos
imc= peso/altura**2
#mostrar imc
print ("Tu IMC = ", imc)
#Si el IMC es menor a 18.5
if imc < 18.5:
    print("Estas bajo de peso")
#Si el IMC es entre 18.5 y 24.9
if imc >= 18.5 and imc <= 24.9:
    print("Tu peso es normal")
#Si el IMC es entre 25 y 29.9
if imc >= 25 and imc <= 29.9:
    print("Tienes sobrepeso")
#Si el IMC es mayor a 30 y 34.9
if imc > 30 and imc <= 34.9:
    print("Tienes obesidad 1")
#Si el IMC es mayor a 35 y 39.9
if imc >= 35 and imc <=39.9:
    print("Tienes obesidad 2")
#Si el IMC es mayor a 40
if imc >= 40:
    print("Tienes obesidad 3 ")





