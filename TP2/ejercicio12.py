def registrar_socios():
    """
    Pre: Pide al usuario que ingrese números de socio (5 dígitos), uno por vez.
         Se termina cuando el usuario ingresa 0.
    Post: Devuelve una lista con todos los números de socio ingresados, 
          cada vez que ingresaron al club (pueden repetirse).
    """
    ingresos = []
    while True:
        nro_socio = int(
            input("Ingrese número de socio (5 dígitos, 0 para terminar): "))
        if nro_socio == 0:
            break
        ingresos.append(nro_socio)
    return ingresos


def mostrar_ingresos(ingresos):
    """
    Pre: Recibe una lista con los números de socio de todos los ingresos.
    Post: Muestra por pantalla, para cada socio que apareció, cuántas veces entró.
          Cada socio aparece solo una vez en el informe.
    """
    socios_unicos = []
    print("\nRegistro de ingresos por socio:")
    for socio in ingresos:
        if socio not in socios_unicos:
            cantidad = ingresos.count(socio)
            print(f"Socio {socio}: {cantidad} ingreso(s)")
            socios_unicos.append(socio)


def eliminar_socio(ingresos, socio_baja):
    """
    Pre: Recibe la lista de ingresos y el número de socio que se dio de baja.
    Post: Elimina de la lista todos los ingresos de ese socio y devuelve
          cuántos ingresos se borraron.
    """
    cantidad_eliminada = ingresos.count(socio_baja)
    while socio_baja in ingresos:
        ingresos.remove(socio_baja)
    return cantidad_eliminada


ingresos = registrar_socios()

print()
print("---------- Registros antes de eliminar -------------")
mostrar_ingresos(ingresos)

socio_baja = int(input("Ingrese el número de socio que desea eliminar: "))
cantidad_eliminada = eliminar_socio(ingresos, socio_baja)

print()
print(f"Se eliminaron {cantidad_eliminada} ingreso del socio {socio_baja}.")

print()
print("-------- Registros después de eliminar al socio indicado -------------")
mostrar_ingresos(ingresos)
