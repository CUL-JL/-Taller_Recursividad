# 3. Número Par o Impar
def es_par(n):
    if n == 0: return True # Caso base: n = 0
    elif n == 1: return False # Caso base: n = 1
    else: return es_par(n - 2) # Llamada recursiva: resta 2 al número y repite