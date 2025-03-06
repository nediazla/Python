# Dia 11: higher order functions

## Funciones de orden superior

En Python, las funciones se consideran ciudadanos de primera clase, lo que permite realizar las siguientes operaciones en las funciones:

- Una función puede tomar una o más funciones como parámetros
- Una función puede devolverse como resultado de otra función
- Una función puede modificarse
- Una función puede asignarse a una variable

En esta sección, cubriremos:

1. Manejo de funciones como parámetros
2. Devolución de funciones como valor de retorno de otras funciones
3. Uso de cierres y decoradores de Python

### Función como parámetro

```python
def sum_numbers(nums):  # Normal function
    return sum(nums)    # Usa la función built-in sum para obtener la suma de los elementos

def higher_order_function(f, lst):  # Función que toma otra función como parámetro
    summation = f(lst)  # Ejecuta la función `f` pasando `lst` como argumento
    return summation

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)  # Imprime 15

```

### Función como valor de retorno

```python
def square(x):  # A function to calculate the square of a number
    return x ** 2

def cube(x):  # A function to calculate the cube of a number
    return x ** 3

def absolute(x):  # A function to calculate the absolute value of a number
    if x >= 0:
        return x
    else:
        return -x

def higher_order_function(type):  # A higher order function returning a function based on the type
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

# Using the higher order function to get the square function and apply it
result = higher_order_function('square')
print(result(3))  # Imprime 9

# Using the higher order function to get the cube function and apply it
result = higher_order_function('cube

```

En el ejemplo anterior, puede ver que la función de orden superior devuelve diferentes funciones según el parámetro que se pasa

## Cierres de Python

Python permite que una función anidada acceda al ámbito externo de la función que la encierra. Esto se conoce como cierre. Veamos cómo funcionan los cierres en Python. En Python, el cierre se crea anidando una función dentro de otra función que la encapsula y luego devolviendo la función interna. Vea el ejemplo a continuación.

**Ejemplo:**

```python
def add_ten():
    ten = 10
    
    # Función interna que usa la variable 'ten' del alcance externo
    def add(num):
        return num + ten
    
    return add

# Llamando a la función add_ten() que devuelve la función 'add'
closure_result = add_ten()

# Probando la función devuelta con diferentes valores
print(closure_result(5))  # Imprime 15
print(closure_result(10))  # Imprime 20
```

## Decoradores de Python

Un decorador es un patrón de diseño en Python que permite a un usuario agregar una nueva funcionalidad a un objeto existente sin modificar su estructura. Los decoradores suelen llamarse antes de la definición de una función que se desea decorar.

### Creación de decoradores

Para crear una función decoradora, necesitamos una función externa con una función contenedora interna.

**Ejemplo:**

```python
# Función normal
def greeting():
    return 'Welcome to Python'

# Decorador para convertir el texto a mayúsculas
def uppercase_decorator(function):
    def wrapper():
        func = function()  # Llama a la función decorada
        make_uppercase = func.upper()  # Convierte el resultado a mayúsculas
        return make_uppercase
    return wrapper

# Aplicando el decorador a la función greeting
@uppercase_decorator
def greeting():
    return 'Welcome to Python'

# Llamando a la función decorada
print(greeting())  # Imprime: WELCOME TO PYTHON
```

### Cómo aplicar varios decoradores a una sola función

```python
# Primer decorador para convertir el texto a mayúsculas
def uppercase_decorator(function):
    def wrapper():
        func = function()  # Llama a la función decorada
        make_uppercase = func.upper()  # Convierte el resultado a mayúsculas
        return make_uppercase
    return wrapper

# Segundo decorador para dividir la cadena en una lista
def split_string_decorator(function):
    def wrapper():
        func = function()  # Llama a la función decorada
        splitted_string = func.split()  # Divide la cadena en palabras
        return splitted_string
    return wrapper

# Aplicando ambos decoradores. Primero se divide la cadena y luego se convierte a mayúsculas
@uppercase_decorator
@split_string_decorator
def greeting():
    return 'Welcome to Python'

# Llamando a la función decorada
print(greeting())  # Imprime: ['WELCOME', 'TO', 'PYTHON']
```

### Aceptación de parámetros en funciones de decorador

La mayoría de las veces necesitamos que nuestras funciones acepten parámetros, por lo que es posible que debamos definir un decorador que acepte parámetros.

```python
# Decorador que acepta parámetros
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)  # Llama a la función original
        print("I live in {}".format(para3))  # Imprime el país después de la función
    return wrapper_accepting_parameters

# Aplicando el decorador
@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(first_name, last_name, country))

# Llamando a la función decorada
print_full_name("Nelson", "Yetayeh", "Finland")
```

## Funciones de orden superior integradas

Algunas de las funciones integradas de orden superior que cubrimos en esta parte son *map()*, *filter* y *reduce*.
La función lambda se puede pasar como parámetro y el mejor caso de uso de las funciones lambda es en funciones como map, filter y reduce.

### Python: función Map

La función map() es una función integrada que toma una función y un iterable como parámetros.

```python
    # syntax    
    map(function, iterable)
```

**Ejemplo 1:**

```python
# Lista de números
numbers = [1, 2, 3, 4, 5]  # iterable

# Función normal para calcular el cuadrado de un número
def square(x):
    return x ** 2

# Aplicando map con la función 'square'
numbers_squared = map(square, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]

# Aplicando map con una función lambda
numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))  # [1, 4, 9, 16, 25]
```

