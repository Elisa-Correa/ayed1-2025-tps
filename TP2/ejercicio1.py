import random as rn
import math
rn.seed(0)


def crear_lista() -> list:
    lista = []
    cant_elem = rn.randint(10, 99)

    for i in range(cant_elem):
        lista.append(rn.randint(1000, 9999))
    return lista


def producto_lista(lista: list) -> int:
    producto = math.prod(lista)
    return producto


def eliminar_valor(valor: int, lista: list) -> list:
    while valor in lista:
        lista.remove(valor)
    return lista


def es_capicua(lista) -> bool:
    if lista == lista[::-1]:
        return True
    return False


lista = crear_lista()
producto = producto_lista(lista)
