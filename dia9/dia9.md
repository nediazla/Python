# Dia 9: modules

## 

## Módulos

### ¿Qué es un módulo?

Un módulo es un archivo que contiene un conjunto de códigos o un conjunto de funciones que se pueden incluir en una aplicación. Un módulo puede ser un archivo que contiene una sola variable, una función o una gran base de código.

### Creación de un módulo

Para crear un módulo, escribimos nuestros códigos en un script de Python y lo guardamos como un archivo .py. Crea un archivo llamado [mymodule.py](http://mymodule.py/) dentro de la carpeta de tu proyecto. Escribamos algo de código en este archivo.

```python
# mymodule.py file
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
```

Cree el archivo [main.py](http://main.py/) en el directorio de su proyecto e importe el archivo [mymodule.py](http://mymodule.py/).

### Importación de un módulo

Para importar el archivo, usamos la palabra clave *import* y solo el nombre del archivo.

```python
# main.py file
import mymodule
print(mymodule.generate_full_name('Nelson', 'Diaz')) # Nelson Diaz
```

### Importar funciones desde un módulo

Podemos tener muchas funciones en un archivo y podemos importarlas de forma diferente.

```python
# main.py file
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Nelson','Diaz'))
print(sum_two_nums(1,9))
mass = 100;
weight = mass * gravity
print(weight)
print(person['firstname'])
```

### Importar funciones desde un módulo y cambiar el nombre

Durante la importación podemos cambiar el nombre del módulo.

```python
# main.py file
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Nelson','Diaz'))
print(total(1, 9))
mass = 100;weight = mass * g
print(weight)
print(p)
print(p['firstname'])
```

## Importar módulos integrados

Al igual que otros lenguajes de programación, también podemos importar módulos importando el archivo o la función utilizando la palabra clave *import*. Importemos el módulo común que utilizaremos la mayor parte del tiempo. Algunos de los módulos integrados comunes son: *math*, *datetime*, *os*, *sys*, *random*, *statistics*, *collections*, *json*, *re*

### Módulo OS

Con el módulo *os* de Python es posible realizar automáticamente muchas tareas del sistema operativo. El módulo OS de Python proporciona funciones para crear, cambiar el directorio de trabajo actual y eliminar un directorio (carpeta), obtener su contenido, cambiar e identificar el directorio actual.

```python
# import the module
import os
# Creating a directory
os.mkdir('directory_name')
# Changing the current directory
os.chdir('path')
# Getting current working directory
os.getcwd()
# Removing directory
os.rmdir()
```

### Módulo Sys

El módulo sys proporciona funciones y variables que se utilizan para manipular diferentes partes del entorno de ejecución de Python. La función sys.argv devuelve una lista de argumentos de línea de comandos que se pasan a un script de Python. El elemento en el índice 0 de esta lista siempre es el nombre del script, y en el índice 1 es el argumento que se pasa desde la línea de comandos.

Ejemplo de un archivo script.py:

```python
import sys
print(sys.argv[0], argv[1],sys.argv[2]) 
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))
```

Ahora, para comprobar cómo funciona este script, escribí en la línea de comandos:

```bash
python script.py 
Nelson ClassOfPython
```

Resultado:

```bash
Welcome Nelson. Enjoy ClassofPython challenge!
```

Algunos comandos de sistema útiles:

```python
# to exit sys
sys.exit()
# To know the largest integer variable it takes
sys.maxsize
# To know environment path
sys.path
# To know the version of python you are using
sys.version
```

### Módulo de estadísticas

El módulo de estadísticas proporciona funciones para estadísticas matemáticas de datos numéricos. Las funciones estadísticas más populares que se definen en este módulo son: *media*, *mediana*, *moda*, *desviación estándar*, etc.

```python
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

### Módulo de Matemáticas

Módulo que contiene muchas operaciones y constantes matemáticas.

```python
import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base
```

Ahora, hemos importado el módulo de matemáticas que contiene muchas funciones que pueden ayudarnos a realizar cálculos matemáticos. Para comprobar qué funciones tiene el módulo, podemos utilizar help(math) o dir(math). Esto mostrará las funciones disponibles en el módulo. Si queremos importar solo una función específica del módulo, la importamos de la siguiente manera:

```python
from math import pi
print(pi)
```

También es posible importar varias funciones a la vez

```python
from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2
```

Pero si queremos importar todas las funciones del módulo matemático podemos usar *.

```python
from math import *
print(pi)                  # 3.141592653589793, pi constant
print(sqrt(2))             # 1.4142135623730951, square root
print(pow(2, 3))           # 8.0, exponential
print(floor(9.81))         # 9, rounding to the lowest
print(ceil(9.81))          # 10, rounding to the highest
print(math.log10(100))     # 2
```

Al importar también podemos cambiar el nombre de la función.

```python
from math import pi as  PI
print(PI) # 3.141592653589793
```

### Módulo de cadena

Un módulo de cadena es un módulo útil para muchos propósitos. El siguiente ejemplo muestra algunos usos del módulo de cadena.

```python
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### Módulo aleatorio

A esta altura ya está familiarizado con la importación de módulos. Hagamos una importación más para familiarizarnos con ella. Importemos el módulo *random* que nos da un número aleatorio entre 0 y 0,9999... El módulo *random* tiene muchas funciones, pero en esta sección solo utilizaremos *random* y *randint*.

```python
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive
```

🌕 ¡Estás llegando lejos! ¡Sigue así! Acabas de completar los desafíos del día 12 y estás a 12 pasos de tu camino hacia la grandeza. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## 💻 Ejercicios: Día 9

### Ejercicios: Nivel 1

1. Escribe una función que genere un random_user_id de seis dígitos/caracteres.

```python
  print(random_user_id());  '1ee33d'
```

1. Modifique la tarea anterior. Declare una función llamada user_id_gen_by_user. No acepta ningún parámetro, pero acepta dos entradas mediante input(). Una de las entradas es la cantidad de caracteres y la segunda es la cantidad de ID que se supone que se generarán.

```python
print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf

print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
```

1. Escriba una función llamada rgb_color_gen. Generará colores RGB (tres valores que van de 0 a 255 cada uno).

```python
print(rgb_color_gen())
# rgb(125,244,255) - the output should be in this form
```

### Ejercicios: Nivel 2

1. Escribe una función list_of_hexa_colors que devuelva cualquier número de colores hexadecimales en una matriz (seis números hexadecimales escritos después de #. El sistema de numeración hexadecimal está formado por 16 símbolos, del 0 al 9 y las primeras 6 letras del alfabeto, de la a a la f. Consulta la tarea 6 para ver ejemplos de resultados).
2. Escribe una función list_of_rgb_colors que devuelva cualquier número de colores RGB en una matriz.
3. Escribe una función generate_colors que pueda generar cualquier número de colores hexadecimales o rgb.

```python
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b']   
   generate_colors('hexa', 1) # ['#b334ef']   
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']   
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
```

### Ejercicios: Nivel 3

1. Llama a tu función shuffle_list, que toma una lista como parámetro y devuelve una lista aleatoria.
2. Escribe una función que devuelva una matriz de siete números aleatorios en un rango de 0 a 9. Todos los números deben ser únicos.

🎉 ¡FELICITACIONES! 🎉