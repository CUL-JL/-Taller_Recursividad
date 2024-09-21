from modules.exercise import ejecutar_opcion

while True:
    try:
        ejecutar_opcion(int(input('Ejercicios:\n 1. Contador recursivo\n 2. Suma recursiva\n 3. Número par o impar\n 4. Invertir cadena\n 5. Potencia de un número\n 6. Salir\nIngrese una opción: ')))

    except ValueError:
        print('Error: ingreso de valor no numérico.\n')