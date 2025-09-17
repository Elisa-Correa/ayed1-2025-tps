import random as rn
rn.seed(0)


"""
Lista 1 = Se crea una lista con numeros al azar comprendidos entre el 1 al 100, de forma random.

Lista 2 = Se crea una nueva lista con los elementos impares de la Lista1 utilizando Filter()
"""

lista1 = [rn.randint(1, 100) for i in range(10)]
lista2 = list(filter(lambda n: n % 2 != 0, lista1))

print(lista1)
print(lista2)
