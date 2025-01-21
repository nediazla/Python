# Dia 4: strings

## Strings

El texto es un tipo de datos de cadena. Cualquier tipo de datos escrito como texto es una cadena. Cualquier dato entre comillas simples, dobles o triples es una cadena. Existen diferentes métodos de cadena y funciones integradas para trabajar con tipos de datos de cadena. Para comprobar la longitud de una cadena, utilice el método len().

### Creating a String

```python
letter = 'P'                # A string could be a single character or a bunch of textsprint(letter)            # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "Espero que estés disfrutando de las clases de Python."
print(sentence)
```

Las cadenas de varias líneas se crean utilizando comillas simples triples (’’’) o comillas dobles triples (“““). Vea el ejemplo a continuación.

```python
multiline_string = '''Soy profesor y disfruto enseñar. No encontré nada tan gratificante como empoderar a las personas. Por eso enseno Python.'''
print(multiline_string)
# Otra forma de hacer lo mismo
multiline_string = """Soy profesor y disfruto enseñar. No encontré nada tan gratificante como empoderar a las personas. Por eso enseno Python."""
print(multiline_string)
```

### String Concatenation

Podemos conectar cadenas entre sí. La fusión o conexión de cadenas se denomina concatenación. Vea el siguiente ejemplo:

```python
first_name = 'Nelson'
last_name = 'Diaz'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Nelson Diaz
# Checking the length of a string using len() built-in function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16
```

### Escape Sequences in Strings

En Python y otros lenguajes de programación, un carácter seguido es una secuencia de escape. Veamos los caracteres de escape más comunes:

- : nueva línea
- Tabulador (8 espacios)
- \\: barra invertida
- \‘: comilla simple (’)
- \“: comilla doble (”)

Ahora veamos el uso de las secuencias de escape anteriores con ejemplos.

```python
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote# outputI hope every one is enjoying the Python Challenge.
Are you ?
Days    Topics  Exercises
Day 1   5       5
Day 2   6       20
Day 3   5       23
Day 4   1       35
This is a backslash  symbol (\)
In every programming language it starts with "Hello, World!"
```

### String formatting

### Formato de cadena de estilo antiguo (operador %)

En Python hay muchas formas de formatear cadenas. En esta sección, cubriremos algunas de ellas.
El operador “%” se utiliza para formatear un conjunto de variables encerradas en una “tupla” (una lista de tamaño fijo), junto con una cadena de formato, que contiene texto normal junto con “especificadores de argumentos”, símbolos especiales como “%s”, “%d”, “%f”, “%.number of digitsf”.

- %s - Cadena (o cualquier objeto con una representación de cadena, como números)
- %d - Números enteros
- %f - Números de punto flotante
- “%.f” - Números de punto flotante con precisión fija

número de dígitos

```python
# Strings only
first_name = 'Nelson'
last_name = 'Diaz'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)
# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) 
# 2 refers the 2 significant digits after the point
python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) 
# "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"
```

### New Style String Formatting (str.format)

Este formato se introduce en la versión 3 de Python.

```python
first_name = 'Nelson'
last_name = 'Diaz'
language = 'Python'

formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# output
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)
```

### String Interpolation / f-Strings (Python 3.6+)

Otro nuevo formato de cadenas es la interpolación de cadenas, f-strings. Las cadenas comienzan con f y podemos inyectar los datos en sus posiciones correspondientes.

```python
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
```

### Python Strings as Sequences of Characters

Las cadenas de Python son secuencias de caracteres y comparten sus métodos básicos de acceso con otras secuencias ordenadas de objetos de Python (listas y tuplas). La forma más sencilla de extraer caracteres individuales de cadenas (y miembros individuales de cualquier secuencia) es descomprimirlos en las variables correspondientes.

### Unpacking Characters

```python
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
```

### Accessing Characters in Strings by Index

En programación, el conteo comienza desde cero. Por lo tanto, la primera letra de una cadena está en el índice cero y la última letra de una cadena es la longitud de una cadena menos uno.

![30-Days-Of-Pythonimagesstring_index.png](img/30-Days-Of-Pythonimagesstring_index.png)

String index

```python
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
```

Si queremos empezar desde el extremo derecho podemos utilizar indexación negativa. -1 es el último índice.

```python
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o
```

### Slicing Python Strings

En Python podemos dividir cadenas en subcadenas.

```python
language = 'Python'
first_three = language[0:3] 
# starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon
```

### Reversing a String

Nosotros podemos revertir fácilmente las cadenas en python.

```python
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH
```

### Skipping Characters While Slicing

Es posible omitir caracteres mientras se corta pasando el argumento de paso al método de corte.

```python
language = 'Python'
pto = language[0:6:2]
print(pto) # Pto
```

### String Methods

Existen muchos métodos de cadenas que nos permiten formatear cadenas. Vea algunos de los métodos de cadenas en el siguiente ejemplo:

