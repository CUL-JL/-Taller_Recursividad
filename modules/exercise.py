# Importar funciones de cada ejercicio
from modules.exercise01 import contar_hasta
from modules.exercise02 import suma_hasta
from modules.exercise03 import es_par
from modules.exercise04 import invertir_cadena
from modules.exercise05 import potencia

# Funciones secundarias
def pedir_numero(num):
    while True: # Bucle
        try: return int(input(num)) # Retorno de valor numérico
        except ValueError: print('Error: ingreso de valor no numérico.\n') # Manejo de errores

def pedir_cadena(txt):
    return input(txt) # Retorno de cadena para caso 4

# Función principal
def ejecutar_opcion(opcion):
    match opcion:
        case 1: # Contador recursivo
            n = pedir_numero('Ingrese un número: ')
            print(f'Contador recursivo: {contar_hasta(n)}\n')

        case 2: # Suma recursiva
            n = pedir_numero('Ingrese un número: ')
            print(f'Suma recursiva de {n}: {suma_hasta(n)}\n')

        case 3: # Número par o impar
            n = pedir_numero('Ingrese un número: ')
            print(f'¿El número {n} es par?: {es_par(n)}\n')

        case 4: # Invertir cadena
            cadena = pedir_cadena('Ingrese una cadena: ')
            print(f'Cadena invertida: {invertir_cadena(cadena)}\n')

        case 5: # Potencia de un número
            a = pedir_numero('Ingrese el primer número: ')
            b = pedir_numero('Ingrese el segundo número: ')
            print(f'{a} elevado a {b} es: {potencia(a, b)}\n')

        case 6: # Salida
            print('Saliendo del programa...')
            return False

        case _: # Manejo de errores
            print('Error: ingreso de opción no válida.\n')