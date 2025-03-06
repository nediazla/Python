# Dia12: python type errors

## Tipos de errores de Python

Cuando escribimos código, es común que cometamos un error tipográfico o algún otro error común. Si nuestro código no se ejecuta, el intérprete de Python mostrará un mensaje que contiene información sobre dónde se produce el problema y el tipo de error. También nos dará sugerencias sobre una posible solución. Comprender los diferentes tipos de errores en los lenguajes de programación nos ayudará a depurar nuestro código rápidamente y también nos hará mejores en lo que hacemos.

Veamos los tipos de error más comunes uno por uno. Primero, abramos nuestro shell interactivo de Python. Vaya a la terminal de su computadora y escriba 'python'. Se abrirá el shell interactivo de Python.

### SyntaxErro

**Ejemplo 1: SyntaxError**

```python
C:\Users\Usuario>python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>>
```

Como puedes ver, cometimos un error de sintaxis porque olvidamos encerrar la cadena entre paréntesis y Python ya sugiere la solución. Vamos a solucionarlo.

```python
C:\Users\Usuario>python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
    ^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print('hello world')
hello world
>>>
```

El error era un *SyntaxError*. Después de la corrección, nuestro código se ejecutó sin problemas. Veamos más tipos de errores.
### NameError

**Ejemplo 1: NameError**

```python
PS C:\Users\Usuario> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>>
```

Como puede ver en el mensaje anterior, el nombre age no está definido. Sí, es cierto que no definimos una variable age, pero estábamos tratando de imprimirla como si la hubiéramos declarado. Ahora, solucionemos esto declarándola y asignándole un valor.

```python
PS C:\Users\Usuario> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>> age = 25
>>> print(age)
25
>>>
```

El tipo de error fue un *NameError*. Depuramos el error definiendo el nombre de la variable.
### IndexError

**Ejemplo 1: IndexError**

```python
PS C:\Users\Usuario> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```

En el ejemplo anterior, Python generó un *IndexError*, porque la lista solo tiene índices del 0 al 4, por lo que estaba fuera de rango.
### ModuleNotFoundError

**Ejemplo 1: ModuleNotFoundError**

```python
PS C:\Users\Usuario> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>>
```

En el ejemplo anterior, agregué deliberadamente una s adicional a math y se generó un error ModuleNotFoundError. Vamos a solucionarlo eliminando la s adicional de math.

```python
PS C:\Users\Usuario> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>>
```

Lo hemos corregido, así que usemos algunas de las funciones del módulo de matemáticas.

### AttributeError

**Ejemplo 1: AttributeError**

```python
PS C:\Users\Usuario> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
>>>
```

Como puedes ver, ¡cometí un error otra vez! En lugar de pi, intenté llamar a una función PI desde el módulo de matemáticas. Se generó un error de atributo, es decir, que la función no existe en el módulo. Vamos a solucionarlo cambiando de PI a pi.

```python
PS C:\Users\Usuario> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
>>> math.pi
3.141592653589793
>>>
```

Ahora, cuando llamamos a pi desde el módulo de matemáticas, obtenemos el resultado.
### KeyError

**Ejemplo 1: KeyError**

```python
PS C:\Users\Usuario> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> users = {'name':'nelson', 'age':250, 'country':'Epain'}
>>> users['name']
'nelson'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>>
```

Como puedes ver, hubo un error tipográfico en la clave utilizada para obtener el valor del diccionario. Por lo tanto, se trata de un error de clave y la solución es bastante sencilla. ¡Hagámoslo!

Depuramos el error, nuestro código se ejecutó y obtuvimos el valor.

```python
PS C:\Users\Usuario> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> users = {'name':'nelson', 'age':250, 'country':'Epain'}
>>> users['name']
'nelson'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>> users['country']
'Epain'
>>>
```

### Error de tipo

**Ejemplo 1: Error de tipo**

```python
PS C:\Users\Usuario> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

En el ejemplo anterior, se genera un TypeError porque no podemos agregar un número a una cadena. La primera solución sería convertir la cadena en int o float. Otra solución sería convertir el número en una cadena (el resultado sería "43"). Sigamos con la primera solución.

```python
PS C:\Users\Usuario> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 4 + float('3')
7.0
>>>
```

Se eliminó el error y obtuvimos el resultado que esperábamos.

### Error de importación

**Ejemplo 1: TypeError**

```python
PS C:\Users\Usuario> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math' (unknown location)
>>>
```

En el módulo de matemáticas no existe una función llamada potencia, sino que tiene un nombre diferente: pow. Vamos a corregirlo:

```python
PS C:\Users\Usuario> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math' (unknown location)
>>> from math import pow
>>> pow(2,3)
8.0
>>>
```

### Error de valor

```python
PS C:\Users\Usuario> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
>>>
```

En este caso no podemos cambiar la cadena dada a un número, debido a que contiene la letra "a".

### Error de división cero

```python
PS C:\Users\Usuario> python
Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```

No podemos dividir un número por cero.

Hemos cubierto algunos de los tipos de error de Python, si quieres saber más sobre ellos, consulta la documentación de Python sobre los tipos de error de Python.
Si eres bueno leyendo los tipos de error, podrás corregir tus errores rápidamente y también te convertirás en un mejor programador.

## 💻 Ejercicios: Día 12

1. Abre tu consola interactiva de Python y prueba todos los ejemplos que se tratan en esta sección.

🎉 ¡FELICITACIONES! 🎉

[Estudiantes 2](laboratorios/estudiante.py)

