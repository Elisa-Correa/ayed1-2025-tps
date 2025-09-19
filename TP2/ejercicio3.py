def al_cuadrado(cant: int) -> list:
    """
    Pre: Recibe un positivo entero que representa la longitud que tendra la lista

    Post: Devuelve una lista con la longitud indicada, con los numeros elevados al cuadrado.
    """
    cuadrados = [x**2 for x in range(1, cant + 1)]
    return cuadrados


cant = -1
while cant <= 0:
    cant = int(input("Ingrese el largo que tendra su lista: "))

cuadrados = al_cuadrado(cant)
print(f"Los ultimos 10 números elevados al cuadrado: {cuadrados[-10:]}")
