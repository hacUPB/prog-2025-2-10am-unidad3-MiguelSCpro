print("=== MENÚ PRINCIPAL ===")
print("A. Peso de maletas")
print("B. Cantidad de pasajeros")
print("C. Solución Drag")
print("D. Salir")


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

                # Datos iniciales
        rendimiento = float(input("Ingrese el rendimiento (km por litro): "))
        capacidad_tanque = float(input("Ingrese la capacidad del tanque (litros): "))
        combustible_tanque = capacidad_tanque

        vuelo = 1

        while True:
                    print(f"\n Vuelo {vuelo}")

                    distancia = float(input("Ingrese la distancia del vuelo (km): "))
                    velocidad = float(input("Ingrese la velocidad del avión (km/h): "))
                    distancia_alterno = float(input("Ingrese la distancia al aeropuerto alterno (km): "))

                    combustible_vuelo = distancia / rendimiento
                    tiempo_vuelo = distancia / velocidad  
                    distancia_extra = velocidad * 1       
                    combustible_extra = distancia_extra / rendimiento
                    combustible_alterno = distancia_alterno / rendimiento

                   
                    combustible_necesario = combustible_vuelo + combustible_extra + combustible_alterno

                    print(f" Combustible requerido para este vuelo: {round(combustible_necesario,2)} litros")
                    print(f" - Vuelo: {round(combustible_vuelo,2)} L")
                    print(f" - Extra (1h): {round(combustible_extra,2)} L")
                    print(f" - Alterno: {round(combustible_alterno,2)} L")

                    
                    if combustible_necesario <= combustible_tanque:
                        combustible_tanque -= combustible_necesario
                        print(" Vuelo realizado con seguridad.")
                        print("Combustible restante en tanque:", round(combustible_tanque, 2), "litros")
                    else:
                        faltante = combustible_necesario - combustible_tanque
                        print(" No alcanza con el combustible actual.")
                        if combustible_necesario <= capacidad_tanque:
                            print("Debe tanquear:", round(faltante, 2), "litros")
                            combustible_tanque = capacidad_tanque - combustible_necesario
                            print("Vuelo realizado tras tanqueo.")
                            print("Combustible restante:", round(combustible_tanque, 2), "litros")
                        else:
                            print(" El combustible requerido excede la capacidad del tanque.")
                            print(f"Capacidad máxima: {capacidad_tanque} L, requerido: {round(combustible_necesario,2)} L")
                            break

                    if combustible_tanque <= 0:
                        print(" No queda combustible suficiente para programar otro vuelo.")
                        break

                    opcion = input("¿Desea programar otro vuelo? (s/n): ").lower()
                    if opcion != "s":
                        print("El piloto decidió no programar más vuelos.")
                        break

                    vuelo += 1

    case "C":
        print("velocidad del despegue")

        densidad = float(input("Ingrese la densidad del aire (kg/m³): "))
        area_frontal = float(input("Ingrese el área frontal del avión (m²): "))
        coef_arrastre = float(input("Ingrese el coeficiente de arrastre (CD): "))
        vel_inicial = float(input("Ingrese la velocidad inicial (m/s): "))
        vel_final = float(input("Ingrese la velocidad final (m/s): "))
        incremento_vel = float(input("Ingrese el incremento de velocidad (m/s): "))
        umbral_critico = float(input("Ingrese el umbral crítico de resistencia (N): "))

        velocidad = vel_inicial
        i = 1

        while velocidad <= vel_final:
        
            drag = 0.5 * densidad * (velocidad ** 2) * area_frontal * coef_arrastre
        
            if drag <= umbral_critico:
                mensaje_estado = "Seguro"
            else:
                mensaje_estado = "peligro"
            
            print(f"\nIteración {i}")
            print(f"Velocidad: {velocidad:.2f} m/s")
            print(f"Resistencia (Drag): {drag:.2f} N")
            print(f"Estado: {mensaje_estado}")

            velocidad += incremento_vel
            i += 1

    case "D":
        print("Saliendo del programa...")
    case _:
        print("Opción inválida.")

        