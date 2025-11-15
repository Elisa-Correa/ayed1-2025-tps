import datetime


def ingresar_fecha_valida():
    """Ingresa y valida una fecha retornándola como tupla (año, mes, dia)."""
    while True:
        fecha_str = input("Ingrese una fecha (AAAA-MM-DD): ").strip()
        try:
            # Separar y convertir a enteros
            partes = [int(p) for p in fecha_str.split('-')]
            if len(partes) != 3:
                raise ValueError

            año, mes, dia = partes

            # Intenta crear un objeto date, si falla, es una fecha inválida.
            datetime.date(año, mes, dia)

            # Si es válida, retorna la tupla
            return (año, mes, dia)

        except ValueError:
            print(
                "Error: Formato incorrecto o fecha inválida. Intente de nuevo (ej: 2025-02-29).")


def sumar_n_dias(fecha_tuple, n_dias):
    """Suma N días a una fecha (tupla) y retorna la nueva fecha (tupla)."""
    try:

        fecha_inicial = datetime.date(*fecha_tuple)

        delta = datetime.timedelta(days=n_dias)

        nueva_fecha = fecha_inicial + delta

        return (nueva_fecha.year, nueva_fecha.month, nueva_fecha.day)

    except Exception as e:
        print(f"Error al sumar días: {e}")
        return None


def ingresar_horario_valido():
    """Ingresa y valida un horario retornándolo como tupla (hora, min, seg)."""
    while True:
        print("Se le solicitaran 2 horarios a ingresar para calcular la diferencia -----------")
        horario_str = input("Ingrese un horario (HH:MM:SS): ").strip()
        try:
            partes = [int(p) for p in horario_str.split(':')]
            if len(partes) != 3:
                raise ValueError("Debe ingresar 3 componentes (HH:MM:SS).")

            hora, minuto, segundo = partes

            if not (0 <= hora <= 23 and 0 <= minuto <= 59 and 0 <= segundo <= 59):
                raise ValueError(
                    "Los valores de hora/minuto/segundo están fuera de rango.")

            return (hora, minuto, segundo)

        except ValueError as e:
            print(f"Error: {e}. Intente de nuevo (ej: 14:30:00).")


def calcular_diferencia_horarios(h1_tuple, h2_tuple):
    """
    Calcula la diferencia entre dos horarios (h2 - h1). 
    Si h1 > h2, asume que h2 es del día siguiente.
    Retorna la diferencia en segundos.
    """

    def horario_a_segundos(h):
        return h[0] * 3600 + h[1] * 60 + h[2]

    segundos_h1 = horario_a_segundos(h1_tuple)
    segundos_h2 = horario_a_segundos(h2_tuple)

    if segundos_h2 >= segundos_h1:
        diferencia_segundos = segundos_h2 - segundos_h1

    else:
        SEGUNDOS_EN_DIA = 86400

        diferencia_segundos = (SEGUNDOS_EN_DIA - segundos_h1) + segundos_h2

    if diferencia_segundos > 86400:
        return "Error: La diferencia calculada supera las 24 horas, lo cual es inválido según la regla."

    return diferencia_segundos


def programa_principal():

    print("\n--- a. Ingreso y Validación de Fecha ---")
    fecha_base = ingresar_fecha_valida()
    print(f"Fecha base válida: {fecha_base}")

    if fecha_base:

        while True:
            try:
                n_dias = int(
                    input("\n--- b. Sumar N días ---\nIngrese el número de días a sumar: "))
                break

            except ValueError:
                print("Por favor, ingrese un número entero.")

        nueva_fecha = sumar_n_dias(fecha_base, n_dias)

        if nueva_fecha:
            print(f"Fecha original: {fecha_base}")
            print(f"Nueva fecha (tras sumar {n_dias} días): {nueva_fecha}")

    print("\n--- c. Ingreso y Validación de Horario ---")
    h1 = ingresar_horario_valido()
    h2 = ingresar_horario_valido()

    if h1 and h2:
        print(f"\n--- d. Calcular Diferencia de Horarios ---")
        print(f"Horario 1 (salida/inicio): {h1}")
        print(f"Horario 2 (llegada/fin): {h2}")

        diferencia_segundos = calcular_diferencia_horarios(h1, h2)

        if isinstance(diferencia_segundos, str):
            print(diferencia_segundos)

        else:

            horas = diferencia_segundos // 3600
            minutos = (diferencia_segundos % 3600) // 60
            segundos = diferencia_segundos % 60

            print(f"Diferencia total en segundos: {diferencia_segundos} s")
            print(
                f"Diferencia: {horas:02d} horas, {minutos:02d} minutos, {segundos:02d} segundos.")


if __name__ == "__main__":
    programa_principal()
