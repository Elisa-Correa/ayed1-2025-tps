def obtener_longitud_sin_puntuacion(palabra: str) -> int:
    """
    Función auxiliar que calcula la longitud de una palabra ignorando la puntuación,
    sin usar el módulo 'string'.

    Pre:
        - Recibe una palabra (cadena de caracteres).

    Post:
        - Retorna la longitud de la palabra después de haber eliminado los signos
          de puntuación más comunes.
    """

    PUNTUACION_COMUN = '.,;!?:()"\''

    caracteres_limpios = [c for c in palabra if c not in PUNTUACION_COMUN]

    return len(caracteres_limpios)

# ----------------------------------------------------------------------------


def ordenar_por_longitud(cadena: str) -> str:
    """
    Esta funcion recibe una cadena de palabras y las ordena por su longitud, conservando la puntuación.

    Pre:
        - Recibe una cadena de caracteres.

    Post:
        - Retorna una nueva cadena con las palabras ordenadas de menor a mayor
          longitud, conservando su puntuación original.
    """

    palabras_originales = cadena.split()

    palabras_ordenadas = sorted(
        palabras_originales, key=obtener_longitud_sin_puntuacion)

    return " ".join(palabras_ordenadas)


def verificar_ordenamiento():

    frase = "Una nube pesa alrededor de un millón de toneladas."

    print(f"\nFrase Original: '{frase}'")
    print("-" * 70)

    resultado = ordenar_por_longitud(frase)

    print(f"Cadena Ordenada:  '{resultado}'")


if __name__ == "__main__":
    verificar_ordenamiento()
