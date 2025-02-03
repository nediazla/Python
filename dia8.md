# Dia 8: functions

## Funciones

Hasta ahora hemos visto muchas funciones integradas de Python. En esta sección, nos centraremos en las funciones personalizadas. ¿Qué es una función? Antes de empezar a crear funciones, aprendamos qué es una función y por qué las necesitamos.

### Definición de una función

Una función es un bloque de código reutilizable o declaraciones de programación diseñadas para realizar una determinada tarea. Para definir o declarar una función, Python proporciona la palabra clave *def*. La siguiente es la sintaxis para definir una función. El bloque de código de la función se ejecuta solo si se llama o invoca la función.

### Declaración y llamada de una función

Cuando creamos una función, la llamamos declarando una función. Cuando empezamos a usarla, la llamamos *llamando* o *invocando* una función. La función se puede declarar con o sin parámetros.

```python
# syntax
# Declaring a function
def function_name():
    codes
    codes
# Calling a functionfunction_name()
```

### Función sin parámetros

La función se puede declarar sin parámetros.

**Ejemplo:**

```python
def generate_full_name ():
    first_name = 'Nelson'    
    last_name = 'Diaz'    
    pace = ' '    
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function
def add_two_numbers ():
    num_one = 2    
    num_two = 3    
    total = num_one + num_two
    print(total)
add_two_numbers()
```

### Función que devuelve un valor - Parte 1

La función también puede devolver valores. Si una función no tiene una declaración de retorno, el valor de la función es Ninguno. Reescribamos las funciones anteriores utilizando la instrucción de retorno. A partir de ahora, obtenemos un valor de una función cuando la llamamos y la imprimimos.

```python
def generate_full_name ():
    first_name = 'Nelson'    
    last_name = 'Diaz'    
    space = ' '    
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
def add_two_numbers ():
    num_one = 2    
    num_two = 3    
    total = num_one + num_two
    return total
print(add_two_numbers())
```

### Función con parámetros

En una función podemos pasar distintos tipos de datos (número, cadena, booleano, lista, tupla, diccionario o conjunto) como parámetro

- Un solo parámetro: si nuestra función acepta un parámetro, debemos llamar a nuestra función con un argumento

```python
  # syntax  
  # Declaring a function  
  def function_name(parameter):
    codes
    codes
  # Calling function  
  print(function_name(argument))
```

**Ejemplo:**

```python
def greetings (name):
    message = name + ', welcome to Python for Everyone!'    
    return message
print(greetings('Nelson'))
def add_ten(num):
    ten = 10    return num + ten
print(add_ten(90))
def square_number(x):
    return x * x
print(square_number(2))
def area_of_circle (r):
    PI = 3.14    area = PI * r ** 2    
    return area
print(area_of_circle(10))
def sum_of_numbers(n):
    total = 0    for i in range(n+1):
        total+=i
    print(total)
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

- Dos parámetros: una función puede tener o no uno o más parámetros. Una función también puede tener dos o más parámetros. Si nuestra función acepta parámetros, debemos llamarla con argumentos. Veamos una función con dos parámetros:

```python
  # syntax  
  # Declaring a function  
  def function_name(para1, para2):
    codes
    codes
  # Calling function  
  print(function_name(arg1, arg2))
```

**Ejemplo:**

```python
def generate_full_name (first_name, last_name):
    space = ' '      full_name = first_name + space + last_name
      return full_name
print('Full Name: ', generate_full_name('Nelson','Diaz'))
def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sumprint('Sum of two numbers: ', sum_two_numbers(1, 9))
def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;print('Age: ', calculate_age(2021, 1819))
def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N'    
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
```

### Pasar argumentos con clave y valor

Si pasamos los argumentos con clave y valor, el orden de los argumentos no importa.

```python
# syntax
# Declaring a function
def function_name(para1, para2):
    codes
    codes
# Calling function
print(function_name(para1 = 'John', para2 = 'Doe'))
```

**Ejemplo:**

```python
def print_fullname(firstname, lastname):
    space = ' '    full_name = firstname  + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Nelson', lastname = 'Diaz'))
def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2))
```

### Función que devuelve un valor - Parte 2

Si no devolvemos un valor con una función, entonces nuestra función devuelve *None* de manera predeterminada. Para devolver un valor con una función, usamos la palabra clave *return* seguida de la variable que estamos devolviendo. Podemos devolver cualquier tipo de datos desde una función.

- Devolver una cadena:
**Ejemplo:**

```python
def print_name(firstname):
    return firstname
print_name('Nelson') # Nelsondef print_full_name(firstname, lastname):
    space = ' '    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Nelson', lastname='Diaz')
```

- Devolviendo un número:

**Ejemplo:**

```python
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))
def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;print('Age: ', calculate_age(2019, 1819))
```

- Devolviendo un valor booleano:
**Ejemplo:**

```python
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True   
        return Falseprint(is_even(10)) # True
        print(is_even(7)) # False
```

- Devolviendo una lista:
**Ejemplo:**

```python
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

### Función con parámetros predeterminados

