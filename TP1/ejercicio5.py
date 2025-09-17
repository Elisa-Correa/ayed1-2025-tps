def es_oblongo(num: int) -> bool:
    for i in range(num):
        if i * (i+1) == num:
            return True
    return False


def es_triangular(num: int) -> bool:
    suma = 1
    for i in range(1, num+1):
        tn = i * (i+1) / 2
        if tn == num:
            return True
    return False


# Corrobora la función Oblongo ---------------------
assert es_oblongo(1) == False
assert es_oblongo(2) == True
assert es_oblongo(3) == False
assert es_oblongo(6) == True
assert es_oblongo(7) == False
assert es_oblongo(12) == True

# Corrobora la función Triangular ---------------------
assert es_triangular(1) == True
assert es_triangular(2) == False
assert es_triangular(3) == True
assert es_triangular(5) == False
assert es_triangular(6) == True
assert es_triangular(10) == True
