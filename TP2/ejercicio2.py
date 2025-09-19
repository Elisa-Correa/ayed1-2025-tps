import random as rn
rn.seed(0)


def lista_aleatoria(cant: int) -> list:
    """
    Pre: Debe recibir un numero entero positivo

    Post: retorma una lista de enteros comprendidos entre 1 y 100 con N cantidad de elementos.
    """

    lista = [rn.randint(1, 100) for i in range(cant)]
    return lista


def hay_repetido(lista: list) -> bool:
    """
    Pre: Recibe una lista que no debe ser vacia []

    Post: Retorna True en caso de existir un elemento repetido, y False en caso de no haberlo.
    """

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return True
    return False


def elementos_sin_repetir(lista: list) -> list:
    """
    Pre: recibe una lista que no debe ser vacia []

    Post: Devuelve una lista con elementos de la original sin repetirlos.
    """

    lista_unica = []

    for e in lista:
        if e not in lista_unica:
            lista_unica.append(e)
    return lista_unica


def guion(cant=70) -> str:
    print("-" * cant)


def opc():
    opc = ["salir del programa", "Crea una lista de numeros aleatorios entre 1 y 100, de N cantidad",
           "Verificar si hay un elemento repetido en una lista", "Recibe una lista y la devuelve sin elementos repetidos"]

    for i, op in enumerate(opc):
        print(f"{i}. {op}")


def menu():

    lista1 = [1, 2, 3, 2]
    lista2 = [1, 2, 3]
    lista3 = ["a", "b", "c", "b"]

    op = "1"
    while True:
        opc()
        op = input("Ingresa una opcion: ")
        guion()

        if op == "0":
            print("Finalizo el programa...")
            guion()
            break

        elif op == "1":
            cant = -1
            while cant <= 0:
                cant = int(input("Ingrese la longitud de su lista: "))

            print(lista_aleatoria(cant))
            guion()

        elif op == "2":
            print(lista1)
            print(hay_repetido(lista1))
            print(lista2)
            print(hay_repetido(lista2))
            print(lista3)
            print(hay_repetido(lista3))

        elif op == "3":
            print(lista1)
            print(elementos_sin_repetir(lista1))
            print(lista3)
            print(elementos_sin_repetir(lista3))

        else:
            print("opcion invalida intente denuevo...")


menu()
