import random


def solicitar_n() -> int:
    """
    Solicita y valida el valor de n para generar una matriz de n x n.
    """

    while True:
        try:
            num = input("Ingrese el tamaño n de la matriz: ")
            n = int(num)

            if n > 0:
                return n
            else:
                print("n debe ser un entero positivo.")

        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")


def rellenar_matriz_sin_repeticion(n: int) -> list[list[int]]:
    """
    Genera una matriz n x n rellenada con números enteros aleatorios
    del intervalo [0, N**2) sin que ninguno se repita.
    """
    if n <= 0:
        return []

    total_elementos = n * n

    numeros_unicos = list(range(total_elementos))

    random.shuffle(numeros_unicos)

    matriz = []
    ind_secuencia = 0

    for i in range(n):
        fila = []
        for j in range(n):

            fila.append(numeros_unicos[ind_secuencia])
            ind_secuencia += 1
        matriz.append(fila)

    return matriz


def imprimir_matriz(matriz: list[list[int]], n: int) -> None:
    """
    Esta función imprime por pantalla la matriz generada de forma alineada.
    """
    print(f"\nMatriz Aleatoria sin Repetición de {n} x {n}: ")

    ancho = len(str(n * n - 1)) + 1

    for fila in matriz:
        linea = "".join(f"{elemento:>{ancho}}" for elemento in fila)
        print(linea)
    print("-" * 50)


# --- Programa Principal (Invocación) ---

if __name__ == '__main__':
    n = solicitar_n()

    matriz_aleatoria = rellenar_matriz_sin_repeticion(n)

    imprimir_matriz(matriz_aleatoria, n)
