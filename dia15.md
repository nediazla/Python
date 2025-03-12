# Dia 15: Expresiones regulares

## Expresiones regulares

Una expresión regular o RegEx es una cadena de texto especial que ayuda a encontrar patrones en los datos. Una RegEx se puede utilizar para comprobar si existe algún patrón en un tipo de datos diferente. Para utilizar RegEx en Python, primero debemos importar el módulo RegEx que se llama *re*.

### El módulo *re*

Después de importar el módulo, podemos usarlo para detectar o encontrar patrones.

```python
import re
```

### Métodos en el módulo *re*

Para encontrar un patrón, utilizamos un conjunto diferente de conjuntos de caracteres *re* que permiten buscar una coincidencia en una cadena.

- *re.match()*: busca solo al principio de la primera línea de la cadena y devuelve objetos coincidentes si los encuentra; de lo contrario, devuelve None.
- *re.search*: devuelve un objeto coincidente si hay uno en cualquier parte de la cadena, incluidas las cadenas de varias líneas.
- *re.findall*: devuelve una lista que contiene todas las coincidencias
- *re.split*: toma una cadena, la divide en los puntos de coincidencia y devuelve una lista
- *re.sub*: reemplaza una o varias coincidencias dentro de una cadena

### Match

```python
# syntacre.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
```

```python
import re

txt = 'I love to teach python and javaScript'

# Usamos re.match para buscar el patrón desde el inicio de la cadena
match = re.match('I love to teach', txt, re.I)

# Imprimimos el objeto match
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>

# Obtenemos las posiciones de inicio y fin del match como una tupla
span = match.span()
print(span)  # (0, 15)

# Extraemos el inicio y fin de la tupla span
start, end = span
print(start, end)  # 0, 15

# Usamos las posiciones para extraer el substring
substring = txt[start:end]
print(substring)  # I love to teach

```

Como puede ver en el ejemplo anterior, el patrón que buscamos (o la subcadena que buscamos) es I love to teach. La función match devuelve un objeto solo si el texto comienza con el patrón.

```python
import re

txt = 'I love to teach python and javaScript'

# Intentamos hacer un match con "I love to teach"
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>

# Intentamos hacer un match con "I like to teach"
match = re.match('I like to teach', txt, re.I)
print(match)  # None

```

La cadena no coincide con Me gusta enseñar, por lo tanto, no hubo coincidencia y el método de coincidencia devolvió Ninguno.

### Search

```python
# syntaxre.match(substring, string, re.I)
# substring is a pattern, string is the text we look for a pattern , re.I is case ignore flag
```

```python
import re

# Texto en el que vamos a buscar
txt = '''Python is the most beautiful language that a human being has ever created. I recommend python for a first programming language'''

# Buscar la palabra 'first' en la cadena de texto, sin importar mayúsculas o minúsculas
match = re.search('first', txt, re.I)

# Verificar si se encontró una coincidencia
if match:
    # Imprimir el objeto de coincidencia, que muestra detalles sobre el resultado
    print(match)  # <re.Match object; span=(100, 105), match='first'>

    # Obtener el rango (inicio y fin) de la coincidencia
    span = match.span()
    print(span)  # (100, 105)

    # Extraer las posiciones de inicio y fin desde el rango
    start, end = span
    print(start, end)  # 100 105

    # Extraer el substring usando las posiciones de inicio y fin
    substring = txt[start:end]
    print(substring)  # 'first'
else:
    # Si no se encuentra la palabra 'first', se imprime este mensaje
    print("No se encontró la palabra 'first'.")

```

Como puede ver, la función de búsqueda es mucho mejor que la de coincidencia porque puede buscar el patrón en todo el texto. La función de búsqueda devuelve un objeto de coincidencia con la primera coincidencia encontrada; de lo contrario, devuelve *None*. Una función *re* mucho mejor es *findall*. Esta función comprueba el patrón en toda la cadena y devuelve todas las coincidencias como una lista.

### Búsqueda de todas las coincidencias con *findall*

*findall()* devuelve todas las coincidencias como una lista

```python
import re

# Texto en el que vamos a buscar las ocurrencias de la palabra 'language'
txt = '''Python is the most beautiful language that a human being has ever created. I recommend python for a first programming language'''

# Buscar todas las ocurrencias de la palabra 'language', sin importar mayúsculas o minúsculas
matches = re.findall('language', txt, re.I)

# Imprimir la lista de coincidencias
print(matches)  # ['language', 'language']

```

Como puede ver, la palabra language se encontró dos veces en la cadena. Practiquemos un poco más.
Ahora buscaremos palabras de Python y python en la cadena:

