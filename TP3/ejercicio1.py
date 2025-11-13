# Opción a -----------------------------------------------------------------------------------
def crear_matriz(filas: int, columnas: int) -> list[list[int]]:
    matriz = []
    for i in range(filas):
        matriz.append([])

        for j in range(columnas):
            matriz[i].append(0)
    return matriz


def cargar_datos(matriz: list[list[int]]) -> list[list[int]]:
    """
    Pre: Recibe una matriz cargada con ceros.

    Post: Devuelve una matriz cargada con los números que ingrese el usuario.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            while True:
                num = input(
                    f"Ingresa un número para la fila: {i} y columna: {j}: ")

                try:
                    num = int(num)
                    matriz[i][j] = num
                    break

                except ValueError:
                    print("El valor ingresado no es un número, intenta denuevo")


# Extra ________________________________________________________________________________________

def copiar_matriz(matriz: list[list[int]]) -> list[list[int]]:
    """
    Pre:
        - Recibe una matriz cargada de numeros enteros.
        - Las listas internas (filas) deben tener la misma longitud.

    Post:
        - Devuelve una copia de la matriz ingresada como parametro.
    """
    matriz_copia = [fila[:] for fila in matriz]
    return matriz_copia


def validar_rango(a, b, dato):
    """
    Pre:
        - Recibe a y b como limites del rango en donde se evaluara si el dato se encuentra entre los mismos limites.
        - Recibe dato, como elemento a evaluar entre el limite a y b.
        - a, b y dato: son enteros positivos.

    Post:

        - Retorna True en caso de que el dato se encuentre entre el limite a y b.
        - Retorna False en caso contrario.
    """

    if a < b:
        if dato >= a and dato <= b:
            return True
        return False

    else:
        if dato >= b and dato <= a:
            return True
        return False

# Opción b ---------------------------------------------------------------------------------


def ordenar_filas_asc(matriz: list[list[int]]) -> list[list[int]]:
    """
    Pre:
        - Recibe una matriz con datos ya cargados de números enteros
        - Las listas internas (filas) deben tener la misma longitud.

    Post:
        - Devuelve una Matriz donde cada fila esta ordenada de forma ASCENDENTE.
    """
    matriz_ord = [sorted(fila) for fila in matriz]
    print(matriz_ord)
    return matriz_ord


# Opción c ------------------------------------------------------------------------------------
def intercambiar_filas(a: int, b: int, matriz: list[list[int]]) -> list[list[int]]:
    """
    Pre:
        - Recibe como parametro 2 números enteros que representan el números de las 2 filas que se desea sean intercambiadas.
        - a y b son los números enteros.

    Post:
        - Devuelve una matriz con las filas seleccionadas intercambiadas.
    """

    copia_matriz = copiar_matriz(matriz)
    copia_matriz[a], copia_matriz[b] = copia_matriz[b], copia_matriz[a]

    return copia_matriz

# Opción d ------------------------------------------------------------------------------------


def intercambiar_columnas(columna_a: int, columna_b: int, matriz: list[list[int]]) -> list[list[int]]:
    """
    Pre:
        - Recibe los índices de las dos columnas a intercambiar (columna_a y columna_b).
        - Recibe una matriz de números enteros.

    Post:
        - Devuelve una nueva matriz con la columna_a y columna_b intercambiadas.
    """
    copia_matriz = copiar_matriz(matriz)

    for fila in copia_matriz:
        fila[columna_a], fila[columna_b] = fila[columna_b], fila[columna_a]

    return copia_matriz


# Opción e -----------------------------------------------------------------------------------------
def transponer_matriz(matriz: list[list[int]]) -> list[list[int]]:
    """
    Pre:
        - Recibe una matriz (lista de listas de enteros).
        - La matriz no debe ser vacia.
        - La matriz debe ser rectangular o cuadrada, osea que, debe tener la misma cantidad de
            elementos en cada fila al igual que en cada columna.

    Post:
        - Devuelve una nueva matriz transpuesta.
        - Si la matriz original era de dimensiones MxN (M filas, N columnas),
          la matriz resultante será de dimensiones NxM.
    """

    cant_columnas = len(matriz)
    matriz_transpuesta = [[fila[columna] for fila in matriz]
                          for columna in range(cant_columnas)]

    return matriz_transpuesta


# Opción f -----------------------------------------------------------------------------------------
def calcular_promedio_fila(matriz: list[list[int]], ind_fila: int) -> float:
    """
    Pre:
        - Recibe una matriz, no vacia.
        - Recibe el índice de la fila que debe ser un entero positivo.

    Post:
        - Devuelve el promedio de los elementos de la fila elegida.
    """

    fila = matriz[ind_fila]

    suma_elem = sum(fila)
    cant_elem = len(fila)
    promedio = suma_elem / cant_elem

    return promedio


# Opción g -------------------------------------------------------------------------------------------
def calcular_porcentaje_impares_columna(matriz: list[list[int]], ind_columna: int) -> float:
    """
    Pre:
        - Recibe una matriz que no debe estar vacía.
        - Recibe el indice de la columna que debe ser un entero positivo.

    Post:
        - Devuelve el porcentaje de elementos impares en la columna ejegida.
    """

    total_elem = len(matriz)
    contador_imp = 0

    for fila in matriz:
        elemento = fila[ind_columna]

        if elemento % 2 != 0:
            contador_imp += 1

    if total_elem == 0:
        return 0.0

    porcentaje = (contador_imp / total_elem) * 100

    return porcentaje


# Opción h -------------------------------------------------------------------------------------------
def es_cuadrada(cant_filas: int, cant_columnas: int) -> bool:
    """
    Esta función verifica que una matriz tenga la misma cantidad de filas como columnas,
    si es asi la matriz es cuadrada

    Pre:
        - Recibe la cantidad de filas y columnas que componen la matriz
        - Deben ser números enteros positivos

    Post:
        - Retorna True en caso de ser cuadrada
        _ Retorna False en caso contrario.

    """

    if cant_filas != cant_columnas:
        return False
    return True


def es_simetrica(matriz: list[list[int]]) -> bool:
    """
    Pre:
        - Recibe una matriz, lista de listas de numeros enteros

    Post:
        - Devuelve True si la matriz es cuadrada y A[i][j] == A[j][i].
        - Devuelve False en caso contrario.
    """
    cant_filas = len(matriz)
    cant_columnas = len(matriz[0])

    if not es_cuadrada(cant_filas, cant_columnas):
        return False

    for i in range(cant_filas):
        for j in range(i + 1, cant_filas):

            if matriz[i][j] != matriz[j][i]:
                return False
    return True


# Opción i ---------------------------------------------------------------------------
def es_simetrica_diagonal_secundaria(matriz: list[list[int]]) -> bool:
    """
    Pre:
        - Recibe una matriz, lista de listas de numeros enteros

    Post:
        - Devuelve True si la matriz es cuadrada y A[i][j] == A[N-1-j][N-1-i].
        - Devuelve False en caso contrario.
    """

    cant_filas = len(matriz)
    cant_columnas = len(matriz[0])

    if not es_cuadrada(cant_filas, cant_columnas):
        return False

    for i in range(cant_filas):
        for j in range(cant_filas):

            if matriz[i][j] != matriz[cant_filas - 1 - j][cant_filas - 1 - i]:
                return False

    return True


# Opción j -----------------------------------------------------------------------------------------
def columnas_palindromas(matriz: list[list[int]]) -> list[int]:
    """
    Pre:
        - Recibe una matriz (lista de listas de enteros) no vacía y bien formada.

    Post:
        - Devuelve una lista de enteros con los índices (0-base) de las columnas
          que son palíndromos (capicúas).
    """

    cant_filas = len(matriz)
    cant_columnas = len(matriz[0])

    if cant_filas <= 1:
        return list(range(cant_columnas))

    indices_palindromos = []

    for j in range(cant_columnas):
        columna = [matriz[i][j] for i in range(cant_filas)]
        if columna == columna[::-1]:
            indices_palindromos.append(j)

    return indices_palindromos


# Menu ------------------------------------------------

def guiones(cant: int) -> str:
    print("-"*cant)


def opciones():
    opc = ["Crear y cargar datos en una matriz", "Ordenar en forma ascendente cada una de las filas de la matriz.", "Intercambiar dos filas, cuyos números se reciben como parámetro.", "Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.",
           "Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)", "Calcular el promedio de los elementos de una fila, cuyo número se recibe como parámetro.", "Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.", "Determinar si la matriz es simétrica con respecto a su diagonal principal.", "Determinar si la matriz es simétrica con respecto a su diagonal secundaria.", "Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo una lista con los números de las mismas."]
    letras = "abcdefghij"

    for letra, op in zip(letras, opc):
        print(f"{letra}. {op}")


def menu():

    matriz_prueba = [
                    [17, 42, 9, 25],
                    [8, 33, 50, 12],
                    [4, 19, 27, 45]
    ]

    matriz_sim = [
                 [10,  2,  5],
                 [2, 20,  7],
                 [5,  7, 30]
    ]

    matriz_diagonal = [
                      [1, 2, 9],
                      [5, 8, 2],
                      [7, 5, 1]
    ]

    matriz_capicua = [
                     [1, 5, 7, 9],
                     [2, 1, 8, 8],
                     [1, 5, 7, 9]
    ]

    largo = len(matriz_prueba)
    largo_col = len(matriz_prueba[0])

    while True:
        opciones()
        op = input("Ingrese una opción (salir): ").lower()

        if op == "salir":
            break

        elif op == "a":
            pass

        elif op == "b":
            matriz_b = ordenar_filas_asc(matriz_prueba)
            print(matriz_b)

        elif op == "c":
            print(
                f"Se le solicita el indice de las filas a intercambiar (rango valido: 0 - {largo - 1}")
            while True:
                fila_a = int(input("Ingrese la fila A: "))
                if validar_rango(0, largo - 1, fila_a):
                    break
                print(
                    f"Error - Valor Fuera de rango. Ingrese un número entre 0 y {largo - 1}")

            while True:
                fila_b = int(input("Ingrese la fila B: "))
                if validar_rango(0, largo - 1, fila_b):
                    break
                print(
                    f"Error - Valor Fuera de rango. Ingrese un número entre 0 y {largo - 1}")

            matriz_c = intercambiar_filas(fila_a, fila_b, matriz_prueba)
            print(matriz_c)

        elif op == "d":
            print(
                f"Se le solicita el indice de las columnas a intercambiar (rango valido: 0 - {largo_col - 1})")
            while True:
                columna_a = int(input("Ingrese la COLUMNA A: "))
                if validar_rango(0, largo_col - 1, columna_a):
                    break
                print(
                    f"Error - Valor Fuera de rango. Ingrese un número entre 0 y {largo_col - 1}")

            while True:
                columna_b = int(input("Ingrese la COLUMNA B: "))
                if validar_rango(0, largo_col - 1, columna_b):
                    break
                print(
                    f"Error - Valor Fuera de rango. Ingrese un número entre 0 y {largo_col - 1}")

            matriz_c = intercambiar_columnas(
                columna_a, columna_b, matriz_prueba)
            print(matriz_c)

        elif op == "e":
            print(transponer_matriz(matriz_prueba))

        elif op == "f":
            while True:
                print(
                    f"Se le solicitara el indice de la fila a promediar. Rango Valido: 0 a {largo_col - 1}")
                ind_fila = int(input("Ingrese el indice de la fila: "))
                if validar_rango(0, largo_col - 1, ind_fila):
                    break
                print(
                    f"Error - Valor Fuera de rango. Ingrese un número entre 0 y {largo_col - 1}")

            promedio_fila = calcular_promedio_fila(matriz_prueba, ind_fila)
            print(promedio_fila)

        elif op == "g":
            print(
                f"Se le solicitara el indice de la columna. Rango valido: (0 a {largo_col - 1})")
            while True:
                ind_columna = int(input("Ingrese el indice de la columna: "))
                if validar_rango(0, largo_col - 1, ind_columna):
                    break
            porcentaje = calcular_porcentaje_impares_columna(
                matriz_prueba, ind_columna)
            print(round(porcentaje, 2))

        elif op == "h":
            print(es_simetrica(matriz_prueba))
            print(es_simetrica(matriz_sim))

        elif op == "i":
            print(es_simetrica_diagonal_secundaria(matriz_prueba))
            print(es_simetrica_diagonal_secundaria(matriz_diagonal))

        elif op == "j":
            indices = columnas_palindromas(matriz_capicua)

            if indices:
                print(
                    f"\nLos índices de las columnas que son palíndromos son: **{indices}**")
            else:
                print("\nNo se encontraron columnas que sean palíndromos.")

        else:
            print("la opción ingresada es invalida, intente denuevo...")


menu()
