def solicitar_positivos() -> list:
    
    """
       Solicita que el usuario ingrese por teclado 3 números positivos,
       en caso de no serlo, se le vuelve a solicitar. 
    """
    
    lista = []
    num = 0
    contador = 0
    
    while contador  < 3:
        num = int(input("Ingrese un número: "))

        if num >= 0:
            lista.append(num)
            contador += 1
    return lista

def buscar_mayor_estricto(a: int , b: int , c: int ) -> int:
    
    """
    Busca el número mayor.
    
    Recibe 3 números enteros, los almacena en una lista y luego la recorre.
    Busca el número mayor y compara que el proximo número no sea igual al mayor,
    en caso de no ser el mayor extricto retorna -1.
    """
    
    lista = [a, b, c] 
    mayor = 0
    repetido = False
    
    for i in lista:
        if i  == mayor:
            repetido = True 
            
        elif i  > mayor:
            mayor = i
            repetido = False
    
    if repetido == False:
        return mayor
    
    else:
        return -1


lista = solicitar_positivos()
mayor = buscar_mayor_estricto(lista[0], lista[1], lista[2])
print(lista)
print(mayor)

assert  buscar_mayor_estricto(1 , 2 , 3) == 3
assert buscar_mayor_estricto(4, 4 , 6) == 6
assert buscar_mayor_estricto(4 , 1 , 4) == -1