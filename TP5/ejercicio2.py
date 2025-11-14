def sumar_cadenas_reales(cadena_a: str, cadena_b: str) -> float:
    """
    Suma dos valores contenidos en cadenas de caracteres, devolviendo el resultado
    como un número real.

    Pre:
        - Recibe dos cadenas de caracteres (cadena_a, cadena_b) que contienen
          la representación de números reales.

    Post:
        - Retorna la suma (float) de ambos números si la conversión es exitosa.
        - Retorna -1.0 si alguna de las cadenas no contiene un número real válido.
    """
    try:
        # Intentar convertir ambas cadenas a float
        num_a = float(cadena_a)
        num_b = float(cadena_b)

        return num_a + num_b

    except ValueError:
        return -1.0

    except Exception:
        return -1.0


def verificar_suma_cadenas():

    pruebas = [
        ("10.5", "5.2", 15.7),
        ("-3", "7.1", 4.1),
        ("20", "10", 30.0),
        ("abc", "5.0", -1.0),
        ("1.0", "xyz", -1.0),
        ("10,5", "5.2", -1.0),
        ("1e2", "3.0", 103.0)
    ]

    for cad_a, cad_b, esperado in pruebas:
        resultado = sumar_cadenas_reales(cad_a, cad_b)
        es_correcto = resultado == esperado

        if resultado == -1.0:
            mensaje = f"Error detectado: no pudo ser realizada la suma ya que alguno valor de los ingresado no fue valido"
        else:
            mensaje = f"Suma exitosa: {resultado}"

        print(f"\nEntradas: ('{cad_a}', '{cad_b}')")
        print(f" Resultado: {mensaje}")


# Ejecución del programa de verificación
if __name__ == "__main__":
    verificar_suma_cadenas()
