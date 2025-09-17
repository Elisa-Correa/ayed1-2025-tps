import random as rn
rn.seed(1)
# Camiones = peso maximo 500 kg

# Cajones = cantidad maxima 100 naranjas

# naranjas entre = 200 - 300 gramos
# Jugo = fuera del rango de peso


def reparto_naranjas(cosechado: int) -> str:
    PESO_MAX = 500_000
    PESO_MIN = PESO_MAX * 0.8
    para_jugo = 0
    para_cajon = 0
    peso_cajon = 0
    peso_cajones = []

    for i in range(cosechado):
        peso_naranja = rn.randint(150, 350)

        if peso_naranja >= 200 and peso_naranja <= 300:
            para_cajon += 1
            peso_cajon += peso_naranja

            if para_cajon == 100:
                peso_cajones.append(peso_cajon)
                para_cajon = 0
                peso_cajon = 0

        else:
            para_jugo += 1

    carga = 0
    prox_carga = 0
    camion = 0

    for cajon in peso_cajones:
        prox_carga = carga + cajon

        if prox_carga < PESO_MAX:
            carga += cajon

        else:
            if carga >= PESO_MIN:
                camion += 1

            carga = cajon

    if carga >= PESO_MIN:
        camion += 1

    return len(peso_cajones), para_jugo, para_cajon, camion


cant = -1
while cant <= 0:
    cant = int(input("Ingrese la cantidad de naranjas cosechadas: "))

cant_cajones, cant_jugo, sobrante, camiones = reparto_naranjas(cant)

print(f"Total de cajones para llenar: {cant_cajones}")
print(f"Total de naranjas para jugo: {cant_jugo}")
print(f"Naranjas sobrantes para el proximo reparto: {sobrante}")
print(
    f"Se necesitan {camiones} para transportar los cajones de naranjas comerciales")
