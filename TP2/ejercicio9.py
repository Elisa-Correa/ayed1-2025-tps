def multiplos_7_no_5(a: int, b: int) -> list[int]:
    """
    Pre: Recibe 2 enteros, a debe ser menor que b.

    Post: Retorna una lista de numeros que se encuentran en el rango de a y b, donde son multiplos de 7 y a su vez no son multiplos de 5.
    """

    return [n for n in range(a, b) if n % 7 == 0 and n % 5 != 0]


print(multiplos_7_no_5(0, 70))
