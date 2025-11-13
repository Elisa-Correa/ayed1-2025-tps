import math


def solicitar_n() -> None:
    """
    Solicita y verifica que el valor de n,para generar una matriz de n x n.
    y valida que n sea un numero valido.
    """

    while True:
        try:
            entrada = input("Ingrese el tamaño n de la matriz: ")
            n = int(entrada)
            if n > 0:
                return n
            else:
                print("n debe ser un entero positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")


def imprimir_matriz(matriz: list[list[int]], n: int) -> None:
    """
    Esta funcion imprime por pantalla la matriz generada 
    """
    print(f"\nMatriz_a de {n} x {n} generada:")
    for fila in matriz:
        print(fila)
    print("-" * 30)


def funcion_a(n: int) -> list[list[int]]:
    """
    Etsa funcion genera una matriz de n x n con ceros y la secuencia 1, 3, 5, 7... 
    en la diagonal principal.

    Pre:

    - Recibe n como un numero entero positivo.

    Post:

    - Imprime por pantalla la secuencia 1, 3, 5, 7, etc. en la diagonal principal.
    """

    if n <= 0:
        return []

    matriz = [[(2 * i + 1) if i == j else 0 for j in range(n)]
              for i in range(n)]

    return matriz


def funcion_b(n: int) -> list[list[int]]:
    """
    Esta funcion genera una matriz de n x n con potencias de 3 en la diagonal secundaria
    (donde i + j = N - 1).

    Pre:

    - Recibe n como un numero entero positivo.

    Post: Imprime por pantalla la matriz con potencias de 3 en la diagonal secundaria.
    """

    if n <= 0:
        return []

    matriz = [[(3 ** (n - 1 - i)) if i + j == n -
               1 else 0 for j in range(n)] for i in range(n)]
    return matriz


def funcion_c(n: int) -> list[list[int]]:
    """
    Esta funcion genera una matriz de n x n triangular inferior. 
    Cada fila 'i' se rellena con el valor N - i.
    """
    if n <= 0:
        return []

    matriz = [[(n - i) if j <= i else 0 for j in range(n)] for i in range(n)]
    return matriz


def funcion_d(n: int) -> list[list[int]]:
    """
    Esta funcion genera una matriz de n x n donde cada fila i está rellena con 
    la potencia de 2: 2^(n - 1 - i).
    """
    if n <= 0:
        return []

    matriz = [[2 ** (n - 1 - i) for j in range(n)] for i in range(n)]
    return matriz


def funcion_e(n: int) -> list[list[int]]:
    """
    Esta funcion genera una matriz de n x n con ceros en posiciones pares (i+j par) 
    y una secuencia ascendente de números en posiciones impares (i+j impar).
    """

    if n <= 0:
        return []

    matriz = []

    for i in range(n):
        fila = []

        for j in range(n):

            if (i + j) % 2 != 0:
                posicion_lineal = (i * n) + j

                valor = math.ceil((posicion_lineal + 1) / 2)
                fila.append(int(valor))

            else:
                fila.append(0)

        matriz.append(fila)

    return matriz


def funcion_g(n: int) -> list[list[int]]:
    """
    Esta funcion genera una matriz de n x n con un relleno en espiral (caracol) clásico,
    comenzando en 1 y terminando en n*n.
    """

    if n <= 0:
        return []

    matriz = [[0] * n for _ in range(n)]
    num = 1

    # Coordenadas de inicio/fin para los límites de la capa exterior
    top, bottom, left, right = 0, n - 1, 0, n - 1

    while num <= n * n:
        # Movimiento Derecha (Fila superior)
        for j in range(left, right + 1):
            if num > n * n:
                break
            matriz[top][j] = num
            num += 1
        top += 1

        # Movimiento Abajo (Columna derecha)
        for i in range(top, bottom + 1):
            if num > n * n:
                break
            matriz[i][right] = num
            num += 1
        right -= 1

        # Movimiento Izquierda (Fila inferior, si es necesario)
        if top <= bottom:
            for j in range(right, left - 1, -1):
                if num > n * n:
                    break
                matriz[bottom][j] = num
                num += 1
            bottom -= 1

        # Movimiento Arriba (Columna izquierda, si es necesario)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                if num > n * n:
                    break
                matriz[i][left] = num
                num += 1
            left += 1

    return matriz

# Menu -----------------------------------------------------------------------------------------------


def guion():
    print("-"*60)


def mostrar_opc():
    op = ["Diagonal Principal Impar", "Diagonal Secundaria con Potencias de 3", "Triangular Inferior Decreciente por Fila",
          "Potencia de 2 por Fila Completa", "Patrón de Ajedrez (Impar)", "Espiral Horario (Caracol Clásico)"]
    letras = "abcdeg"

    for l, o in zip(letras, op):
        print(f"{l}. {o}")


def menu():

    while True:
        mostrar_opc()
        opcion = input("Ingrese una opción (salir): ")

        if opcion == "salir":
            print("Finalizo el programa...")
            break

        elif opcion == "a":
            n = solicitar_n()

            matriz_a = funcion_a(n)

            imprimir_matriz(matriz_a, n)

        elif opcion == "b":
            n = solicitar_n()

            matriz_b = funcion_b(n)

            imprimir_matriz(matriz_b, n)

        elif opcion == "c":
            n = solicitar_n()

            matriz_c = funcion_c(n)

            imprimir_matriz(matriz_c, n)

        elif opcion == "d":
            n = solicitar_n()

            matriz_d = funcion_d(n)

            imprimir_matriz(matriz_d, n)

        elif opcion == "e":
            n = solicitar_n()

            matriz_e = funcion_e(n)

            imprimir_matriz(matriz_e, n)

        elif opcion == "g":
            n = solicitar_n()

            matriz_g = funcion_g(n)

            imprimir_matriz(matriz_g, n)

        else:
            print("\nERROR - la opcion ingresada es invalida, intente denuevo")


menu()
