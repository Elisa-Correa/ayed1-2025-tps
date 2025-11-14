def obtener_ultimos_n(cadena: str, n: int) -> str:
    """
    Devuelve una subcadena con los últimos n caracteres de una cadena.

    Pre:
        - Recibe una cadena de caracteres (original).
        - Recibe n: como la cantidad de caracteres a extraer desde el final.

    Post:
        - Retorna una subcadena de los últimos n caracteres.
    """

    if n <= 0:
        return ""

    return cadena[-n:]


def verificar_ultimos_n():

    # Datos de prueba --------------------------------------------------
    frase = "Los aguacates son una fruta, no una verdura. Técnicamente se consideran una baya de una sola semilla"

    print(f"\nCadena Original: '{frase}'")
    print("-" * 50)

    n1 = 25
    resultado1 = obtener_ultimos_n(frase, n1)
    print(f"Últimos {n1} caracteres: '{resultado1}'")


if __name__ == "__main__":
    verificar_ultimos_n()
