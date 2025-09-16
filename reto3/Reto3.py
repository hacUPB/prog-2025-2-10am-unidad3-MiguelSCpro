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

    
    case "B":
        print("Cantidad de combustible...")
                
        rendimiento = float(input("Ingrese el rendimiento (km por litro): "))
        capacidad_tanque = float(input("Ingrese la capacidad del tanque (litros): "))
        combustible_tanque = capacidad_tanque

        vuelo = 1

        while True:
            print(f"\nVuelo {vuelo}")

            distancia = float(input("Ingrese la distancia del vuelo (km): "))
            velocidad = float(input("Ingrese la velocidad del avión (km/h): "))
            distancia_alterno = float(input("Ingrese la distancia al aeropuerto alterno (km): "))


            combustible_vuelo = distancia / rendimiento
            tiempo_vuelo = distancia / velocidad  # horas
            distancia_extra = velocidad * 1       # distancia para 1 hora extra
            combustible_extra = distancia_extra / rendimiento
            combustible_alterno = distancia_alterno / rendimiento

            combustible_necesario = combustible_vuelo + combustible_extra + combustible_alterno

            if combustible_necesario <= combustible_tanque:
                combustible_tanque -= combustible_vuelo
                print("Vuelo realizado.")
                print("Combustible restante en tanque:", round(combustible_tanque, 2), "litros")
            else:
                faltante = combustible_necesario - combustible_tanque
                print("No alcanza con el combustible actual.")
                print("Debe tanquear:", round(faltante, 2), "litros")
                # Reabastecer para completar vuelo
                combustible_tanque = capacidad_tanque - combustible_vuelo
                print("Vuelo realizado tras tanqueo.")
                print("Combustible restante:", round(combustible_tanque, 2), "litros")

            # Verificar si lo que sobra alcanza para un próximo destino
            opcion = input("¿Desea programar otro vuelo? (s/n): ").lower()
            if opcion != "s":
                print("El piloto decidió no programar más vuelos.")
                break

            vuelo += 1

        print("\n--- Fin de la simulación ---")

    case "C":
        print("Saliendo del programa...")
    case _:
        print("Opción inválida.")

        