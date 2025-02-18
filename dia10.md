# Dia 10: list comprehension

## Comprensión de listas
La comprensión de listas en Python es una forma compacta de crear una lista a partir de una secuencia. Es una forma abreviada de crear una nueva lista. La comprensión de listas es considerablemente más rápida que procesar una lista utilizando el bucle *for*.

```python
# syntax
[i for i in iterable if expression]
```

**Ejemplo: 1**
Por ejemplo, si desea convertir una cadena en una lista de caracteres, puede utilizar un par de métodos. Veamos algunos de ellos:

```python
# Primer método: Convertir un string a lista usando la función `list()`
language = 'Python'
lst = list(language)  # Convierte el string en una lista de caracteres
print(type(lst))  # Debería mostrar <class 'list'>
print(lst)  # Imprime ['P', 'y', 't', 'h', 'o', 'n']

# Segundo método: Usando comprensión de listas
lst = [i for i in language]  # Crea una lista de caracteres usando list comprehension
print(type(lst))  # Debería mostrar <class 'list'>
print(lst)  # Imprime ['P', 'y', 't', 'h', 'o', 'n']
```

**Ejemplo:2**
Por ejemplo, si desea generar una lista de números
```python
# Generando números del 0 al 10 usando comprensión de listas
numbers = [i for i in range(11)]  # Genera una lista con números del 0 al 10
print(numbers)  # Imprime [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Realizando operaciones matemáticas durante la iteración: cuadrados de los números
squares = [i * i for i in range(11)]  # Genera una lista con los cuadrados de los números del 0 al 10
print(squares)  # Imprime [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Creando una lista de tuplas (número, cuadrado del número)
numbers_and_squares = [(i, i * i) for i in range(11)]  # Cada elemento es una tupla (número, cuadrado)
print(numbers_and_squares)  # Imprime [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36), (7, 49), (8, 64), (9, 81), (10, 100)]
```

**Ejemplo: 2**
La comprensión de listas se puede combinar con la expresión if
```python
# Generando números pares en el rango de 0 a 20
even_numbers = [i for i in range(21) if i % 2 == 0]  # Genera una lista de números pares en el rango de 0 a 20
print(even_numbers)  # Imprime [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generando números impares en el rango de 0 a 20
odd_numbers = [i for i in range(21) if i % 2 != 0]  # Genera una lista de números impares en el rango de 0 a 20
print(odd_numbers)  # Imprime [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Filtrando números positivos y pares de una lista
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]  # Lista de números con valores negativos y positivos
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]  # Filtra los números positivos y pares
print(positive_even_numbers)  # Imprime [4, 6, 8, 10]

# Aplanando una lista tridimensional (listas dentro de listas)
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Lista tridimensional
flattened_list = [number for row in list_of_lists for number in row]  # Aplana la lista
print(flattened_list)  # Imprime [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Función Lambda
La función Lambda es una pequeña función anónima sin nombre. Puede aceptar cualquier cantidad de argumentos, pero solo puede tener una expresión. La función Lambda es similar a las funciones anónimas en JavaScript. La necesitamos cuando queremos escribir una función anónima dentro de otra función.

### Creación de una función Lambda
Para crear una función Lambda, usamos la palabra clave *lambda* seguida de uno o más parámetros, seguidos de una expresión. Vea la sintaxis y el ejemplo a continuación. La función Lambda no usa return, pero devuelve explícitamente la expresión.

```python
# syntax
x = lambda param1, param2, param3: param1 + param2 + param2
print(x(arg1, arg2, arg3))
```

**Ejemplo:**
```python
# Función nombrada
def add_two_nums(a, b):
    return a + b
print(add_two_nums(2, 3))  # Imprime 5

# Cambiamos la función anterior a una función lambda
add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))  # Imprime 5

# Función lambda autoejecutable
print((lambda a, b: a + b)(2, 3))  # Imprime 5

# Función lambda para calcular el cuadrado
square = lambda x: x ** 2
print(square(3))  # Imprime 9

# Función lambda para calcular el cubo
cube = lambda x: x ** 3
print(cube(3))  # Imprime 27

# Función lambda con múltiples variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3))  # Imprime 22
```

### Función Lambda dentro de otra función
Uso de una función Lambda dentro de otra función.
```python
# Función que retorna una función lambda que calcula la potencia
def power(x):
    return lambda n: x ** n

# Usando la función power para calcular el cubo de 2 (2^3)
cube = power(2)(3)  # power(2) devuelve una función lambda, que luego se ejecuta con el argumento 3
print(cube)  # Imprime 8

# Usando la función power para calcular 2^5
two_power_of_five = power(2)(5)  # power(2) devuelve una función lambda, que luego se ejecuta con el argumento 5
print(two_power_of_five)  # Imprime 32
```

🌕 ¡Sigue así! ¡No dejes de insistir, el cielo es el límite! Acabas de completar los desafíos del día 10 y estás 10 pasos por delante en tu camino hacia la grandeza. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## 💻 Ejercicios: Día 10
1. Filtrar solo los negativos y ceros en la lista usando la comprensión de listas
    
```python
    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
```
    
2. Aplanar la siguiente lista de listas de listas a una lista unidimensional:
    
```python
    list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
    output
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
    
3. Usando la comprensión de listas, cree la siguiente lista de tuplas:
    
```python
    [(0, 1, 0, 0, 0, 0, 0),
    (1, 1, 1, 1, 1, 1, 1),
    (2, 1, 2, 4, 8, 16, 32),
    (3, 1, 3, 9, 27, 81, 243),
    (4, 1, 4, 16, 64, 256, 1024),
    (5, 1, 5, 25, 125, 625, 3125),
    (6, 1, 6, 36, 216, 1296, 7776),
    (7, 1, 7, 49, 343, 2401, 16807),
    (8, 1, 8, 64, 512, 4096, 32768),
    (9, 1, 9, 81, 729, 6561, 59049),
    (10, 1, 10, 100, 1000, 10000, 100000)]
```
    
4. Aplanar la siguiente lista para formar una nueva lista:
    
```python
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
```
    
5. Cambie la siguiente lista a una lista de diccionarios:
    
```python
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output:
[{'country': 'FINLAND', 'city': 'HELSINKI'},
{'country': 'SWEDEN', 'city': 'STOCKHOLM'},
{'country': 'NORWAY', 'city': 'OSLO'}]
```
    
6. Cambie la siguiente lista de listas a una lista de cadenas concatenadas:
    
```python
    names = [[('Nelson', 'Diaz')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
    output
    ['Nelson Diaz', 'David Smith', 'Donald Trump', 'Bill Gates']
```
    
7. Escribe una función lambda que pueda resolver una pendiente o una intersección con el eje y de funciones lineales.

🎉 ¡FELICITACIONES! 🎉