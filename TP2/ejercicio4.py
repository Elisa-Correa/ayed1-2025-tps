def eliminar_valores(lista1: list[int], lista2: list[int]) -> list:
    """
    Esta funcion recibe 2 listas y elimina de la primera, elementos que se encuentren en la segunda lista.

    Pre: Recibe una lista de enteros, no debe ser vacia []

    Post: Devuelve la primera lista, sin los valores que se encontraban en la segunda lista.
    """
    for valor in lista2:
        while valor in lista1:
            lista1.remove(valor)

    return lista1


lista1 = [1, 2, 3, 4, 5, 6, 2, 3]
lista2 = [2, 3]

print("Lista original:", lista1)
print("Lista con los valores a eliminar en la primera:", lista2)

lista_final = eliminar_valores(lista1, lista2)
print("Lista final:", lista_final)
