import math


def calcular_raiz_cuadrada_segura() -> float:
    """
    Esta funcion calcula la raíz cuadrada de un número ingresado por el usuario.
    Utiliza manejo de excepciones para evitar errores si se ingresa un número negativo
    o caracteres no numéricos.

    Pre:
        - No recibe parámetros.

    Post:
        - Retorna la raíz cuadrada (float) del número ingresado.
        - Muestra un mensaje de error si el número no es válido o es negativo.
    """
    print("Calculadora de Raíz Cuadrada")

    while True:
        try:
            entrada = input(
                "Ingrese un número positivo para calcular su raíz cuadrada: ").strip()

            num = float(entrada)

            if num < 0:

                raise ValueError(
                    "Error: La raíz cuadrada solo se puede calcular para números mayores o iguales a cero.")

            raiz = math.sqrt(num)

            print(
                f"\nResultado: La raíz cuadrada de {num} es {round(raiz, 5)}")
            return raiz

        except ValueError as e:
            print(f"\nEntrada inválida ->>> {e}")

        except Exception:
            print("\nError inesperado durante el procesamiento de la entrada.")


def programa_de_prueba_raiz():

    calcular_raiz_cuadrada_segura()
    print("-" * 60)


if __name__ == "__main__":
    programa_de_prueba_raiz()
