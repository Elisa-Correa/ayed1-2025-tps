def control_gasto(cant_viajes: int) -> int:
    precio = 1000

    if cant_viajes < 0:
        return -1

    elif cant_viajes == 0:
        return 0

    else:
        total = 0

        while cant_viajes:
            if cant_viajes > 40:
                resta = cant_viajes - 40
                cant_viajes -= resta
                total += (precio * 0.60) * resta

            elif cant_viajes > 30:
                resta = cant_viajes - 30
                cant_viajes -= resta
                total += (precio * 0.70) * resta

            elif cant_viajes > 20:
                resta = cant_viajes - 20
                cant_viajes -= resta
                total += (precio * 0.80) * resta

            else:
                total += cant_viajes * precio
                cant_viajes = 0

    return total


print(control_gasto(21))
