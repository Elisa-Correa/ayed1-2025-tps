def extraer_subcadena_a(cadena: str, posicion: int, cant: int) -> str:
    """
    Esta función extrae una subcadena utilizando rebanadas (slicing).

    Pre:
        - Recibe la cadena de caracteres original.
        - Recibe la posicion (indice de inicio), como un numero entero positivo.
        - Recibe la cantidad caracteres a extraer, como un numero entero positivo.

    Post:
        - Retorna la subcadena extraída.
    """

    fin = posicion + cant

    return cadena[posicion:fin]


def extraer_subcadena_b(cadena: str, posicion: int, cant: int) -> str:
    """
    Esta función extrae una subcadena utilizando un ciclo for, sin usar rebanadas.

    Pre:
        - Recibe la cadena de caracteres original.
        - Recibe la posicion (indice de inicio), como un numero entero positivo.
        - Recibe la cantidad caracteres a extraer, como un numero entero positivo.

    Post:
        - Retorna la subcadena extraída.
    """

    subcadena = ""
    longitud_cadena = len(cadena)

    for i in range(cant):
        indice_actual = posicion + i

        if indice_actual < longitud_cadena:
            subcadena += cadena[indice_actual]
        else:
            break

    return subcadena


# Verificación de las funciones -----------------------------------------------------------------------

def verificar_extraccion():

    # Datos de prueba -----------------------------------------------------------------

    cadena_original = "El número de teléfono es 2254135769"
    pos_inicio = 24
    cant_chars = 8   # Extrayendo '43567890'

    print(
        f"\nCadena Original: '{cadena_original}' (Longitud: {len(cadena_original)})")
    print(f"Inicio: {pos_inicio}, Cantidad: {cant_chars}")
    print("-" * 60)

    # Rebanadas A
    resultado_a = extraer_subcadena_a(cadena_original, pos_inicio, cant_chars)
    print(f"a. Rebanadas ->>>   Resultado: '{resultado_a}'")

    # Rebanadas B
    resultado_b = extraer_subcadena_b(cadena_original, pos_inicio, cant_chars)
    print(f"b. Sin rebanadas ->>>   Resultado: '{resultado_b}'")


if __name__ == "__main__":
    verificar_extraccion()