- capitalize(): Convierte el primer carácter de la cadena en letra mayúscula.

```python
challenge = 'clases de python'
print(challenge.capitalize()) # 'clases de  python'
```

- count(): devuelve ocurrencias de subcadena en cadena, count(substring, start=.., end=..). El inicio es un índice inicial para contar y el final es el último índice a contar.

```python
challenge = 'clases de python'
print(challenge.count('y')) 
print(challenge.count('y', 7, 14))
print(challenge.count('th'))
```

- endswith(): Comprueba si una cadena termina con una terminación especificada

```python
challenge = 'clases de python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
```

- expandtabs(): Reemplaza el carácter de tabulación con espacios, el tamaño de tabulación predeterminado es 8. Acepta el argumento de tamaño de tabulación.

```python
challenge = 'class\tof\tpython'
print(challenge.expandtabs())   # 'class    of      python'
print(challenge.expandtabs(10)) # 'class      of        python'
```

- find(): Devuelve el índice de la primera aparición de una subcadena, si no se encuentra, devuelve -1

```python
challenge = 'clases de python'
print(challenge.find('y'))
print(challenge.find('th'))
```

- rfind(): Devuelve el índice de la última aparición de una subcadena, si no se encuentra devuelve -1

```python
challenge = 'clases de python'
print(challenge.rfind('y'))
print(challenge.rfind('th'))
```

