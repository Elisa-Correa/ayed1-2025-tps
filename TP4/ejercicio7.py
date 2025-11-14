def eliminar_subcadena_a(cadena: str, posicion: int, cant: int) -> str:
    """
    Elimina una subcadena usando rebanadas (slicing).

    Pre:
        - Recibe la cadena de caracteres original.
        - Recibe la posicion (indice de inicio), como un numero entero positivo.
        - Recibe la cantidad caracteres a eliminar, como un numero entero positivo.

    Post:
        - Retorna la cadena resultante sin el segmento que fue eliminado.
    """

    fin_segmento_eliminado = posicion + cant

    cadena_resultante = cadena[:posicion] + cadena[fin_segmento_eliminado:]

    return cadena_resultante


def eliminar_subcadena_b(cadena: str, posicion: int, cant: int) -> str:
    """
    Elimina una subcadena utilizando un ciclo for, sin usar rebanadas.

    Pre:
        - Recibe la cadena de caracteres original.
        - Recibe la posicion (indice de inicio), como un numero entero positivo.
        - Recibe la cantidad caracteres a eliminar, como un numero entero positivo.

    Post:
        - Retorna la cadena resultante sin el segmento que fue eliminado.
    """

    cadena_resultante = ""
    longitud_cadena = len(cadena)

    indice_corte = posicion

    indice_reinicio = posicion + cant

    for i in range(indice_corte):
        if i < longitud_cadena:
            cadena_resultante += cadena[i]

    for i in range(indice_reinicio, longitud_cadena):
        cadena_resultante += cadena[i]

    return cadena_resultante


def verificar_eliminacion():

    # Datos de prueba
    cadena_original = "La torre Eiffel puede ser 15 cm más alta en verano debido a la expansión térmica del hierro."
    pos_1 = 25
    cant_1 = 37

    print(f"\nCadena Original: '{cadena_original}'")
    print(
        f"Eliminar: '' y_Estructuras '' ||   Inicio {pos_1}   ||   Cantidad {cant_1}  ")
    print(f"Resultado esperado: La torre Eiffel puede ser expansión térmica del hierro.")
    print("-" * 120)

    # Rebanadas A
    resultado_a = eliminar_subcadena_a(cadena_original, pos_1, cant_1)
    print(f"a. Rebanadas ->>> Resultado: {resultado_a}")

    # Sin Rebanadas B
    resultado_b = eliminar_subcadena_b(cadena_original, pos_1, cant_1)
    print(f"b. Sin rebanadas ->>> Resultado: {resultado_b}")


# Ejecución del programa de verificación
if __name__ == "__main__":
    verificar_eliminacion()
