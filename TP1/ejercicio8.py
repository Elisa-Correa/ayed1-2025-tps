def dia_de_la_semana(dia: int, mes: int, anio: int) -> int:
    """
    Esta funcion calcula el día de la semana para una fecha dada usando la fórmula de Zeller.

    Pre: Recibe 3 enteros positivos correspondientes al dia mes y año.
        La fecha dada debe ser valida / existente.
        El dia debe correponder al mes.
        El mes debe encontrarse entre 1 y 12.
        El año debe ser mayor a 0.


    Post:
    Devuelve un entero que representa el día de la semana.
      0 = Domingo,
      1 = Lunes,
      2 = Martes, y asi sucesivamente hasta el 6 = Sabado
    Si la fecha es inválida → devuelve -1.
    """

    if dia < 1 or mes < 1 or mes > 12 or anio < 1:
        return -1

    if mes < 3:
        mes += 12
        anio -= 1

    mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100

    dia_sem = ((26 * mes - 2) // 10 + dia + anio2 +
               anio2 // 4 + siglo // 4 - 2 * siglo) % 7

    if dia_sem < 0:
        dia_sem += 7

    return dia_sem


assert dia_de_la_semana(4, 7, 2023) == 2
