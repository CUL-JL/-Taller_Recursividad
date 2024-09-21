# 1. Contador Recursivo
list_n = []
def contar_hasta(n): 
    if n == 0: return 'el programa se detuvo.' # Caso base: cuando n = 0
    else: contar_hasta(n - 1); list_n.append(n) # Caso recursivo: cuando n > 0
    return f'{n} {list_n}\n' # Retorno: n y list_n