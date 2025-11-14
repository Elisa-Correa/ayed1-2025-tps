import time


def contador_con_interrupcion():
    """
    Imprime números entre 1 y 100000. Solicita confirmación al usuario para
    detenerse cuando se presiona Ctrl-C (KeyboardInterrupt).

    Pre:
        - No recibe parámetros.

    Post:
        - Imprime los números hasta 100000 o hasta que el usuario confirme
          la detención mediante Ctrl-C.
    """
    LIMITE = 100000
    i = 1

    print("Iniciando Contador (Presione Ctrl-C para pausar)")

    while i <= LIMITE:
        try:

            while i <= LIMITE:
                print(f"Número: {i}")
                i += 1

            print("\nConteo finalizado con éxito.")
            break

        except KeyboardInterrupt:

            print("\n\n--- Interrupción detectada (Ctrl-C) ---")
            print(f"El contador se detuvo en {i-1}.")

            confirmacion = input(
                "¿Desea detener el programa permanentemente? (s/n): ").strip().lower()

            if confirmacion == 's':
                print("\nDetención confirmada por el usuario. Saliendo del programa.")
                break
            else:
                print("\nReanudando el conteo...")
                continue


if __name__ == "__main__":
    contador_con_interrupcion()
