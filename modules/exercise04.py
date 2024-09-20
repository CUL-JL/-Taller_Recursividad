# 4. Invertir cadena
def invertir_cadena(cadena):
    if len(cadena) == 1: return cadena  # Caso base: cadena vacía o de un solo carácter
    elif len(cadena) == 0: return 'no hay caracteres.' # Caso propuesto: por si se da el caso de una cadena vacía
    else: return invertir_cadena(cadena[1:]) + cadena[0] # Llamada recursiva: devuelve el ultimo carácter concatenado con la función aplicada al resto de la cadena