def mostrar_baraja_amigable(baraja: list[str], naipes_por_linea: int = 6):
    """
    Muestra la baraja de naipes de forma amigable por pantalla.

    Pre:
        - Recibe 'baraja', una lista de cadenas que representan los naipes.
        - Recibe 'naipes_por_linea', un entero indicando cuántos naipes mostrar por línea (opcional).

    Post:
        - Imprime la lista de naipes formateada por pantalla, sin retornar valor.
    """

    print("\nBaraja Española")
    print(f"Total: {len(baraja)} naipes\n")

    for i, naipe in enumerate(baraja):
        print(f"  {naipe}", end="")

        if (i + 1) % naipes_por_linea == 0:
            print("\n")
        else:
            print(" | ", end="")

    if len(baraja) % naipes_por_linea != 0:
        print("\n")


def crear_baraja_espanola():
    """
    Crea la lista completa de naipes de la baraja española (48 naipes)
    utilizando una lista por comprensión anidada.

    Pre:
        - No recibe parámetros.

    Post:
        - Retorna e imprime la lista de cadenas de la baraja española.
    """

    palos = ["Oros", "Copas", "Espadas", "Bastos"]

    valores_numericos = range(1, 13)

    baraja_espanola = [

        f"{valor_formateado} {palo}"

        # Itera sobre los palos
        for palo in palos

        # Itera sobre los valores
        for valor in valores_numericos


        for valor_formateado in [
            str(valor)
        ]
    ]

    return baraja_espanola


if __name__ == "__main__":

    baraja = crear_baraja_espanola()

    mostrar_baraja_amigable(baraja)