```python
import re

# Texto en el que vamos a buscar las ocurrencias de la palabra 'python'
txt = '''Python is the most beautiful language that a human being has ever created. I recommend python for a first programming language'''

# Buscar todas las ocurrencias de la palabra 'python', sin importar mayúsculas o minúsculas
matches = re.findall('python', txt, re.I)

# Imprimir la lista de coincidencias
print(matches)  # ['Python', 'python']

```

Dado que utilizamos re.I, se incluyen tanto letras mayúsculas como minúsculas. Si no tenemos el indicador re.I, tendremos que escribir nuestro patrón de otra manera. Veámoslo:

```python
import re

# Texto en el que vamos a buscar las ocurrencias de 'Python' o 'python'
txt = '''Python is the most beautiful language that a human being has ever created. I recommend python for a first programming language'''

# Buscar todas las ocurrencias de 'Python' o 'python'
matches = re.findall('Python|python', txt)

# Imprimir la lista de coincidencias
print(matches)  # ['Python', 'python']
```

### Reemplazar una subcadena

```python
import re

# Texto en el que vamos a realizar el reemplazo de 'Python' o 'python'
txt = '''Python is the most beautiful language that a human being has ever created. I recommend python for a first programming language'''

# Reemplazar tanto 'Python' como 'python' con 'JavaScript', sin importar mayúsculas o minúsculas
match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)

# Imprimir la cadena modificada
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created. JavaScript recommend JavaScript for a first programming language.
```

Agreguemos un ejemplo más. La siguiente cadena es muy difícil de leer a menos que eliminemos el símbolo %. Reemplazar el % con una cadena vacía limpiará el texto.

```python
import re

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

# Replace all '%' characters with an empty string
matches = re.sub('%', '', txt)

# Print the modified string
print(matches)

```

```bash
I am teacher and I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs. Does this motivate you to be a teacher?
```

## División de texto mediante RegEx Split

```python
import re

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

# Splitting using '\n' (newline) to break the string into lines
result = re.split('\n', txt)

# Print the resulting list
print(result)
```

```bash
['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']
```

## Cómo escribir patrones RegEx

Para declarar una variable de cadena, usamos comillas simples o dobles. Para declarar la variable RegEx, *r’’*.
El siguiente patrón solo identifica a apple con minúsculas. Para que no distinga entre mayúsculas y minúsculas, debemos reescribir nuestro patrón o agregar una bandera.

```python
import re

# Define the regex pattern
regex_pattern = r'apple'

# The input text
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'

# Find all occurrences of 'apple'
matches = re.findall(regex_pattern, txt)

# Print the matches (only lowercase 'apple' will match)
print(matches)  # ['apple']

# To make the search case-insensitive, add the re.I flag
matches = re.findall(regex_pattern, txt, re.I)

# Print the matches (both 'Apple' and 'apple' will match now)
print(matches)  # ['Apple', 'apple']

# Another way: Use a character set to match both 'Apple' and 'apple'
regex_pattern = r'[Aa]pple'  # This allows for both 'Apple' or 'apple' to match

# Find all occurrences of 'apple' or 'Apple' (case-insensitive)
matches = re.findall(regex_pattern, txt)

# Print the matches
print(matches)  # ['Apple', 'apple']

```

- [a-c] significa a o b o c
- [a-z] significa cualquier letra de la a a la z
- [A-Z] significa cualquier caracter de la A a la Z
- [0-3] significa 0 o 1 o 2 o 3
- [0-9] significa cualquier número del 0 al 9
- [A-Za-z0-9] cualquier caracter individual, es decir de la a a la z, de la A a la Z o del 0 al 9
- \: se usa para escapar caracteres especiales
    - eans: coincide con los casos en los que la cadena contiene dígitos (números del 0 al 9)
    - means: coincide con los casos en los que la cadena no contiene dígitos
- . : cualquier caracter excepto el carácter de nueva línea()
- ^: comienza con
    - r’^substring’ p. ej. r’^love’, una oración que comienza con la palabra love
    - r’[^abc] no significa a, ni b, ni c.
- : *endswith* − *r*′*substring*’ p. ej. r’love$’, oración que termina con la palabra love
- : cero o más veces
    - r’[a]*’ significa opcional o puede aparecer muchas veces.
- +: una o más veces
    - r’[a]+’ significa al menos una vez (o más)
- ?: cero o una vez
    - r’[a]?’ significa cero veces o una vez
- {3}: Exactamente 3 caracteres
- {3,}: Al menos 3 caracteres
- {3,8}: De 3 a 8 caracteres
- |: O bien
    - r’apple|banana’ significa manzana o bien un plátano
- (): Capturar y agrupar

![](img/30-Days-Of-Pythonimagesregex.png)

Hoja de trucos de expresiones regulares

Usemos ejemplos para aclarar los metacaracteres anteriores

### Corchetes

Usemos corchetes para incluir mayúsculas y minúsculas