**Ejemplo 2:**

```python
# Lista de números como cadenas
numbers_str = ['1', '2', '3', '4', '5']  # iterable

# Aplicando map para convertir las cadenas en enteros
numbers_int = map(int, numbers_str)

# Imprimiendo la lista de números enteros
print(list(numbers_int))  # [1, 2, 3, 4, 5]
```

**Ejemplo 3:**

```python
# Lista de nombres
names = ['Nelson', 'Lidiya', 'Ermias', 'Abraham']  # iterable

# Función normal para convertir a mayúsculas
def change_to_upper(name):
    return name.upper()

# Aplicando map con la función 'change_to_upper'
names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))  # ['Nelson', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# Aplicando map con una función lambda
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))  # ['Nelson', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

Lo que hace realmente map es iterar sobre una lista. Por ejemplo, cambia los nombres a mayúsculas y devuelve una nueva lista.

### Python - Función de filtro

La función filter() llama a la función especificada que devuelve un valor booleano para cada elemento del iterable (lista) especificado. Filtra los elementos que satisfacen los criterios de filtrado.

```python
    # syntax    
    filter(function, iterable)
```

**Ejemplo 1:**

```python
# Lista de números
numbers = [1, 2, 3, 4, 5]  # iterable

# Función para verificar si un número es par
def is_even(num):
    if num % 2 == 0:
        return True
    return False

# Usando filter para filtrar solo los números pares
even_numbers = filter(is_even, numbers)

# Imprimiendo los números pares
print(list(even_numbers))  # [2, 4]
```

**Ejemplo 2:** 

```python
# Lista de números
numbers = [1, 2, 3, 4, 5]  # iterable

# Función para verificar si un número es impar
def is_odd(num):
    if num % 2 != 0:
        return True
    return False

# Usando filter para filtrar solo los números impares
odd_numbers = filter(is_odd, numbers)

# Imprimiendo los números impares
print(list(odd_numbers))  # [1, 3, 5]
```

```python
# Lista de nombres
names = ['Nelson', 'Lidiya', 'Ermias', 'Abraham']  # iterable

# Función para verificar si el nombre es largo
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

# Usando filter para filtrar solo los nombres largos
long_names = filter(is_name_long, names)

# Imprimiendo los nombres largos
print(list(long_names))  # ['Nelson']
```

### Python - Función Reduce

La función *reduce()* está definida en el módulo functools y debemos importarla desde este módulo. Al igual que map y filter, toma dos parámetros, una función y un iterable. Sin embargo, no devuelve otro iterable, sino un único valor.
**Ejemplo:1**

```python
from functools import reduce  # Importamos reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable

def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
```

## 💻 Ejercicios: Día 11

```python
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Nelson', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Ejercicios: Nivel 1

1. Explica la diferencia entre map, filter y reduce.
2. Explica la diferencia entre función de orden superior, cierre y decorador
3. Define una función de llamada antes de map, filter o reduce, consulta los ejemplos.
4. Utiliza el bucle for para imprimir cada país de la lista de países.
5. Utiliza for para imprimir cada nombre de la lista de nombres.
6. Utiliza for para imprimir cada número de la lista de números.

### Ejercicios: Nivel 2

1. Utiliza map para crear una nueva lista cambiando cada país a mayúscula en la lista de países
2. Utiliza map para crear una nueva lista cambiando cada número a su cuadrado en la lista de números
3. Utiliza map para cambiar cada nombre a mayúscula en la lista de nombres
4. Utiliza filter para filtrar los países que contengan "land".
5. Utiliza filter para filtrar los países que tengan exactamente seis caracteres.
6. Utiliza filter para filtrar los países que contengan seis letras o más en la lista de países.
7. Use filter para filtrar los países que comiencen con una ‘E’
8. Encadene dos o más iteradores de lista (p. ej. arr.map(callback).filter(callback).reduce(callback))
9. Declare una función llamada get_string_lists que tome una lista como parámetro y luego devuelva una lista que contenga solo elementos de cadena.
10. Use reduce para sumar todos los números en la lista de números.
11. Use reduce para concatenar todos los países y producir esta oración: Estonia, Finlandia, Suecia, Dinamarca, Noruega e Islandia son países del norte de Europa
12. Declare una función llamada categorize_countries que devuelva una lista de países con algún patrón común puede encontrar la https://github.com/nediazla/Python/blob/main/data/countries.py
13. Crea una función que devuelva un diccionario, donde las claves representan las letras iniciales de los países y los valores son la cantidad de nombres de países que comienzan con esa letra.
14. Declara una función get_first_ten_countries: devuelve una lista de los primeros diez países de la lista countries.js en la carpeta de datos.
15. Declara una función get_last_ten_countries que devuelva los últimos diez países de la lista de países.

### Ejercicios: Nivel 3

1. Usa el archivo https://github.com/nediazla/Python/blob/main/data/countries-data.py) y sigue las tareas a continuación:
- Ordena los países por nombre, por capital, por población
- Ordena los diez idiomas más hablados por ubicación.
- Ordena los diez países más poblados.

🎉 ¡FELICITACIONES! 🎉

[Estudiantes](laboratorios/estudiantes.py)