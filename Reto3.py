print("=== MENÚ PRINCIPAL ===")
print("A. Peso de maletas")
print("B. Configurar parámetros")
print("C. Salir")


opcion = input("Selecciona una opción: ")


match opcion:
    case "A":
        print("Peso de maletas....")
        peso = 0
        peso_max = 23000
        while peso < peso_max :
            i=0
            peso = float(input("Ingrese peso en kg: "))
            if peso > 20:
                print("Maleta con sobrepeso")
            elif peso < 0:
                print("Inserte maleta a la bascula")
            else:
                print(f"Maleta aprovada, su peso es: {peso}Kg")
        i= peso + i
        peso_total=i
        print(f"El peso de carga de la aeronave es:{i} ")
        

    case "B":
        print("Entrando a configuración...")
    case "C":
        print("Saliendo del programa...")
    case _:
        print("Opción inválida.")