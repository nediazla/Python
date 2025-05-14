# Dia 7: loops

## Loops

La vida está llena de rutinas. En programación también realizamos muchas tareas repetitivas. Para manejar tareas repetitivas, los lenguajes de programación utilizan bucles. El lenguaje de programación Python también proporciona los siguientes tipos de bucles:

1. bucle while
2. bucle for

### Bucle While

Usamos la palabra reservada while para crear un bucle while. Se utiliza para ejecutar un bloque de instrucciones repetidamente hasta que se cumpla una condición dada. Cuando la condición se vuelve falsa, las líneas de código posteriores al bucle continuarán ejecutándose.

```python
  # syntax
  while condition:
    code goes here
```

**Ejemplo:**

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
```

En el bucle while anterior, la condición se vuelve falsa cuando el conteo es 5. En ese momento, el bucle se detiene.
Si nos interesa ejecutar un bloque de código una vez que la condición ya no es verdadera, podemos usar else.

```python
  # syntax
  while condition:
    code goes here
else:
    code goes here
```

**Ejemplo:**

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
	print(count)
```

La condición de bucle anterior será falsa cuando el conteo sea 5 y el bucle se detenga y la ejecución inicie la instrucción else. Como resultado, se imprimirá 5.

### Break y Continue - Parte 1

- Break: usamos break cuando queremos salir del bucle o detenerlo.

```python
# syntax
while condition:
    code goes here
    if another_condition:
        break
```

**Ejemplo:**

```python
count = 0
while count < 5:
    print(count)
    count = count + 1    
    if count == 3:
        break
```

El bucle while anterior solo imprime 0, 1, 2, pero cuando llega a 3 se detiene.

- Continuar: con la instrucción continue podemos omitir la iteración actual y continuar con la siguiente:

```python
  # syntax
  while condition:
    code goes here
    if another_condition:
        continue
```

**Ejemplo:**

```python
count = 0
while count < 5:
    if count == 3:
        count = count + 1        
        continue    
        print(count)
    count = count + 1
```

El bucle while anterior solo imprime 0, 1, 2 y 4 (omite 3).

### Bucle For

Se utiliza una palabra clave *for* para crear un bucle for, similar a otros lenguajes de programación, pero con algunas diferencias de sintaxis. El bucle se utiliza para iterar sobre una secuencia (que puede ser una lista, una tupla, un diccionario, un conjunto o una cadena).

- Bucle For con lista

```python
# syntax
for iterator in lst:
    code goes here
```

**Ejemplo:**

```python
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:  
print(number)   
```

- Bucle for con string

```python
# syntax
for iterator in string:
    code goes here
```

**Ejemplo:**

```python
language = 'Python'
for letter in language:
    print(letter)
for i in range(len(language)):
    print(language[i])
```

- Bucle for con tuple

```python
# syntax
for iterator in tpl:
    code goes here
```

**Ejemplo:**

```python
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

- Bucle For con diccionario
Al recorrer un diccionario en bucle, obtendrá la clave del mismo.

```python
  # syntax
  for iterator in dct:
    code goes here
```

**Ejemplo:**

```python
person = {
    'first_name':'Nelson',
    'last_name':'Diaz',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'    }
}
for key in person:
    print(key)
for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out
```

- Loops in set

```python
# syntax
for iterator in st:
    code goes here
```

**Ejemplo:**

```python
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

### Break and Continue - Part 2

Breve recordatorio:
Break: usamos break cuando queremos detener nuestro bucle antes de que se complete.

```python
# syntax
for iterator in sequence:
    code goes here
    if condition:
        break
```

**Ejemplo:**

```python
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```

En el ejemplo anterior, el bucle se detiene cuando llega a 3.

Continuar: usamos continuar cuando queremos omitir algunos de los pasos en la iteración del bucle.

```python
  # syntax
  for iterator in sequence:
    code goes here
    if condition:
        continue
```

**Ejemplo:**

```python
numeros = (0,1,2,3,4,5)

for numero in numeros:
   print(numero)
    if numero == 3:
       continue
   if numero != 5:
       print('el siguiente numero es: ', numero + 1)
   else:
       print('termina el loop')
```

