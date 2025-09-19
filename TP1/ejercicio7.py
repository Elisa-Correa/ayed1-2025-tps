def es_bisiesto(anio: int) -> bool:
    """
    Esta funcion verifica si el año es bisiesto.

    Pre: Recibe un entero positivo que representaria el año a verificar.

    Post: Devuelve un Boolean, si el año es bisiesto devuelve True, y si no lo fuera devuelve False.
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)


def dia_siguiente(dia: int, mes: int, anio: int) -> tuple:
    """
    Esta función se encarga de indicar cual es el dia siguiente al ingresado.

    Pre: Recibe 3 enteros positivos que representan el dia, mes y año.

    Post: Devuelve una tupla que indica el dia siguiente al ingresado.
    """

    if dia < 1 or mes < 1 or anio < 1:
        # Verifica que el dia, mes o año no sean valores negativos
        return (-1, -1, -1)

    dias_en_mes = [31, 28 + (1 if es_bisiesto(anio) else 0),
                   31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Crea una lista con el total de dia por mes, y para febrero utiliza la funcion es_biciesto para en caso de ser verdad,
    # suma un dia más, en caso contrario, mantiene 28 dias.

    # Verifica si el dia es valido para el mes y año dado
    if dia > dias_en_mes[mes - 1]:
        return (-1, -1, -1)

    dia += 1
    if dia > dias_en_mes[mes - 1]:
        dia = 1
        mes += 1
        if mes > 12:
            mes = 1
            anio += 1
    return (dia, mes, anio)


def sumar_dias(dia: int, mes: int, anio: int, cant: int) -> tuple:
    """
    Esta funcion se encarga de sumarle dias a una fecha brindada.

    Pre: Recibe 4 enteros positivos que representan, dia, mes, año y cantidad de dias a sumar a la fecha ingresada.

    Post: Devuelve una tupla con 3 enteros positivos que representan, dia, mes y año con la suma de dias realizada e indicada por el usuario.
    """
    for i in range(cant):
        dia, mes, anio = dia_siguiente(dia, mes, anio)
    return dia, mes, anio


def contar_dias(dia_ini: int, mes_ini: int, anio_ini: int, dia_fin: int, mes_fin: int, anio_fin: int) -> int:
    """
    Esta funcion cuenta cuantos dias hay entre 2 fechas ingresadas.

    Pre: Recibe 3 enteros positivos que representan dia, mes y año de inicio, y 3 enteros positivos que representan dia, mes y año de fin.

    Post: Devuelve un entero que corresponde al total de dias que hay entre una fecha y otra.
    """
    contador = 0
    while (dia_ini, mes_ini, anio_ini) != (dia_fin, mes_fin, anio_fin):
        dia_ini, mes_ini, anio_ini = dia_siguiente(dia_ini, mes_ini, anio_ini)
        contador += 1

    return contador


# Verificación del programa -------------------------------

# Verifica que devuelve el dia siguiente al ingresado:
assert dia_siguiente(28, 2, 2024) == (29, 2, 2024)  # Año bisiesto
assert dia_siguiente(28, 2, 2025) == (1, 3, 2025)  # Año no bisiesto


# Verifica que devuelve la fecha correspondiente a una cantidad de dias posteriores que indico el usuario.
assert sumar_dias(28, 2, 2024, 4) == (3, 3, 2024)   # Año bisiesto
assert sumar_dias(28, 2, 2025, 10) == (10, 3, 2025)  # Año no bisiesto

# Verifica que devuelve la cantidad de dias que hay entre 2 fechas:
assert contar_dias(28, 2, 2024, 1, 3, 2024) == 2  # Año bisiesto
assert contar_dias(1, 1, 2025, 5, 1, 2025) == 4  # Año no bisiesto
