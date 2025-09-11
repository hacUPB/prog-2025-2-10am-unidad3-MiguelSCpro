print("=== MENÚ PRINCIPAL ===")
print("A. Peso de maletas")
print("B. Cantidad de pasajeros")
print("C. Salir")


opcion = input("Selecciona una opción: ").upper()


match opcion:
    case "A":
        print("Peso de maletas....")
        peso = 0
        peso_max = 23000
        i=0
        capacidad_bodega1 = 8000  # 
        capacidad_bodega2 = 10000  # 
        capacidad_bodega3 = 7500   # 
        bodega1 = 0
        bodega2 = 0
        bodega3 = 0
        while peso < peso_max :
            peso = float(input("Ingrese peso en kg: "))
            if peso > 20:
                print("Maleta con sobrepeso")
                costo = ((peso-20)*5)
                print(f"el costo de abordaje de la maleta es de: {costo}$")
            elif peso < 0:
                print("Inserte maleta a la bascula")
            else:
                print(f"Maleta aprovada, su peso es: {peso}Kg")
            i += peso
            peso_total = i
            espacio1 = capacidad_bodega1 - bodega1
            espacio2 = capacidad_bodega2 - bodega2
            espacio3 = capacidad_bodega3 - bodega3

            if peso <= max(espacio1, espacio2, espacio3):
                if espacio1 >= espacio2 and espacio1 >= espacio3:
                    bodega1 += peso
                    print(f"La maleta fue enviada a la Bodega 1. (Carga actual: {bodega1}/{capacidad_bodega1})")
                elif espacio2 >= espacio1 and espacio2 >= espacio3:
                    bodega2 += peso
                    print(f"La maleta fue enviada a la Bodega 2. (Carga actual: {bodega2}/{capacidad_bodega2})")
                else:
                    bodega3 += peso
                    print(f"La maleta fue enviada a la Bodega 3. (Carga actual: {bodega3}/{capacidad_bodega3})")
            else:
                print(" La maleta no cabe en ninguna bodega.")
            
            print(f"Estado bodegas -> B1: {bodega1}/{capacidad_bodega1}, B2: {bodega2}/{capacidad_bodega2}, B3: {bodega3}/{capacidad_bodega3}\n")

            '''
            if bodega1 + peso <= capacidad_bodega1:
                bodega1 += peso
                print(f"La maleta fue enviada a la Bodega 1. (Carga actual: {bodega1}/{capacidad_bodega1})")
            elif bodega2 + peso <= capacidad_bodega2:
                bodega2 += peso
                print(f"La maleta fue enviada a la Bodega 2. (Carga actual: {bodega2}/{capacidad_bodega2})")

            elif bodega3 + peso <= capacidad_bodega3:
                bodega3 += peso
                print(f"La maleta fue enviada a la Bodega 3. (Carga actual: {bodega3}/{capacidad_bodega3})")
            else:
                print("La maleta no cabe en ninguna bodega.")

            print(f"Estado bodegas -> B1: {bodega1}/{capacidad_bodega1}, B2: {bodega2}/{capacidad_bodega2}, B3: {bodega3}/{capacidad_bodega3}\n")
'''
    
    case "B":
        print("Cantidad de pasajeros...")
    case "C":
        print("Saliendo del programa...")
    case _:
        print("Opción inválida.")

        