```python
import re

# Define the regex pattern to match 'Apple' or 'apple'
regex_pattern = r'[Aa]pple'

# The input text
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'

# Find all occurrences of 'Apple' or 'apple'
matches = re.findall(regex_pattern, txt)

# Print the list of matches
print(matches)  # ['Apple', 'apple']

```

Si queremos buscar el plátano escribimos el patrón de la siguiente manera:

```python
import re

# Define the regex pattern to match 'Apple' or 'apple' and 'Banana' or 'banana'
regex_pattern = r'[Aa]pple|[Bb]anana'

# The input text
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'

# Find all occurrences of 'Apple' or 'apple' and 'Banana' or 'banana'
matches = re.findall(regex_pattern, txt)

# Print the list of matches
print(matches)  # ['Apple', 'banana', 'apple', 'banana']

```

Usando el corchete y el operador o , logramos extraer Apple, apple, Banana y banana.

### Carácter de escape (\) en RegEx

```python
import re

# Define the regex pattern to match one or more digits
regex_pattern = r'\d+'  # \d+ will match a sequence of digits (whole numbers)

# The input text
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'

# Find all occurrences of one or more digits (whole numbers)
matches = re.findall(regex_pattern, txt)

# Print the list of matches (whole numbers)
print(matches)  # ['6', '2019', '8', '2021']

```

### Una o más veces(+)

```python
import re

# Definir el patrón de expresión regular para encontrar secuencias de uno o más dígitos
regex_pattern = r'\d+'  # \d+ coincidirá con secuencias de dígitos (números enteros)

# El texto de entrada
txt = 'Este ejemplo de expresión regular se realizó el 6 de diciembre de 2019 y se revisó el 8 de julio de 2021'

# Buscar todas las secuencias de dígitos (números completos)
matches = re.findall(regex_pattern, txt)

# Imprimir los números encontrados
print(matches)  # ['6', '2019', '8', '2021']
```

### Período(.)

```python
import re

# Pattern: 'a' followed by any character
regex_pattern = r'[a].'

# The input text
txt = '''Apple and banana are fruits'''

# Find all matches
matches = re.findall(regex_pattern, txt)

# Print the list of matches
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

```

### Cero o más veces (*)

Cero o muchas veces. El patrón puede no aparecer o puede aparecer muchas veces.

```python
regex_pattern = r'[a].*'  # . any character, * any character zero or more timestxt = '''Apple and banana are fruits'''matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### Cero o una sola vez(?)

Cero o una sola vez. El patrón puede no ocurrir o puede ocurrir una sola vez.

```python
import re

# Input text
txt = '''I am not sure if there is a convention how to write the word e-mail.Some people write it as email others may write it as Email or E-mail.'''

# Regular expression to match 'e-mail', 'email', 'Email', or 'E-mail'
regex_pattern = r'[Ee]-?mail'

# Find all matches using re.findall
matches = re.findall(regex_pattern, txt)

# Print the matches
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

```

### Cuantificador en RegEx

Podemos especificar la longitud de la subcadena que buscamos en un texto, utilizando una llave. Imaginemos que nos interesa una subcadena con una longitud de 4 caracteres:

```python
import re

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # Exactly four digits

matches = re.findall(regex_pattern, txt)
print(matches)  # Output: ['2019', '2021']

```

### Carrito ^

- Comienza con

```python
import re

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means it starts with 'This'

matches = re.findall(regex_pattern, txt)
print(matches)  # Output: ['This']
```

- Negacion

```python
import re

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # Match any sequence of non-alphabetical and non-space characters

matches = re.findall(regex_pattern, txt)
print(matches)  # Output: ['6,', '2019', '8', '2021']

```

## 💻 Ejercicios: Día 15

### Ejercicios: Nivel 1

1. ¿Cuál es la palabra más frecuente en el siguiente párrafo?

```python
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.
```

```bash
[
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
]
```

1. La posición de algunas partículas en el eje x horizontal es -12, -4, -3 y -1 en la dirección negativa, 0 en el origen, 4 y 8 en la dirección positiva. Extraiga estos números de todo este texto y encuentre la distancia entre las dos partículas más alejadas.

```python
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, -1, 0, 2, 4, 8]
distance = 8 -(-12) # 20
```

### Ejercicios: Nivel 2

1. Escriba un patrón que identifique si una cadena es una variable de Python válida
    
    ```bash
    is_valid_variable('first_name') # Trueis_valid_variable('first-name') # Falseis_valid_variable('1first_name') # Falseis_valid_variable('firstname') # True
    ```
    

### Ejercicios: Nivel 3

1. Limpia el siguiente texto. Después de limpiarlo, cuenta las tres palabras más frecuentes en la cadena.
    
    ```python
    sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
    print(clean_text(sentence));
    I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
    print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
    ```
    

🎉¡FELICIDADES! 🎉

[Calculadora](laboratorios/calculadora.py)