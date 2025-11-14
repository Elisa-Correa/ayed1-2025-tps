import random


def jugar_adivina_numero():
    """
    Esta funcion se trata de un juego donde el usuario debe divinar un número generado al azar entre 1 y 500.
    El programa maneja entradas no numericas como intentos fallidos.

    Pre:
        - No recibe parámetros.

    Post:
        - Imprime el resultado del juego y la cantidad de intentos.
    """

    LIMITE_SUPERIOR = 500
    numero_secreto = random.randint(1, LIMITE_SUPERIOR)
    intentos = 0

    print("Adivina el Número Secreto")
    print(
        f"Se genero un número al azar entre 1 y {LIMITE_SUPERIOR}. Adivínalo si puedes...")

    while True:
        try:

            entrada = input("\nIntroduce tu intento: ").strip()

            intentos += 1

            intento_usuario = int(entrada)

            if intento_usuario == numero_secreto:
                print(
                    f"\n¡FELICIDADES! Adivinaste el número secreto ({numero_secreto})")
                print(f"Te tomó un total de {intentos} intentos.")
                break

            elif intento_usuario < numero_secreto:
                print("El número secreto es MAYOR que el ingresado.")

            else:
                print("El número secreto es MENOR que el ingresado.")

        except ValueError:
            print(
                "ERROR: La entrada no es un número válido. Esto cuenta como un intento.")

        except KeyboardInterrupt:
            print(
                f"\nJuego interrumpido. El número secreto era: {numero_secreto}")
            break

        except Exception:
            print("Se produjo un error inesperado.")
            break


if __name__ == "__main__":
    jugar_adivina_numero()
