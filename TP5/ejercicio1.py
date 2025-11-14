def ingresar_natural_seguro() -> int:
    """
    Esta funcion solicita al usuario el ingreso de un número natural (mayor a 0) y valida la entrada
    utilizando manejo de excepciones.

    Pre:
        - No recibe parámetros.

    Post:
        - Retorna un número entero natural (> 0) válido.
        - Muestra en pantalla la razón exacta de cualquier error de entrada.
    """
    while True:
        try:
            entrada = input("Ingrese un número natural (entero > 0): ").strip()

            numero = float(entrada)

            if not numero.is_integer():
                raise ValueError(
                    "Error: El número ingresado contiene decimales. Debe ser entero.")

            entero = int(numero)

            if entero <= 0:
                raise ValueError(
                    "Error: El número debe ser mayor que cero (un número natural).")
            return entero

        except ValueError as e:
            print(f"Error - entrada inválida. Razón del error: {e}")

        except Exception:
            print(
                "Error - entrada inválida. Razón del error: Se produjo un error inesperado.")


def programa_de_prueba():
    print("-" * 60)

    resultado = ingresar_natural_seguro()

    print("-" * 60)
    print(f"El número ingresado es un numero natural valido: {resultado}")


# Ejecución del programa de prueba
if __name__ == "__main__":
    programa_de_prueba()
