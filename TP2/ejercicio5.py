# Tp 2 - Ejercicio 5

def ordenada(lista: list) -> bool:
    """
    Pre: Recibe una lista como parametro, no debe ser vacia []

    Post: Devuelve un Booleano, True si esta ordenada de forma ascendente y False si es de forma descendente
    """
    return lista == sorted(lista)


"""
La función ordenada() recibe una lista previamente ordenada ya sea de
forma ascendente o descendente.
Si esta ordenada de forma ascendente devuelve True.
Si esta ordenada de forma descendente devuelve False.
Devuelve un booleano. 
"""


assert ordenada([1, 2, 3]) == True
assert ordenada([3, 2, 1]) == False
assert ordenada(["a", "b", "c"]) == True
assert ordenada(["c", "b", "a"]) == False
