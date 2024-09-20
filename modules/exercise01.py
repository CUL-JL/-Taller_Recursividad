# 1. Contador Recursivo
def contar_hasta(n): 
    if n == 0: 'el programa se detuvo.' # Caso base: cuando n = 0
    else: contar_hasta(n - 1); print(f' {n}') # Caso recursivo: imprime el número actual y llama a la función con n - 1