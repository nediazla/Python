# Dia 14: Manejo de excepciones

## Manejo de excepciones

Python utiliza *try* y *except* para manejar los errores con elegancia. Una salida elegante (o manejo elegante) de errores es un modismo de programación simple: un programa detecta una condición de error grave y "sale elegantemente", de manera controlada como resultado. A menudo, el programa imprime un mensaje de error descriptivo en una terminal o registro como parte de la salida elegante, esto hace que nuestra aplicación sea más robusta. La causa de una excepción a menudo es externa al programa en sí. Un ejemplo de excepciones podría ser una entrada incorrecta, un nombre de archivo incorrecto, no poder encontrar un archivo, un dispositivo de E/S que funciona mal. El manejo elegante de errores evita que nuestras aplicaciones se bloqueen.

Hemos cubierto los diferentes tipos de *error* de Python en la sección anterior. Si usamos *try* y *except* en nuestro programa, entonces no generará errores en esos bloques.

![](img/30-Days-Of-Pythonimagestry_except.png)

Probar y aceptar

```python
try:
    code in this block if things go well
except:
    code in this block run if things go wrong
```

**Ejemplo:**

```python
try:
    print(10 + '5')
except:
    print('Something went wrong')
```

En el ejemplo anterior, el segundo operando es una cadena. Podríamos cambiarlo a float o int para agregarlo con el número y que funcione. Pero sin ningún cambio, se ejecutará el segundo bloque, *except*.

**Ejemplo:**

```python
try:
    # Solicitar el nombre y el año de nacimiento
    name = input('Enter your name: ')
    year_born = int(input('Year you were born: '))  # Convertir la entrada a entero
    age = 2019 - year_born  # Calcular la edad
    print(f'You are {name}. And your age is {age}.')  # Imprimir el nombre y la edad
except ValueError:  # Capturar errores específicos de conversión
    print('Invalid input. Please enter a valid number for the year you were born.')
except Exception as e:  # Capturar cualquier otro error
    print(f'Something went wrong: {e}')

```

En el ejemplo anterior, se ejecutará el bloque de excepción y no sabemos exactamente cuál es el problema. Para analizar el problema, podemos utilizar los diferentes tipos de error con except.

En el siguiente ejemplo, se manejará el error y también nos dirá el tipo de error generado.

```python
try:
    # Solicitar el nombre y el año de nacimiento
    name = input('Enter your name: ')
    year_born = int(input('Year you were born: '))  # Convertir la entrada a un entero
    age = 2019 - year_born  # Calcular la edad
    print(f'You are {name}. And your age is {age}.')  # Imprimir el nombre y la edad
except TypeError:
    print('Type error occurred')
except ValueError:
    print('Value error occurred')  # Esto captura si la conversión de año falla
except Exception as e:
    print(f'Something went wrong: {e}')
```

En el código anterior, la salida será TypeError.
Ahora, agreguemos un bloque adicional:

```python
try:
    # Solicitar el nombre y el año de nacimiento
    name = input('Enter your name: ')
    year_born = input('Year you were born: ')
    
    # Convertir el año a entero y calcular la edad
    age = 2019 - int(year_born)
    
    print(f'You are {name}. And your age is {age}.')
    
except ValueError:  # Si no se puede convertir el año a entero
    print('Value error occurred. Please enter a valid number for the year you were born.')

except TypeError:  # En caso de que algo no sea del tipo esperado
    print('Type error occurred.')

else:
    # Si no ocurre ninguna excepción, esta parte del código se ejecuta
    print('I usually run with the try block')

finally:
    # Este bloque siempre se ejecuta, sin importar si hubo error o no
    print('I always run.')
```

También se puede acortar el código anterior de la siguiente manera:

```python
try:
    # Solicitar el nombre y el año de nacimiento
    name = input('Enter your name: ')
    year_born = input('Year you were born: ')
    
    # Convertir el año a entero y calcular la edad
    age = 2019 - int(year_born)
    
    # Mostrar el nombre y la edad
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    # Capturar cualquier excepción y mostrar el error
    print(f'An error occurred: {e}')

```