A veces, pasamos valores predeterminados a los parámetros cuando invocamos la función. Si no pasamos argumentos al llamar a la función, se utilizarán sus valores predeterminados.

```python
# syntax
# Declaring a function
def function_name(param = value):
    codes
    codes
# Calling function
function_name()
function_name(arg)
```

**Ejemplo:**

```python
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'    
    return message
print(greetings())
print(greetings('Nelson'))
def generate_full_name (first_name = 'Nelson', last_name = 'Diaz'):
    space = ' '    
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())
print(generate_full_name('David','Smith'))
def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age;
    print('Age: ', calculate_age(1821))
def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' 
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100))
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62))
```

### Número arbitrario de argumentos

Si no conocemos el número de argumentos que pasamos a nuestra función, podemos crear una función que pueda aceptar un número arbitrario de argumentos agregando * antes del nombre del parámetro.

```python
# syntax
# Declaring a function
def function_name(*args):
    codes
    codes
# Calling function
function_name(param1, param2, param3,..)
```

**Ejemplo:**

```python
def sum_all_nums(*nums):
    total = 0    for num in nums:
        total += num      
        return total
print(sum_all_nums(2, 3, 5))
```

### Número de parámetros predeterminados y arbitrarios en funciones

```python
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
print(generate_groups('Team-1','Nelson','Brook','David','Eyob'))
```

### Función como parámetro de otra función

```python
#You can pass functions around as parameters
def square_number (n):
    return n * n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

🌕 Has logrado mucho hasta ahora. ¡Sigue así! Acabas de completar los desafíos del día 11 y estás 11 pasos por delante en tu camino hacia la grandeza. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## 💻 Ejercicios: Día 11

### Ejercicios: Nivel 1

1. Declara una función *add_two_numbers*. Toma dos parámetros y devuelve una suma.
2. El área de un círculo se calcula de la siguiente manera: área = π x r x r. Escribe una función que calcule *area_of_circle*.
3. Escribe una función llamada add_all_nums que tome una cantidad arbitraria de argumentos y sume todos los argumentos. Comprueba si todos los elementos de la lista son de tipo numérico. Si no es así, da una respuesta razonable.
4. La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. Escribe una función que convierta °C a °F, *convert_celsius_to-fahrenheit*.
5. Escribe una función llamada check-season, que toma un parámetro de mes y devuelve la estación: otoño, invierno, primavera o verano.
6. Escribe una función llamada calculate_slope que devuelve la pendiente de una ecuación lineal.
7. La ecuación cuadrática se calcula de la siguiente manera: ax² + bx + c = 0. Escribe una función que calcule el conjunto de soluciones de una ecuación cuadrática, *solve_quadratic_eqn*.
8. Declara una función llamada print_list. Toma una lista como parámetro e imprime cada elemento de la lista.
9. Declara una función llamada reverse_list. Toma una matriz como parámetro y devuelve el reverso de la matriz (usa bucles).

```python
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list1(["A", "B", "C"]))

```

1. Declara una función llamada capitalize_list_items. Esta toma una lista como parámetro y devuelve una lista de elementos en mayúsculas.
2. Declara una función llamada add_item. Esta toma una lista y un elemento como parámetros. Devuelve una lista con el elemento agregado al final.

```python
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))
```

1. Declara una función llamada remove_item. Esta toma como parámetros una lista y un elemento. Devuelve una lista con el elemento eliminado de ella.

```python
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango')) 
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))
```

1. Declara una función denominada suma_de_números. Esta función toma un parámetro numérico y suma todos los números de ese rango.

```python
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

1. Declara una función llamada suma_de_números_impares. Esta función toma un parámetro numérico y suma todos los números impares en ese rango.
2. Declara una función llamada suma_de_números_pares. Esta función toma un parámetro numérico y suma todos los números pares en ese rango.

### Ejercicios: Nivel 2

1. Declara una función llamada evens_and_odds . Toma un entero positivo como parámetro y cuenta la cantidad de pares e impares en el número.

```python
    print(evens_and_odds(100))
    # The number of odds are 50.    
    # The number of evens are 51.
```

1. Llama a tu función factorial, toma un número entero como parámetro y devuelve un factorial del número
2. Llama a tu función *is_empty*, toma un parámetro y verifica si está vacío o no
3. Escribe diferentes funciones que tomen listas. Deben calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (desviación estándar).

### Ejercicios: Nivel 3

1. Escribe una función llamada is_prime, que verifique si un número es primo.
2. Escribe una función que verifique si todos los elementos son únicos en la lista.
3. Escribe una función que verifique si todos los elementos de la lista son del mismo tipo de datos.
4. Escribe una función que verifique si la variable proporcionada es una variable de Python válida
5. Ve a la carpeta de datos y accede al archivo [countries-data.py](https://github.com/nediazla/Python/blob/main/data/countries-data.py).
- Crea una función llamada the most_spoken_languages ​​in the world. Debería devolver 10 o 20 de los idiomas más hablados del mundo en orden descendente
- Crea una función llamada the most_populated_countries. Debería devolver 10 o 20 de los países más poblados en orden descendente.

🎉 ¡FELICITACIONES! 🎉