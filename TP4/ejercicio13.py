def numero_a_letras(numero: int) -> str:
    """
    Convierte un número entero positivo (entre 0 y 1,000,000,000,000) a su representación en letras.

    Pre:
        - Recibe un número entero entre 0 y 1,000,000,000,000.

    Post:
        - Retorna una cadena con el número escrito en letras.
    """

    # 1. Validación de rango y caso base
    if not (0 <= numero <= 1_000_000_000_000):
        return "Error: Número fuera del rango permitido (0 a 1 billón)."
    if numero == 0:
        return "cero"

    UNIDADES = ["", "uno", "dos", "tres", "cuatro",
                "cinco", "seis", "siete", "ocho", "nueve"]
    DECENAS = ["", "diez", "veinte", "treinta", "cuarenta",
               "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
    ESPECIALES = ["diez", "once", "doce", "trece", "catorce",
                  "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve"]
    CENTENAS = ["", "ciento", "doscientos", "trescientos", "cuatrocientos",
                "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
    GRUPOS = ["", "mil", "millón", "billón"]

    def convertir_cientos(n: int) -> str:
        """Convierte un número de 1 a 999 a letras."""
        letras = []
        c = n // 100
        d_u = n % 100

        # Centenas
        if c > 0:
            if c == 1 and d_u == 0:
                letras.append("cien")
            else:
                letras.append(CENTENAS[c])

        # Decenas y Unidades
        if d_u > 0:
            if 10 <= d_u <= 19:
                letras.append(ESPECIALES[d_u - 10])
            elif d_u % 10 == 0:
                letras.append(DECENAS[d_u // 10])
            else:
                d = d_u // 10
                u = d_u % 10

                if d == 0:  # 1 a 9 (ej. 3)
                    letras.append(UNIDADES[u])
                elif d == 2:  # 21 a 29 (ej. "veintiuno")
                    letras.append("veinti" + UNIDADES[u])
                else:  # 31 a 99 (ej. "treinta y uno")
                    letras.append(DECENAS[d] + " y " + UNIDADES[u])

        return " ".join(letras).strip()

    # bloques de miles
    letras_final = []
    resto = numero
    grupo_ind = 0

    while resto > 0 and grupo_ind < len(GRUPOS):
        grupo = resto % 1000
        resto //= 1000

        if grupo > 0:
            letras_grupo = convertir_cientos(grupo)
            nombre_grupo = GRUPOS[grupo_ind]

            if nombre_grupo in ("millón", "billón"):
                if grupo == 1:
                    letras_final.append(nombre_grupo)
                    letras_final.append(letras_grupo)
                else:
                    letras_final.append(nombre_grupo + "es")
                    letras_final.append(letras_grupo)

            elif nombre_grupo == "mil":
                letras_final.append(nombre_grupo)

                if grupo > 1:
                    letras_final.append(letras_grupo)

            elif grupo_ind == 0:
                letras_final.append(letras_grupo)

        grupo_ind += 1

    return " ".join(reversed(letras_final)).strip().replace("  ", " ")


def verificar_conversion():

    pruebas = [
        0, 12, 2_153, 1_110, 5_000, 99_999, 1_000_000_000, 1_000_000_000_000]

    for num in pruebas:
        letras = numero_a_letras(num)
        print(f"{num:,}: {letras.capitalize()}")


if __name__ == "__main__":
    verificar_conversion()