## Empaquetado y desempaquetado de argumentos en Python

Usamos dos operadores:

- para tuplas
- para diccionarios

Tomemos como ejemplo lo siguiente. Solo se necesitan argumentos, pero tenemos una lista. Podemos desempaquetar la lista y cambiar los argumentos.

### Desempaquetado

### Desempaquetado de listas

```python
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]

# Desempaquetando la lista para pasar los valores individualmente
print(sum_of_five_nums(*lst))  # Esto imprimirá: 15
```

Cuando ejecutamos este código, se genera un error porque esta función toma números (no una lista) como argumentos. Descomprimamos/desestructuremos la lista.

```python
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # Esto imprimirá: 15
```

También podemos utilizar la función de desempaquetado en el rango incorporado que espera un inicio y un final.

```python
numbers = range(2, 7)  # llamada normal con argumentos separados
print(list(numbers))  # [2, 3, 4, 5, 6]

args = [2, 7]
numbers = range(*args)  # llamada con argumentos desempaquetados desde una lista
print(list(numbers))  # [2, 3, 4, 5, 6]
```

Una lista o una tupla también se puede descomprimir de la siguiente manera:

```python
# Lista de países
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)  # Esperado: Finland Sweden Norway ['Denmark', 'Iceland']

# Lista de números
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)  # Esperado: 1 [2, 3, 4, 5, 6] 7
```

### Desempaquetando diccionarios

```python
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'

dct = {'name': 'Nelson', 'country': 'Espana', 'city': 'Caceres', 'age': 250}
print(unpacking_person_info(**dct))  # Esto imprimirá: Nelson lives in Espana, Caceres. He is 250 year old.
```

### Empaquetado

A veces, nunca sabemos cuántos argumentos se deben pasar a una función de Python. Podemos usar el método de empaquetado para permitir que nuestra función acepte una cantidad ilimitada o arbitraria de argumentos.

### Listas de empaquetado

```python
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s

print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```

### Diccionarios de embalaje

```python
def packing_person_info(**kwargs):
    # Verificar si kwargs es un diccionario (aunque siempre lo será, es una buena práctica confirmarlo)
    if isinstance(kwargs, dict):
        print(f"Tipo de kwargs: {type(kwargs)}")  # Imprime el tipo de kwargs
        # Iterar sobre el diccionario y mostrar cada clave y su valor correspondiente
        for key, value in kwargs.items():
            print(f"{key} = {value}")
    else:
        print("Error: Se esperaba un diccionario.")

    return kwargs  # Retorna el diccionario kwargs

# Llamada a la función con datos de ejemplo
print(packing_person_info(name="Nelson", country="Finland", city="Helsinki", age=250))

```

## Propagación en Python

Al igual que en JavaScript, la propagación es posible en Python. Comprobémoslo con el siguiente ejemplo:

```python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)  # [0, 1, 2, 3, 4, 5, 6, 7]

country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
```

## Enumerar

Si nos interesa el índice de una lista, utilizamos la función incorporada *enumerate* para obtener el índice de cada elemento de la lista.

```python
for index, item in enumerate([20, 30, 40]):
    print(index, item)
```

```python
countries = ['Sweden', 'Finland', 'Norway', 'Denmark']

for index, i in enumerate(countries):
    print('hi')
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')
```

## Zip

A veces nos gustaría combinar listas al recorrerlas en bucle. Vea el siguiente ejemplo:

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']

fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit': f, 'veg': v})

print(fruits_and_veges)
```

🌕 Estás decidido. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## Ejercicios: Día 14

1. names = [‘Finlandia’, ‘Suecia’, ‘Noruega’, ‘Dinamarca’, ‘Islandia’, ‘Estonia’, ‘Rusia’]. Descomprime los primeros cinco países y guárdalos en una variable nordic_countries, guarda Estonia y Rusia en es y ru respectivamente.

🎉 ¡FELICIDADES! 🎉