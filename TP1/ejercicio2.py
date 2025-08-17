"""
Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida.
Debe tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no.

Realizar también un programa para verificar el comportamiento de la función.
"""

def validar_fecha(dia: int, mes: int, anio: int) -> bool:

    # Si es biciesto - mientras el año no sea 100
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        if mes > 0 and mes < 13:
            if mes == 1 or  mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12: # Dias = 31
                if dia > 0 and dia < 32:
                    return True 
            
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11: # Dias = 30
                 if dia > 0 and dia < 31:
                     return True
                    
            elif  mes == 2:
                if dia > 0 and dia < 30:
                     return True
            else:
                return False
            
        else:
            return False 
    
    else:
         if mes == 1 or  mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12: # Dias = 31
                if dia > 0 and dia < 32:
                    return True 
                
                elif mes == 4 or mes == 6 or mes == 9 or mes == 11: # Dias = 30
                     if dia > 0 and dia < 31:
                         return True
                
                elif  mes == 2:
                    if dia > 0 and dia < 29:
                         return True
                
                else:
                    return False 
                
        
