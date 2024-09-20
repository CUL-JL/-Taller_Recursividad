# 2. Suma Recursiva
def suma_hasta(n):
    if n == 1: return 1 # Caso base: n = 1
    else: return n + suma_hasta(n - 1) # Llamada recursiva: suma_hasta(n - 1)