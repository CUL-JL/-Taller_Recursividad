# 5. Potencia de un Número
def potencia(a, b):
    if b == 0: return 1 # Caso base: b = 0
    elif b == 1: return a # Caso propuesto: b = 1
    else: return a * potencia(a, b - 1) # Llamada recursiva: a * potencia(a, b - 1)