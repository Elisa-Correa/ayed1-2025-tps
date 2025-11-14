import re


def es_email_valido(email: str) -> tuple[bool, str]:
    """
    Verifica si un email cumple con los requisitos:
    1. Un solo '@'
    2. Usuario: solo alfanumérico
    3. Dominio: no vacío, termina en .com o .com.ar (insensible a mayúsculas)

    Pre: Recibe la cadena de correo electrónico.
    Post: Retorna una tupla (True/False, Dominio_encontrado_o_cadena_vacia).
    """

    if email.count('@') != 1:
        return False, ""

    usuario, dominio_completo = email.split('@')

    if not usuario or not usuario.isalnum():
        return False, ""

    if not dominio_completo:
        return False, ""

    dominio_lower = dominio_completo.lower()

    if dominio_lower.endswith(".com") or dominio_lower.endswith(".com.ar"):
        return True, dominio_lower
    else:
        return False, ""


def validacion():
    """
    Ejecuta el bucle de validación y muestra el listado final de dominios.
    """

    print("Ingrese correos. Deje vacío y presione Enter -> para Finalizar.")

    dominios_unicos = set()

    while True:
        email = input("\nIngrese email: ").strip()

        if not email:
            print("\nFinalizando proceso...")
            break

        es_valido, dominio = es_email_valido(email)

        if es_valido:
            print(f"Estado: Válido")
            dominios_unicos.add(dominio)
        else:
            print(f"Estado: Inválido. Revise el formato (usuario alfanumérico, un solo '@', dominio termina en .com/.com.ar).")

    dominios_ordenados = sorted(list(dominios_unicos))

    print("\nListado de Dominios Válidos Encontrados ------------")
    if dominios_ordenados:
        for dominio in dominios_ordenados:
            print(f"* {dominio}")
    else:
        print("No se ingresaron dominios válidos.")


if __name__ == "__main__":
    validacion()
