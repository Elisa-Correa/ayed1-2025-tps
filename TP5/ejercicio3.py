def obtener_nombre_mes(numero_mes: int) -> str:
    """
    Devuelve el nombre del mes cuyo número se recibe como parámetro.

    Pre:
        - Recibe el número del mes (entero).

    Post:
        - Retorna una cadena con el nombre del mes si el número es válido.
        - Retorna una cadena vacía ("") si el número del mes es inválido,
          detectando el error a través de una excepción.
    """

    NOMBRES_MESES = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    try:

        nombre_mes = NOMBRES_MESES[numero_mes - 1]
        return nombre_mes

    except IndexError:
        return ""

    except TypeError:
        return ""


def verificar_meses():

    pruebas = [
        (1, "Enero"),
        (6, "Junio"),
        (12, "Diciembre"),
        (0, "invalido"),
        (13, "invalido"),
        (-5, "invalido"),
    ]

    for numero, esperado in pruebas:
        resultado = obtener_nombre_mes(numero)

        if not resultado:
            print("ERROR - El numero del mes ingresado es invalido")

        es_correcto = resultado == esperado

        print(f"\nNúmero ingresado: {numero}")
        print(f"-> Resultado obtenido: '{resultado}' | Esperado: '{esperado}'")


if __name__ == "__main__":
    verificar_meses()
