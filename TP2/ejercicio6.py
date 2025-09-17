def normalizar(lista: list[int]) -> list[float]:
    """
    Pre: Recibe una lista de numeros enteros como parametro. La misma no debe ser vacia []

    Post: Devuelve una lista con los digitos normalizados, es decir que todos sus elementos deben sumar 1.0

    Recibe una lista de enteros, y retorna una lista de flotantes.
    Realiza la suma de todos los elemntos de la lista, y luego divide cada elemento por el total de la suma.
    Esto indica la proporciion que representan del total, dando siempre la suma de toda la proporcion 1.0.
    """

    return [n/sum(lista) for n in lista]


print(normalizar([6, 2, 2]))

assert normalizar([1, 1, 2]) == [0.25, 0.25, 0.50]
assert normalizar([1, 2, 2]) == [0.2, 0.4, 0.4]
assert normalizar([1, 2, 5]) == [0.125, 0.25, 0.625]
assert normalizar([1, 4, 5]) == [0.1, 0.4, 0.5]
assert normalizar([6, 2, 2]) == [0.6, 0.2, 0.2]
