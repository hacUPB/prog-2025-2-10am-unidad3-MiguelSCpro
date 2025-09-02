# Solicitar al usuario un número entero
Imprimir("Ingrese un número entero para generar la serie de Fibonacci:")
Leer(num)

# Verificar si el número ingresado es válido
Si num <= 0, entonces:
    Imprimir("Por favor, ingrese un número entero positivo.")
Sino si num == 1, entonces:
    Imprimir("Serie de Fibonacci:")
    Imprimir(0)
Sino:
    # Inicializar los primeros dos términos de la serie
    a = 0
    b = 1
    contador = 2  # Iniciar en 2 debido a los dos primeros términos ya impresos

    # Imprimir los primeros dos términos
    Imprimir("Serie de Fibonacci:")
    Imprimir(a)
    Imprimir(b)

    # Calcular e imprimir los términos restantes
    Mientras contador < num, hacer:
        siguiente = a + b
        Imprimir(siguiente)
        a = b
        b = siguiente
        contador += 1