En el ejemplo anterior, si el número es igual a 3, se omite el paso *posterior* a la condición (pero dentro del bucle) y la ejecución del bucle continúa si quedan iteraciones.

### La función Range

La función *range()* se utiliza para listas de números. *range(start, end, step)* toma tres parámetros: inicio, fin e incremento. De forma predeterminada, comienza desde 0 y el incremento es 1. La secuencia range necesita al menos 1 argumento (fin).
Creación de secuencias utilizando range

```python
lst = list(range(11))
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}
```

```python
# syntax
for iterator in range(start, end, step):
```

**Ejemplo:**

```python
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
```

### Bucle For anidado

Podemos escribir bucles dentro de un bucle.

```python
# syntax
for x in y:
    for t in x:
        print(t)
```

**Ejemplo:**

```python
person = {
    'first_name': 'Nelson',
    'last_name': 'Diaz',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

### For Else

Si queremos ejecutar algún mensaje cuando finaliza el bucle, utilizamos else.

```python
# syntax
for iterator in range(start, end, step):
    do something
else:
    print('The loop ended')
```

**Ejemplo:**

```python
for number in range(11):
    print(number)  
    else:
    print('The loop stops at', number)
```

### Pass

En Python, cuando se requiere una declaración (después del punto y coma), pero no queremos ejecutar ningún código allí, podemos escribir la palabra pass para evitar errores. También podemos usarla como un marcador de posición para declaraciones futuras.

**Ejemplo:**

```python
for number in range(6):
    pass
```

🌕 Has marcado un hito importante, eres imparable. ¡Sigue así! Acabas de completar los desafíos del día 10 y estás 10 pasos por delante en tu camino hacia la grandeza. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## 💻 Ejercicios: Día 10

### Ejercicios: Nivel 1

1. Itera de 0 a 10 usando el bucle for, haz lo mismo usando el bucle while.
2. Itera de 10 a 0 usando el bucle for, haz lo mismo usando el bucle while.
3. Escribe un bucle que haga siete llamadas a print(), de modo que obtengamos en la salida el siguiente triángulo:

```python
  #  
  ##  
  ###  
  ####  
  #####  
  ######  
  #######
```

1. Utilice bucles anidados para crear lo siguiente:
    
    ```bash
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    # # # # # # # #
    ```
    
2. Imprima el siguiente patrón:
    
    ```bash
    0 x 0 = 0
    1 x 1 = 1
    2 x 2 = 4
    3 x 3 = 9
    4 x 4 = 16
    5 x 5 = 25
    6 x 6 = 36
    7 x 7 = 49
    8 x 8 = 64
    9 x 9 = 81
    10 x 10 = 100
    ```
    
3. Recorra la lista [‘Python’, ‘Numpy’, ‘Pandas’, ‘Django’, ‘Flask’] mediante un bucle for e imprima los elementos.
4. Utilice el bucle for para iterar de 0 a 100 e imprimir solo números pares
5. Utilice el bucle for para iterar de 0 a 100 e imprimir solo números impares

### Ejercicios: Nivel 2

1. Utilice el bucle for para iterar de 0 a 100 e imprimir la suma de todos los números.

```bash
The sum of all numbers is 5050.
```

1. Utilice el bucle for para iterar de 0 a 100 e imprimir la suma de todos los números pares y la suma de todos los números impares.
    
    ```bash
    The sum of all evens is 2550. And the sum of all odds is 2500.
    ```
    

### Ejercicios: Nivel 3

1. Ve a la carpeta de datos y usa el archivo [countries.py](https://github.com/nediazla/Python/blob/main/data/countries.py). Recorre los países y extrae todos los países que contengan la palabra *land*.
2. Esta es una lista de frutas, [‘banana’, ‘orange’, ‘mango’, ‘lemon’] invierte el orden usando loop.
3. Ve a la carpeta de datos y usa el archivo [countries_data.py](https://github.com/nediazla/Python/blob/main/data/countries-data.py).
4. ¿Cuál es el número total de idiomas en los datos?
5. Encuentra los diez idiomas más hablados a partir de los datos
6. Encuentra los 10 países más poblados del mundo

🎉 ¡FELICITACIONES! 🎉
