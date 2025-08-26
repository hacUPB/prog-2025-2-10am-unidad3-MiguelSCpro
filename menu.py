#2

print("=== MENÚ PRINCIPAL ===")
print("A. Ver datos de sensores")
print("B. Configurar parámetros")
print("C. Salir")


opcion = input("Selecciona una opción: ")

match opcion:
    case "A":
        print("Mostrando datos de sensores...")
    case "B":
        print("Entrando a configuración...")
    case "C":
        print("Saliendo del programa...")
    case _:
        print("Opción inválida.")