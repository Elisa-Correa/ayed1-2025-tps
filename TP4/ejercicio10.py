import re


def reemplazar_palabras_completas(cadena: str, palabra_vieja: str, palabra_nueva: str) -> tuple[str, int]:
    """
    Reemplaza todas las apariciones de una palabra completa por otra en una cadena.

    Pre:
        - Recibe la cadena original de caracteres.
        - Recibe la palabra a buscar (palabra_vieja).
        - Recibe la palabra de reemplazo (palabra_nueva).

    Post:
        - Retorna una tupla que contiene:
            1. La cadena resultante después de los reemplazos.
            2. Un entero con la cantidad total de reemplazos realizados.
    """

    patron = r'\b' + re.escape(palabra_vieja) + r'\b'
    cadena_resultante, cantidad_reemplazos = re.subn(
        patron, palabra_nueva, cadena)
    return cadena_resultante, cantidad_reemplazos


def verificar_reemplazo():

    # Datos de prueba -------------------------------------------------------------------------------------------
    cadena_original = "Los dientes humanos son la única parte del cuerpo que no puede curarse por sí misma."
    palabra_vieja = "curarse"
    palabra_nueva = "sanarse"

    print(f"\nCadena Original:  '{cadena_original}'")
    print(f"Palabra a buscar: '{palabra_vieja}'")
    print(f"Palabra de reemplazo: '{palabra_nueva}'")
    print("-" * 70)

    cadena_final, reemplazos = reemplazar_palabras_completas(
        cadena_original, palabra_vieja, palabra_nueva)

    print(f"Cadena Resultante: '{cadena_final}'")
    print(f"Reemplazos realizados: {reemplazos}")


if __name__ == "__main__":
    verificar_reemplazo()
