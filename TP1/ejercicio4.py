def cambio(total: int, recibido: int, billetes: list) -> list:
    """
    Pre: Recibe un entero positivo que represente el total de la compra, 
         un entero positivo que represente el dinero recibido por el cliente, 
         y una lista de la denominación de billetes existentes.

    Post: Si no recibio nada, retorna una lista vacia []
          Si no se puede devolver el vuelto exacto, porque no hay billetes de denominación suficientes, devuelve [-1]
          Si se pudo devolver el vuelto completo, retorna una lista con la cantidad de billetes a devolver.
    """
    cantidades = []

    if recibido < total:
        return cantidades

    else:
        vuelto = recibido - total
        for billete in billetes:
            cantidades.append(vuelto//billete)
            if vuelto // billete > 0:
                vuelto %= billete
        if vuelto != 0:
            return [-1]
        else:
            return cantidades


def guion(cant=70) -> str:
    print("-" * cant)


def opciones():
    op = ["Salir", "Calcular vuelto"]

    for i, dato in enumerate(op):
        print(f"{i}. {dato}")


def menu():
    billetes = [5000, 1000, 500, 200, 100, 50, 10]

    op = "-1"
    while op != "0":
        opciones()
        guion()
        op = input("Ingrese la opción a realizar: ")
        guion()

        if op == "0":
            print("Finalizo...")

        elif op == "1":
            total = -1
            while total <= 0:
                total = int(input("Ingrese el total de la compra: "))
                guion()

            recibido = -1
            while recibido <= 0:
                recibido = int(input("Ingrese el dinero recibido: "))
                guion()

            vuelto = cambio(total, recibido, billetes)

            if vuelto == []:
                print("El dinero recibido es insuficiente")
                guion()

            elif vuelto == [-1]:
                print(
                    "No se puede entregar el cambio debido a falta de billetes con denominación adecuada")
                guion()

            else:
                for b, c in zip(billetes, vuelto):
                    if c > 0:
                        print(f" Billetes de {b}: {c}")
                guion()

        else:
            print("Opcion invalida, intente con otra opción")


menu()
