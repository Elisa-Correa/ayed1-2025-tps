def intercalar(lista1: list[int], lista2: list[int]) -> list[int]:
    """
    Pre: Recibe 2 listas de numeros entero.
         Permite que sean vacias [].
         Permite que tengan diferente longitud cada una.

    Post: Retorna una lista con los elemento intercalados de cada lista.


    Recibe 2 listas de numeros enteros, y las intercala guardandolas en una sola lista.
    Retorna una lista de numeros intercalados.
    El slicing no tiene problema si las 2 listas no tienen la misma longitud.
    """

    for i, valor in enumerate(lista2):
        ind = i*2+1
        lista1[ind:ind] = [valor]

    return lista1


lista1 = [1, 3, 5]
lista2 = [2, 4, 6, 8, 10]

print(intercalar(lista1, lista2))

assert intercalar([8, 1, 3], [5, 9, 7]) == [8, 5, 1, 9, 3, 7]
assert intercalar([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
assert intercalar([1, 3, 5, 7, 9], [2, 4, 6]) == [1, 2, 3, 4, 5, 6, 7, 9]
assert intercalar([1, 3, 5], [2, 4, 6, 8, 10]) == [1, 2, 3, 4, 5, 6, 8, 10]
