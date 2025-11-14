def contar_subsecuencia(cadena: str, sub_cadena: str) -> int:
    """
    Cuenta cuántas veces se encuentra una subcadena como subsecuencia dentro de otra cadena.
    La búsqueda es insensible a mayúsculas/minúsculas, y los caracteres
    de la subcadena no necesitan ser consecutivos, pero deben respetar el orden.

    Pre:
        - Recibe la cadena de caracteres principal (donde buscar).
        - Recibe la sub-cadena (la subsecuencia a buscar).

    Post:
        - Retorna un entero con la cantidad total de veces que se encontró la
          subsecuencia de forma no solapada.
    """

    cadena_lower = cadena.lower()
    sub_lower = sub_cadena.lower()
    len_sub = len(sub_lower)

    if len_sub == 0:
        return 0

    contador = 0
    start_ind = 0

    while start_ind < len(cadena_lower):

        sub_ind = 0
        coincidencia = -1

        for i in range(start_ind, len(cadena_lower)):

            if cadena_lower[i] == sub_lower[sub_ind]:

                sub_ind += 1

                if sub_ind == len_sub:
                    contador += 1
                    coincidencia = i
                    break

        if coincidencia != -1:
            start_ind = coincidencia + 1

        else:
            break

    return contador


def verificar_conteo():

    # Datos de prueba --------------------------------------------------------
    cadena_ejemplo = "Platero es pequeño, peludo, suave; tan blando por fuera, que se diría todo de algodón, que no lleva huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro."
    sub_cadena = "UADE"

    print(f"\nCadena Original: '{cadena_ejemplo}'")
    print(f"Subcadena a buscar: '{sub_cadena}'")
    print("-" * 70)

    conteo = contar_subsecuencia(cadena_ejemplo, sub_cadena)
    print(f"Cantidad encontrada: {conteo}")


if __name__ == "__main__":
    verificar_conteo()
