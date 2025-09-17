def impares(inicio: int, fin: int) -> list[int]:
    """
    Pre: Recibe 2 enteros, el primero indica desde que numero empieza y el otro en que numero debe terminar.

    Post: Devuelve una lista con los numeros comprendido entre el rango designado, donde se almacenaron solo los impares.
    """

    return [n for n in range(inicio, fin + 1) if n % 2 != 0]


print(impares(100, 200))
