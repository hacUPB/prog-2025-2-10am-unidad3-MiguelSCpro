#calculadora

while True:
    num1 =int(input("ingrese un numero entero: "))
    num2 =int(input("ingrese otro numero entero: "))
    print("S. sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nP. Pontencia\nE. Salir")
    opcion = input("elija una opcion: ")
    opcion = opcion.upper()  #Se convierte el texto en mayuscula
    match opcion:
        case "S":
            print("Suma")
            resultado = num1 + num2
        case "R":
            print("Resta")
            resultado = num1 - num2
        case "M":
            print("Multiplicacion")
            resultado = num1 * num2
        case "D":
            if num2 == 0:
                resultado = "No se puede dividir"
            else:
                print("Division")
                resultado = num1 / num2
        case "P":
            print("Potenciacion")
            resultado = num1 ** num2
        case "E":
            break 
        case _:
            print("Opción inválida.")
    print(f"Resultado = {resultado}")
    
