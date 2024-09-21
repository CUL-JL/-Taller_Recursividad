from modules.exercise01 import contar_hasta
from modules.exercise02 import suma_hasta
from modules.exercise03 import es_par
from modules.exercise04 import invertir_cadena
from modules.exercise05 import potencia

def pedir_numero(num):
    while True:
        try: return int(input(num))
        except ValueError: print('Error: ingreso de valor no numérico.\n')

def pedir_cadena(txt):
    return input(txt)

def ejecutar_opcion(opcion):
    match opcion:
        case 1:
            n = pedir_numero('Ingrese un número: ')
            print(f'Contador recursivo: {contar_hasta(n)}\n')

        case 2:
            n = pedir_numero('Ingrese un número: ')
            print(f'Suma recursiva de {n}: {suma_hasta(n)}\n')

        case 3:
            n = pedir_numero('Ingrese un número: ')
            print(f'¿El número {n} es par?: {es_par(n)}\n')

        case 4:
            cadena = pedir_cadena('Ingrese una cadena: ')
            print(f'Cadena invertida: {invertir_cadena(cadena)}\n')

        case 5:
            a = pedir_numero('Ingrese el primer número: ')
            b = pedir_numero('Ingrese el segundo número: ')
            print(f'{a} elevado a {b} es: {potencia(a, b)}\n')

        case 6:
            print('Saliendo del programa...')
            return False

        case _:
            print('Error: ingreso de opción no válida.\n')