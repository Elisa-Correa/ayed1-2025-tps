def cargar_lista() -> list[int]:
    """
    Carga una lista con números enteros ingresados por el teclado,
    terminando la carga con el valor -1.

    Pre:
        - No recibe parámetros.
    Post:
        - Retorna la lista de números enteros cargados.
    """

    lista = []
    print("\nCarga de la lista (ingrese -1 para finalizar)")

    while True:
        try:
            entrada = input("Ingrese número entero para la lista: ").strip()

            if not entrada:
                continue

            num = int(entrada)
            if num == -1:
                break

            lista.append(num)

        except ValueError:
            print("Error: Ingrese un número entero válido.")

    return lista


def buscar_elementos(lista: list[int]):
    """
    Permite al usuario buscar elementos en la lista usando list.index().
    Aborta el proceso al detectar el tercer error de búsqueda (valor no encontrado).

    Pre:
        - Recibe la lista de números enteros donde buscar.

    Post:
        - Imprime las posiciones encontradas o los mensajes de error.

    """

    MAX_ERRORES = 3
    contador_errores = 0

    print("\nBúsqueda de Elementos en la Lista: ")
    print(
        f"La búsqueda se cortara después de {MAX_ERRORES} errores de 'Valor no encontrado'.")

    while contador_errores < MAX_ERRORES:

        valor = f"Ingrese el valor a buscar (Errores de búsqueda detectados: {contador_errores}): "
        entrada_busqueda = input(valor).strip()

        if not entrada_busqueda:
            continue

        try:
            valor_buscado = int(entrada_busqueda)

            try:
                posicion = lista.index(valor_buscado)

                # éxito
                print(
                    f"Valor encontrado: El valor {valor_buscado} se encuentra en la posición {posicion}.")

            except ValueError:
                print(
                    f"ERROR de Búsqueda: El valor {valor_buscado} NO pertenece a la lista.")
                contador_errores += 1

        except ValueError:
            print(
                f"ERROR de Formato: Ingrese un número entero válido. Este error no cuenta para el límite.")

        if contador_errores == MAX_ERRORES:
            print("\nLímite de 3 errores de búsqueda alcanzado. Finalizando busqueda....")
            break

    if contador_errores < MAX_ERRORES:
        print("\nBúsqueda finalizada.")


if __name__ == "__main__":

    mi_lista = cargar_lista()

    if not mi_lista:
        print("\nLa lista está vacía. No hay elementos para buscar.")

    else:
        print(f"\nLista cargada: {mi_lista}")
        print("-" * 35)

        buscar_elementos(mi_lista)
