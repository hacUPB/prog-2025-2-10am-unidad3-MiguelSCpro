while True:

    print("=== MENÚ PRINCIPAL ===")
    print("A. Peso de maletas")
    print("B. Cantidad de combustible")
    print("C. Solución Drag")
    print("D. Salir")


    opcion = input("Selecciona una opción: ").upper()


    match opcion:
        case "A":
            print("Sistema de control de maletas y bodegas ")

            def calcular_costo(peso): #Definicion de la función
                if peso > 20:
                    return (peso - 20) * 5
                return 0

            def asignar_bodega(peso, b1, b2, b3, cap1, cap2, cap3):#definicion de la funcion
                espacio1 = cap1 - b1
                espacio2 = cap2 - b2
                espacio3 = cap3 - b3

                if peso <= max(espacio1, espacio2, espacio3):
                    if espacio1 >= espacio2 and espacio1 >= espacio3:
                        b1 += peso
                        print(f"La maleta fue enviada a la Bodega 1. (Carga actual: {b1}/{cap1})")
                    elif espacio2 >= espacio1 and espacio2 >= espacio3:
                        b2 += peso
                        print(f"La maleta fue enviada a la Bodega 2. (Carga actual: {b2}/{cap2})")
                    else:
                        b3 += peso
                        print(f"La maleta fue enviada a la Bodega 3. (Carga actual: {b3}/{cap3})")
                else:
                    print("La maleta no cabe en ninguna bodega.")
                
                return b1, b2, b3

            def mostrar_estado(b1, b2, b3, cap1, cap2, cap3):#definicion de la funcion
                print(f"Estado bodegas -> B1: {b1}/{cap1}, B2: {b2}/{cap2}, B3: {b3}/{cap3}\n")

           
            peso_max = 23000 #Valor que se puede sustituir
            capacidad_bodega1 = 8000 #Valor que se puede sustituir
            capacidad_bodega2 = 10000 #Valor que se puede sustituir
            capacidad_bodega3 = 7500 #Valor que se puede sustituir
            bodega1 = bodega2 = bodega3 = 0
            peso_total = 0

            while peso_total < peso_max:
                peso = float(input("Ingrese peso en kg: "))

                if peso < 0:
                    print("Inserte maleta a la báscula")
                    continue
                
                costo = calcular_costo(peso)
                if costo > 0:
                    print(f"Maleta con sobrepeso. Costo adicional: {costo}$")
                else:
                    print(f"Maleta aprobada, su peso es: {peso}Kg")

                peso_total += peso
                bodega1, bodega2, bodega3 = asignar_bodega(peso, bodega1, bodega2, bodega3,
                    capacidad_bodega1, capacidad_bodega2, capacidad_bodega3)
                mostrar_estado(bodega1, bodega2, bodega3,capacidad_bodega1, capacidad_bodega2, capacidad_bodega3)

                opcion = input("¿Desea seguir pesando? (s/n): ").lower()#lower para pasar a minusculas
                if opcion != "s":
                    print("Se acabó el programa.")
                    break



        
        case "B":
            print("Cantidad de combustible...")

            # 🔹 Definimos la función
            def calcular_combustible(distancia, velocidad, distancia_alterno, rendimiento):#Definicion de la funcion
                """
                Calcula el combustible necesario para un vuelo considerando:
                - Vuelo hasta el destino
                - 1 hora extra de vuelo
                - Vuelo al aeropuerto alterno
                """
                combustible_vuelo = distancia / rendimiento
                distancia_extra = velocidad * 1
                combustible_extra = distancia_extra / rendimiento
                combustible_alterno = distancia_alterno / rendimiento

                combustible_necesario = combustible_vuelo + combustible_extra + combustible_alterno
                return combustible_necesario, combustible_vuelo, combustible_extra, combustible_alterno


            # Entradas iniciales
            rendimiento = float(input("Ingrese el rendimiento (km por litro): "))
            capacidad_tanque = float(input("Ingrese la capacidad del tanque (litros): "))
            combustible_tanque = capacidad_tanque

            vuelo = 1

            while True:
                print(f"\n Vuelo {vuelo}")

                distancia = float(input("Ingrese la distancia del vuelo (km): "))
                velocidad = float(input("Ingrese la velocidad del avión (km/h): "))
                distancia_alterno = float(input("Ingrese la distancia al aeropuerto alterno (km): "))

                
                combustible_necesario, combustible_vuelo, combustible_extra, combustible_alterno = calcular_combustible(distancia, velocidad, distancia_alterno, rendimiento)

                print(f" Combustible requerido para este vuelo: {round(combustible_necesario, 2)} litros")
                print(f" Vuelo: {round(combustible_vuelo, 2)} L")
                print(f" Extra (1h): {round(combustible_extra, 2)} L")
                print(f" Alterno: {round(combustible_alterno, 2)} L")

                if combustible_necesario <= combustible_tanque:
                    combustible_tanque -= combustible_necesario
                    print(" Vuelo realizado con seguridad.")
                    print(" Combustible restante en tanque:", round(combustible_tanque, 2), "litros")
                else:
                    faltante = combustible_necesario - combustible_tanque
                    print(" No alcanza con el combustible actual.")
                    if combustible_necesario <= capacidad_tanque:
                        print(" Debe tanquear:", round(faltante, 2), "litros")
                        combustible_tanque = capacidad_tanque - combustible_necesario
                        print(" Vuelo realizado tras tanqueo.")
                        print(" Combustible restante:", round(combustible_tanque, 2), "litros")
                    else:
                        print(" El combustible requerido excede la capacidad del tanque.")
                        print(f" Capacidad máxima: {capacidad_tanque} L, requerido: {round(combustible_necesario, 2)} L")
                        break

                if combustible_tanque <= 0:
                    print(" No queda combustible suficiente para programar otro vuelo.")
                    break

                opcion = input("¿Desea programar otro vuelo? (s/n): ").lower()
                if opcion != "s":
                    print(" El piloto decidió no programar más vuelos.")
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
    break

        