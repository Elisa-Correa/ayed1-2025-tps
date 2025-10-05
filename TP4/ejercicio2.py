def centrar_texto(texto: str) -> str:
    """
    Recibe una cadena de caracteres y lo centra en pantalla.

    Pre:
        - La funcion debe recibir un Str.

    Post:
        - Retorna el str recibido centralizado teniendo 80 columnas.

    """
    return texto.center(80)


texto = receta_galletas_chips = "Hola Mundo, como estas?"
print(centrar_texto(texto))
