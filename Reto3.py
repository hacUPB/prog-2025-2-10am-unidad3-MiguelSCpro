print("=== MENÚ PRINCIPAL ===")
print("A. Peso de maletas")
print("B. Configurar parámetros")
print("C. Salir")


opcion = input("Selecciona una opción: ").upper()


match opcion:
    case "A":
        print("Peso de maletas....")
        peso = 0
        peso_max = 23000
        i=0
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
            peso_total=i
            print(f"El peso de carga de la aeronave es:{i} ")
        

    case "B":
        print("Entrando a configuración...")
    case "C":
        print("Saliendo del programa...")
    case _:
        print("Opción inválida.")