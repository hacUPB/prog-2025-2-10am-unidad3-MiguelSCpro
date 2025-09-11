def menu():
    print("1. entradas\n2. platos fuertes\n3. Bebidas\n4. postres\n5. salida")
    opcion = int(input("Elija una opcion: "))
    return opcion

def entradas():
    print("1. pan de bono\t\t $3000")
    print("2. empanada\t\t $3500")

def fuertes():
    print("1. mojarra a la francesa\t $80000")
    print("2. pasta venezolana\t\t $45000")

def bebidas():
    print("1. jugo de carambolo\t\t $15000")
    print("2. jugo de borojó\t\t $15000")

def postres():
    print("1. helado tres leches\t\t $12000")
    print("2. flan de caramelo\t\t $10000")

# Funcion principal
eleccion = menu()
print(eleccion)

match eleccion:
    case 1:
        entradas()
    case 2:
        fuertes()
    case 3:
        bebidas()
    case 4:
        postres()
    case _:
        print("Opción no válida")

if __name__== "__main__":
    menu()
