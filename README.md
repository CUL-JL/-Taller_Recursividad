# Actividad: Ejercicios de Métodos Recursivos en Python

En esta actividad, implementarás varios métodos recursivos en Python y los integrarás en un programa con un menú interactivo para que el usuario pueda ejecutar cada funcionalidad. Aquí se enumeran los ejercicios que debes realizar:

**NOTA:** 

### 1. [Contador recursivo](/assets/exercise01.png)
Crea una función que reciba un número entero positivo `n` y cuente de 1 a `n`, imprimiendo cada número en una línea.
- **list_n**: lista para guardar los números.
- **Caso base:** cuando `n = 0`, la función se detendrá.
- **Llamada recursiva:** imprime el número actual y luego llama a la función con `n - 1`.


### 2. [Suma recursiva](/assets/exercise02.png)
Escribe una función recursiva que calcule la suma de todos los números enteros positivos desde 1 hasta `n`.
- **list_n**: lista para guardar los números.
- **Caso base:** cuando `n = 1`, la función devolverá el valor `1`.
- **Llamada recursiva:** cuando `n > 1`, la función devolverá la suma de `n` y la función recursiva llamada con `n - 1`.

### 3. [Número par o impar](/assets/exercise03.png)
Determina recursivamente si un número es par o impar.
- **Caso base:** cuando `n = 1`, el número es impar.
- **Llamada recursiva:** cuando `n > 1`, el número es impar si `n` es divisible entre 2, y par si no lo es.

### 4. [Invertir cadena](/assets/exercise04.png)
Crea una función recursiva que reciba una cadena de texto y la invierta, utilizando slicing.
- **Caso base:** si la cadena tiene un solo carácter, la función devolverá la misma cadena.
- **Caso propuesto:** si la cadena está vacía, la función devolverá `no hay caracteres.`
- **Llamada recursiva:** si la cadena tiene más de un carácter, la función devolverá la cadena invertida, con el carácter de la posición `i` invertido y el resto de caracteres.

### 5. [Potencia de un número](/assets/exercise05.png)
Implementa una función recursiva para calcular la potencia de un número, donde `a` es la base y `b` es el exponente.
- **Caso base:** si `b = 0`, la función devolverá `1`.
- **Caso propuesto:** si `b = 1`, la función devolverá `a`.
- **Llamada recursiva:** si `b > 0`, la función devolverá `a * potencia(a, b - 1)`.

Cada una de estas funciones debe estar dentro de una clase en Python y ser parte del menú principal del programa para facilitar la interacción del usuario.