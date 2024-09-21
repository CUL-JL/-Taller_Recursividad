# 2. Suma Recursiva
list_n = []
def suma_hasta(n):
    if n == 1: return 1 # Caso base: n = 1
    else: suma_hasta(n - 1); list_n.append(n) # Caso recursivo: n > 1
    return f'{sum(list_n)} {list_n}\n' # Retorno: n y list_n