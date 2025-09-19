def registrar_pacientes():
    """
    Registra los pacientes en la clínica hasta que se ingrese -1 como número de afiliado.

    Pre: No recibe un parametro.

    Post: Devuelve dos listas: pacientes_urgencia y pacientes_turno.
    """
    pacientes_urgencia = []
    pacientes_turno = []

    while True:
        nro_afiliado = int(
            input("Ingrese un numero de afiliado (-1 para finalizar): "))

        if nro_afiliado == -1:
            print("Finalizo carga de afiliados...")
            break

        print("0. si es de urgencia")
        print("1. si tiene turno")
        tipo = int(input("Ingrese una opción: "))

        if tipo == 0:
            pacientes_urgencia.append(nro_afiliado)

        elif tipo == 1:
            pacientes_turno.append(nro_afiliado)

        else:
            print("Opcion invalida, intente denuevo...")

    return pacientes_urgencia, pacientes_turno


def mostrar_listado(pacientes_urgencia, pacientes_turno):
    """
    Pre: recibe 2 listas que no deben ser vacias []

    Post: Imprime por pantalla el listado de pacientes por urgencia y por turno.
    """
    print("\nPacientes atendidos por urgencia:")
    for i, pac_urg in enumerate(pacientes_urgencia):
        print(f"{i+1}. {pac_urg}")

    print("\nPacientes atendidos por turno:")
    for i, pac_tur in enumerate(pacientes_turno):
        print(f"{i+1}. {pac_tur}")


def buscar_afiliado(pacientes_urgencia, pacientes_turno):
    """
    Permite buscar un número de afiliado y mostrar cuántas veces fue atendido
    por urgencia y por turno. Repite hasta ingresar -1.
    """
    while True:
        nro = int(input("\nIngrese número de afiliado a buscar (-1 para salir): "))
        if nro == -1:
            break
        cantidad_urgencia = pacientes_urgencia.count(nro)
        cantidad_turno = pacientes_turno.count(nro)
        print(
            f"El afiliado {nro} fue atendido {cantidad_urgencia} veces por urgencia y {cantidad_turno} veces por turno.")


pacientes_urgencia, pacientes_turno = registrar_pacientes()
mostrar_listado(pacientes_urgencia, pacientes_turno)
buscar_afiliado(pacientes_urgencia, pacientes_turno)
