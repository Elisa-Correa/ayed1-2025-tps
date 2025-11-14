def filtrar_palabras_a(frase: str, N: int) -> str:
    """
    Esta función filtra palabras usando un bucle 'for' tradicional.

    Pre:
      - Recibe frase como una cadena de caracteres
      - Recibe n como un numero entero

    Post:
      - Retorna una cadena de caracteres
    """

    palabras_originales = frase.split()
    palabras_filtradas = []

    # Recorrer cada palabra y aplica la condición de filtro.
    for palabra in palabras_originales:
        if len(palabra) >= N:
            palabras_filtradas.append(palabra)

    # Une las palabras filtradas de vuelta en una cadena.
    return " ".join(palabras_filtradas)


def filtrar_palabras_b(frase: str, N: int) -> str:
    """
    Esta función filtra palabras usando una lista por comprensión (List Comprehension).

    Pre:

    - Recibe una frase como una cadena de caracteres.
    - Recibe n como un numero entero positivo.
    """

    # La lista por comprensión (dentro de los corchetes) genera la lista filtrada
    # de manera concisa: [expresión for elemento in iterable if condición]
    palabras_filtradas = [
        palabra for palabra in frase.split() if len(palabra) >= N]

    # Se utiliza la misma técnica de unión para el resultado final.
    return " ".join(palabras_filtradas)


def filtrar_palabras_c(frase: str, N: int) -> str:
    """Filtra palabras usando la función 'filter' con una lambda."""

    palabras_originales = frase.split()

    # Definir la función de filtrado: toma una palabra y verifica su longitud.
    # filter() devuelve un objeto iterable (un 'filter object').
    palabras_filtradas_iterable = filter(
        lambda p: len(p) >= N, palabras_originales)

    # Se convierte el iterable de vuelta a una cadena.
    return " ".join(palabras_filtradas_iterable)


def verificar_funciones():
    """
    Esta funcion se encarga de verificar el comportamiento de las tres funciones.

    Pre:
      - No recibe nada por parametro

    Post:
      -
    """

    # Datos de Prueba ------------------------------------------------------------
    frase = "A diferencia de lo que solemos creer, las gotas de lluvia no son 'lágrimas' celestes, sino 'panecillos' que caen del cielo a gran velocidad"
    n = 5
    # -----------------------------------------------------------------------------

    print(f"\nFrase Original: '{frase}'")
    print(f"Longitud mínima (N): {n}")
    print("-" * 50)

    # Verificación A
    resultado_a = filtrar_palabras_a(frase, n)
    print(f"a. Ciclos Normales   -> '{resultado_a}'")

    # Verificación B
    resultado_b = filtrar_palabras_b(frase, n)
    print(f"b. Lista Comprensión -> '{resultado_b}'")

    # Verificación C
    resultado_c = filtrar_palabras_c(frase, n)
    print(f"c. Función filter    -> '{resultado_c}'")


if __name__ == "__main__":
    verificar_funciones()