- format(): Formatea la cadena en una salida más agradable
Para obtener más información sobre el formato de cadenas, consulte este [link](https://www.programiz.com/python-programming/methods/string/format)

```python
first_name = 'Nelson'
last_name = 'Diaz' 
age = 250 
job = 'teacher'
country = 'Espana'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Nelson Diaz. Tengo 250 años. Soy profesor. Vivo en España.
radius = 10pi = 3.14area = pi * radius ** 2result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314
```

- index(): Devuelve el índice más bajo de una subcadena; los argumentos adicionales indican el índice inicial y final (valor predeterminado: 0 y longitud de cadena: 1). Si no se encuentra la subcadena, se genera un error de valor.

```python
challenge = 'clases de python'
sub_string = 'cl'
print(challenge.index(sub_string))
print(challenge.index(sub_string, 9))
```

- rindex(): Devuelve el índice más alto de una subcadena, los argumentos adicionales indican el índice inicial y final (valor predeterminado 0 y longitud de la cadena - 1)

```python
challenge = 'clases de python'
sub_string = 'cl'
print(challenge.rindex(sub_string))
print(challenge.rindex(sub_string, 9))
print(challenge.rindex('on', 8))
```

- isalnum(): Comprueba caracteres alfanuméricos

```python
challenge = 'classofPython'
print(challenge.isalnum())
challenge = '30daysofPython'
print(challenge.isalnum())
challenge = 'clases de python'
print(challenge.isalnum())
challenge = 'clases de python 2025'
print(challenge.isalnum())
```

- isalpha(): Comprueba si todos los elementos de la cadena son caracteres alfabéticos (a-z y A-Z)

```python
challenge = 'clases de python'
print(challenge.isalpha()) # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # Truenum = '123'
print(num.isalpha())      # False
```

- isdecimal(): Comprueba si todos los caracteres de una cadena son decimales (0-9)

```python
challenge = 'clases de python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed
```

- isdigit(): Comprueba si todos los caracteres de una cadena son números (0-9 y algunos otros caracteres Unicode para números)

```python
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
```

- isnumeric(): Comprueba si todos los caracteres de una cadena son números o están relacionados con números (al igual que isdigit(), solo que acepta más símbolos, como ½)

```python
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False
```

- isidentifier(): Comprueba si un identificador es válido: comprueba si una cadena es un nombre de variable válido

```python
challenge = '30classOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'class_of_python'
print(challenge.isidentifier()) # True
```

- islower(): Comprueba si todos los caracteres del alfabeto en la cadena están en minúsculas

```python
challenge = 'clases de python'
print(challenge.islower()) # True
challenge = 'Clases de Python'
print(challenge.islower()) # False
```

- isupper(): Comprueba si todos los caracteres del alfabeto en la cadena están en mayúsculas

```python
challenge = 'clases de python'
print(challenge.isupper()) #  False
challenge = 'Clases de Python'
print(challenge.isupper()) # True
```

- join(): Devuelve una cadena concatenada

```python
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
```

```python
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'
```

- strip(): Elimina todos los caracteres dados comenzando desde el principio y el final de la cadena.

```python
challenge = 'class of pythoonnn'
print(challenge.strip('noth'))
```

- replace(): Reemplaza la subcadena con una cadena dada

```python
challenge = 'clases de python'
print(challenge.replace('python', 'coding'))
```

- split(): Divide la cadena, utilizando la cadena dada o el espacio como separador

```python
challenge = 'clases de python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
```

- title(): Devuelve una cadena con título en mayúsculas y minúsculas

```python
challenge = 'clases de python'
print(challenge.title()) # clases de python
```

- swapcase(): Convierte todos los caracteres en mayúsculas en minúsculas y todos los caracteres en minúsculas en mayúsculas.

```python
challenge = 'clases de python'
print(challenge.swapcase())   # clases de python
challenge = 'clases de python'
print(challenge.swapcase())  # clases de python
```

- startswith(): Comprueba si la cadena comienza con la cadena especificada

```python
challenge = 'clases de python'
print(challenge.startswith('clases')) # True
challenge = 'class of python'
print(challenge.startswith('clases')) # False
```

🌕 Eres una persona extraordinaria y tienes un potencial extraordinario. Acabas de completar los desafíos del día 4 y estás cuatro pasos adelante en tu camino hacia la grandeza. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## 💻 Exercises - Day 4

1. Concatenar las cadenas ‘Class’, ‘Of’, ‘Python’ en una sola cadena, ‘clases de python’.
2. Concatenar las cadenas ‘Coding’, ‘For’, ‘All’ en una sola cadena, ‘Coding For All’.
3. Declarar una variable llamada company y asignarle el valor inicial “Coding For All”.
4. Imprimir la variable company utilizando *print()*.
5. Imprimir la longitud de la cadena company utilizando el método *len()* y *print()*.
6. Cambiar todos los caracteres a mayúsculas utilizando el método *upper()*
7. Cambiar todos los caracteres a minúsculas utilizando el método *lower()*.
8. Usar los métodos capitalize(), title(), swapcase() para dar formato al valor de la cadena *Coding For All*.
9. Cortar (slice) la primera palabra de la cadena *Coding For All*.
10. Verificar si la cadena *Coding For All* contiene la palabra Coding usando el método index, find u otros métodos.
11. Reemplazar la palabra coding en la cadena ‘Coding For All’ por Python.
12. Cambiar Python for Everyone a Python for All utilizando el método replace u otros métodos.
13. Dividir la cadena ‘Coding For All’ usando el espacio como separador (split()).
14. “Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon” dividir la cadena en la coma.
15. ¿Cuál es el carácter en el índice 0 de la cadena *Coding For All*?
16. ¿Cuál es el último índice de la cadena *Coding For All*?
17. ¿Qué carácter está en el índice 10 de la cadena “Coding For All”?
18. Crear un acrónimo o abreviatura para el nombre ‘Python For Everyone’.
19. Crear un acrónimo o abreviatura para el nombre ‘Coding For All’.
20. Usar index para determinar la posición de la primera ocurrencia de C en Coding For All.
21. Usar index para determinar la posición de la primera ocurrencia de F en Coding For All.
22. Usar rfind para determinar la posición de la última ocurrencia de l en Coding For All People.
23. Usar index o find para encontrar la posición de la primera ocurrencia de la palabra ‘because’ en la siguiente oración: ‘No puedes terminar una oración con porque porque porque es una conjunción’.
24. Usar rindex para encontrar la posición de la última ocurrencia de la palabra because en la siguiente oración: ‘No puedes terminar una oración con porque porque porque es una conjunción’
25. Cortar (slice) la frase ‘porque porque porque’ de la siguiente oración: ‘No puedes terminar una oración con porque porque porque es una conjunción’.
26. Encontrar la posición de la primera ocurrencia de la palabra ‘porque’ en la siguiente oración: ‘No puedes terminar una oración con porque porque porque es una conjunción’.
27. Cortar (slice) la frase ‘porque porque porque’ de la siguiente oración: ‘No puedes terminar una oración con porque porque porque es una conjunción’.
28. ¿Empieza ‘Coding For All’ con una subcadena *Coding*?
29. ¿Termina ‘Coding For All’ con una subcadena *coding*?
30.  eliminar los espacios a la izquierda y derecha de la cadena dada.
    1. 
31. ¿Cuál de las siguientes variables devuelve True cuando usamos el método isidentifier()?
    - ClassOfPython
    - Class_of_python
32. La siguiente lista contiene los nombres de algunas bibliotecas de Python: [‘Django’, ‘Flask’, ‘Bottle’, ‘Pyramid’, ‘Falcon’]. Unir la lista con un hash con espacio entre las cadenas.
33. Usar la secuencia de escape de nueva línea para separar las siguientes oraciones.`py Estoy disfrutando de este desafío. Solo me pregunto qué será lo próximo.`
34. Usar una secuencia de escape de tabulación para escribir las siguientes líneas. `py Nombre Edad País Ciudad Nelson 250 España Caceres`
35. Usar el método de formato de cadenas para mostrar lo siguiente:

```bash
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
```

1. Realice lo siguiente utilizando métodos de formato de cadena:

```bash
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
```

🎉¡FELICIDADES! 🎉