def concatenar_numeros(a: int, b: int) -> int:
    """
    Recibe 2 numeros entreros
    1_ Cuenta cuantos digitos tiene b a base de la división por 10,
    haciendo que en cada vuelta la coma se corra a la izquierda hasta ser menor a 0.
    2_ Utiliza un número auxiliar que va a pasar por la división para no modificar b
    """
    
    dig = 0
    aux = b
    while aux > 0:
        aux //= 10
        dig += 1
    numero = a * (10 ** dig) + b 
    return numero


assert concatenar_numeros(1234, 567) == 1234567
assert concatenar_numeros(12, 34) == 1234
assert concatenar_numeros(456, 111) == 456111
