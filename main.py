from modules.exercise01 import contar_hasta; from modules.exercise02 import suma_hasta; from modules.exercise03 import es_par; from modules.exercise04 import invertir_cadena; from modules.exercise05 import potencia # importe de módulos

while True:
    try:
        match int(input('\nEjercicios:\n 1. Contador recursivo\n 2. Suma recursiva\n 3. Número par o impar\n 4. Invertir cadena\n 5. Potencia de un número\n 6. Salir\nIngrese una opción: ')):
            case 1: 
                while True:
                    try:
                        n  = int(input('Ingrese un número: '))
                        print(f'Contador recursivo hasta {n} es:'); contar_hasta(n)
                        break

                    except ValueError:
                        print('Error: ingreso de valor no numérico.\n')

            case 2: 
                while True:
                    try:
                        n  = int(input('Ingrese un número: '))
                        print(f'Suma recursiva de {n}: {suma_hasta(n)}'); 
                        break

                    except ValueError:
                        print('Error: ingreso de valor no numérico.\n')

            case 3: 
                while True:
                    try:
                        n  = int(input('Ingrese un número: '))
                        print(f'¿El número {n} es par?: {es_par(n)}');
                        break

                    except ValueError:
                        print('Error: ingreso de valor no numérico.\n')

            case 4: 
                while True:
                    try:
                        cadena  = input('Ingrese una cadena: ')
                        print(f'Cadena invertida: {invertir_cadena(cadena)}');
                        break

                    except ValueError:
                        print('Error: ingreso de valor no numérico.\n')

            case 5: 
                while True:
                    try:
                        a  = int(input('Ingrese el primer número: '))
                        b  = int(input('Ingrese el segundo número: '))
                        print(f'{a} elevado a {b} es: {potencia(a, b)}'); 
                        break

                    except ValueError:
                        print('Error: ingreso de valor no numérico.\n')

            case 6: print('Saliendo del programa.\n'); break

            case _: print('Opción no válida.\n')

    except ValueError:
        print('Error: ingreso de opción no válida.\n')