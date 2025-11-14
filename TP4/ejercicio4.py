def solicitar_n():
    while True:
        num = input("ingrese un número entero positivo: ")

        try:
            n = int(num)

            if not (1 <= n <= 3999):
                print(
                    "Error: El número debe estar entre 1 y 3999 para una conversión romana estándar.")

            else:
                return n

        except ValueError:
            print("Error - el valor ingresado es invalido, intente denuevo")


def conversor_romano(n: int) -> str:
    """
    Convierte un número entero (1 a 3999) en su representación romana, ya que no existe un 0 como tal.

    Pre::
        - Recibe un número entero en el rango entre 1 a 3999.

    Post:
        - Retorna una cadena de caracteres con el número romano, o un mensaje de error.
    """
    n = solicitar_n()

    valores_romanos = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    resultado = ""

    for valor, simbolo in valores_romanos:
        while n >= valor:
            resultado += simbolo
            n -= valor

    return resultado


print(conversor_romano(123))
