# Dia 6: conditionales

## Condicionales

De manera predeterminada, las sentencias en un script de Python se ejecutan secuencialmente de arriba hacia abajo. Si la lógica de procesamiento así lo requiere, el flujo secuencial de ejecución se puede alterar de dos maneras:

- Ejecución condicional: se ejecutará un bloque de una o más sentencias si una determinada expresión es verdadera
- Ejecución repetitiva: se ejecutará un bloque de una o más sentencias de manera repetitiva siempre que una determinada expresión sea verdadera. En esta sección, cubriremos las sentencias *if*, *else*, *elif*. Los operadores lógicos y de comparación que aprendimos en las secciones anteriores serán útiles aquí.

### Condición If

En Python y otros lenguajes de programación, la palabra clave *if* se usa para verificar si una condición es verdadera y para ejecutar el código del bloque. Recuerde la sangría después de los dos puntos.

```python
# syntax
if condition:
    this part of code runs for truthy conditions
```

**Ejemplo: 1**

```python
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
```

Como puede ver en el ejemplo anterior, 3 es mayor que 0. La condición era verdadera y se ejecutó el código de bloque. Sin embargo, si la condición es falsa, no vemos el resultado. Para ver el resultado de la condición falsa, deberíamos tener otro bloque, que será else.

### If Else

Si la condición es verdadera se ejecutará el primer bloque, si no se ejecutará la condición else.

```python
# syntax
if condition:
    this part of code runs for truthy conditions
else:
     this part of code runs for false conditions
```

**Ejemplo:**

```python
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
```

La condición anterior resulta falsa, por lo tanto, se ejecutó el bloque else. ¿Qué sucede si nuestra condición es mayor de dos? Podríamos usar elif.

### If Elif Else

En nuestra vida diaria, tomamos decisiones a diario. No tomamos decisiones verificando una o dos condiciones, sino múltiples. Al igual que la vida, la programación también está llena de condiciones. Usamos elif cuando tenemos múltiples condiciones.

```python
# syntax
if condition:
    code
elif condition:
    code
else:
    code
```

**Ejemplo:**

```python
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
```

### Taquigrafía

```python
# syntax
code if condition else code
```

**Ejemplo:**

```python
a = 3
print('A is positive') if a > 0 else print('A is negative')
```

### Condiciones anidadas

Las condiciones se pueden anidar

```python
# syntax
if condition:
    code
    if condition:
    code
```

**Ejemplo:**

```python
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
```

Podemos evitar escribir condiciones anidadas utilizando el operador lógico *and*.

### Condición If y operadores lógicos

```python
# syntax
if condition and condition:
    code
```

**Ejemplo:**

```python
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
```

### Operadores lógicos If y Or

```python
# syntax
if condition or condition:
    code
```

**Ejemplo:**

```python
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
```

🌕 Lo estás haciendo muy bien. Nunca te rindas porque las grandes cosas llevan tiempo. Acabas de completar los desafíos del día 9 y estás 9 pasos adelante en tu camino hacia la grandeza. Ahora haz algunos ejercicios para tu cerebro y músculos.

## 💻 Ejercicios: Día 9

### Ejercicios: Nivel 1

1. Obtén la información del usuario usando input(“Ingresa tu edad:”). Si el usuario tiene 18 años o más, envía comentarios: Tienes la edad suficiente para conducir. Si tienes menos de 18 años, envía comentarios para esperar la cantidad de años que falta. Resultado:
    
    ```python
    Enter your age: 30
    You are old enough to learn to drive.
    Output:Enter your age: 15
    You need 3 more years to learn to drive.
    ```
    
2. Compara los valores de my_age y your_age usando if … else. ¿Quién es mayor (tú o yo)? Usa input(“Ingresa tu edad:”) para obtener la edad como entrada. Puedes usar una condición anidada para imprimir ‘year’ para una diferencia de edad de 1 año, ‘years’ para diferencias mayores y un texto personalizado si my_age = your_age. Salida:
    
    ```python
    Enter your age: 30
    You are 5 years older than me.
    ```
    
3. Obtener dos números del usuario mediante el mensaje de entrada. Si a es mayor que b, devolver a es mayor que b; si a es menor que b, devolver a es menor que b; de lo contrario, a es igual a b. Salida:
    
    ```python
    Enter number one: 4
    Enter number two: 3
    4 is greater than 3
    ```
    

### 

```python
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
```

### Ejercicios: Nivel 2

1. Escribe un código que califique a los estudiantes según sus puntuaciones:

```python
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
```

1. Comprueba si la estación es Otoño, Invierno, Primavera o Verano. Si la entrada del usuario es:
Septiembre, Octubre o Noviembre, la estación es Otoño.
Diciembre, Enero o Febrero, la estación es Invierno.
Marzo, Abril o Mayo, la estación es Primavera.
Junio, Julio o Agosto, la estación es Verano.
2. La siguiente lista contiene algunas frutas:

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
```

Si una fruta no existe en la lista, agréguela a la lista e imprima la lista modificada. Si la fruta existe, imprima ('Esa fruta ya existe en la lista')
```python
### Ejercicios: Nivel 3

1. Aquí tenemos un diccionario de personas. ¡Siéntete libre de modificarlo!

```python
        person={
    'first_name': 'Nelson',
    'last_name': 'Diaz',
    'age': 250,
    'country': 'Espana',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'    }
    }
```

- Verificar si el diccionario de personas tiene la clave de habilidades, si es así, imprimir la habilidad del medio en la lista de habilidades.
- Verificar si el diccionario de personas tiene la clave de habilidades, si es así, verificar si la persona tiene la habilidad 'Python' e imprimir el resultado.
- Si las habilidades de una persona solo tienen JavaScript y React, imprimir ('Él es un desarrollador front-end'), si las habilidades de la persona tienen Node, Python, MongoDB, imprimir ('Él es un desarrollador back-end'), si las habilidades de la persona tienen React, Node y MongoDB, imprimir ('Él es un desarrollador fullstack'), de lo contrario imprimir ('título desconocido') - para obtener resultados más precisos, se pueden anidar más condiciones.
- Si la persona está casada y vive en España, imprimir la información en el siguiente formato:

```python
    Nelson Diaz lives in Espana. He is married.
```

🎉¡FELICIDADES! 🎉