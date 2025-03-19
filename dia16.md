# Día 16: manejo de archivos

Hasta ahora hemos visto diferentes tipos de datos de Python. Normalmente almacenamos nuestros datos en diferentes formatos de archivo. Además de manejar archivos, también veremos diferentes formatos de archivo (.txt, .json, .xml, .csv, .tsv, .excel) en esta sección. Primero, familiaricémonos con el manejo de archivos con formato de archivo común (.txt).

El manejo de archivos es una parte importante de la programación que nos permite crear, leer, actualizar y eliminar archivos. En Python, para manejar datos, usamos la función incorporada *open()*.

```python
# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
```

### Modos de apertura (mode)

Los diferentes modos de apertura de archivo son los siguientes:

- **`'r'` (leer)**: Modo de solo lectura. Abre el archivo para leer su contenido. Si el archivo no existe, se genera un error `FileNotFoundError`.
- **`'w'` (write)**: Modo de escritura. Abre el archivo para escribir. Si el archivo ya existe, su contenido se sobrescribe. Si el archivo no existe, se crea uno nuevo.
- **`'a'` (append)**: Modo de anexado. Abre el archivo para agregar contenido al final del archivo sin sobrescribirlo. Si el archivo no existe, se crea uno nuevo.
- **`'x'` (creación exclusiva)**: Modo de creación exclusiva. Abre el archivo para crear un archivo nuevo. Si el archivo ya existe, genera un error `FileExistsError`.
- **`'b'` (binary)**: Modo binario. Abre el archivo en modo binario. Esto es útil cuando se trabaja con archivos que no son de texto, como imágenes o archivos de audio. Ejemplo: `'rb'`, `'wb'`.
- **`t'` (text)**: Modo de texto. Abre el archivo en modo de texto. Este es el modo predeterminado y no es necesario especificarlo si estás trabajando con archivos de texto. Ejemplo: `'rt'`, `'wt'`.

### Modo combinado

También puedes combinar algunos de estos modos. Por ejemplo:

- **`'rt'`**: Abre el archivo en modo de lectura y en formato texto (modo predeterminado).
- **`'wb'`**: Abre el archivo en modo binario y en formato escritura.
- '**`a+'`**: Abre el archivo para leer y escribir (en modo de anexado).

### Apertura de archivos para lectura

El modo predeterminado de *abrir* es lectura, por lo que no tenemos que especificar 'r' o 'rt'. He creado y guardado un archivo llamado reading_file_example.txt en el directorio de archivos. Veamos cómo se hace:

```python
f = open('./files/reading_file_example.txt', 'r')  # Abrir el archivo en modo lectura
print(f)  # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
f.close()  # Cerrar el archivo después de usarlo

```

en caso de dar error aplicar decodificador: 
```python
with open('donald_speech.txt', 'r', encoding='cp1252') as file:  
    contenido = file.read()  
    print(contenido)
```

Como puede ver en el ejemplo anterior, imprimí el archivo abierto y me brindó información al respecto. El archivo abierto tiene diferentes métodos de lectura: *read()*, *readline*, *readlines*. Un archivo abierto debe cerrarse con el método *close()*.

- *read()*: lee todo el texto como una cadena. Si queremos limitar la cantidad de caracteres que queremos leer, podemos limitarlo pasando un valor int al método *read(number)*.

```python
f = open('./files/reading_file_example.txt', 'r')  # Abrir el archivo en modo lectura
txt = f.read()  # Leer todo el contenido del archivo y almacenarlo en la variable 'txt'
print(type(txt))  # Imprimir el tipo de la variable 'txt', que debería ser una cadena (str)
print(txt)  # Imprimir el contenido completo del archivo
f.close()  # Cerrar el archivo después de usarlo
```

En lugar de imprimir todo el texto, imprimimos los primeros 10 caracteres del archivo de texto.

```python
f = open('./files/reading_file_example.txt', 'r')  # Abrir el archivo en modo lectura
txt = f.read(10)  # Leer los primeros 10 caracteres del archivo
print(type(txt))  # Imprimir el tipo de la variable 'txt', que debería ser una cadena (str)
print(txt)  # Imprimir los primeros 10 caracteres leídos del archivo
f.close()  # Cerrar el archivo después de usarlo
```

- *readline()*: lee solo la primera línea

```python
f = open('./files/reading_file_example.txt', 'r')  # Abrir el archivo en modo lectura
line = f.readline()  # Leer la primera línea del archivo
print(type(line))  # Imprimir el tipo de la variable 'line', que debería ser una cadena (str)
print(line)  # Imprimir la primera línea leída del archivo
f.close()  # Cerrar el archivo después de usarlo
```

- *readlines()*: Lee todo el texto línea por línea y devuelve una lista de líneas.

```python
f = open('./files/reading_file_example.txt', 'r')  # Abrir el archivo en modo lectura
lines = f.readlines()  # Leer todas las líneas del archivo y almacenarlas en una lista
print(type(lines))  # Imprimir el tipo de la variable 'lines', que debería ser una lista
print(lines)  # Imprimir las líneas leídas del archivo
f.close()  # Cerrar el archivo después de usarlo
```

Otra forma de obtener todas las líneas como una lista es usando splitlines():

```python
f = open('./files/reading_file_example.txt', 'r')  # Abrir el archivo en modo lectura
lines = f.read().splitlines()  # Leer todo el contenido y separar las líneas en una lista
print(type(lines))  # Imprimir el tipo de la variable 'lines', que debería ser una lista
print(lines)  # Imprimir las líneas leídas del archivo
f.close()  # Cerrar el archivo después de usarlo
```

Después de abrir un archivo, debemos cerrarlo. Existe una gran tendencia a olvidarse de cerrarlos. Existe una nueva forma de abrir archivos utilizando with: cierra los archivos por sí solo. Reescribimos el ejemplo anterior con el método with:

```python
with open('./files/reading_file_example.txt', 'r') as f:  # Abrir el archivo en modo lectura
    lines = f.read().splitlines()  # Leer todo el contenido y dividirlo en líneas, eliminando los saltos de línea
    print(type(lines))  # Imprimir el tipo de la variable 'lines', que debería ser una lista
    print(lines)  # Imprimir las líneas leídas del archivo
```


contar lineas
```python
# Abre el archivo en modo lectura
with open('archivo.txt', 'r', encoding='cp1252') as file:
    # Cuenta las líneas
    num_lineas = sum(1 for line in file)

print(f'El archivo tiene {num_lineas} líneas.')
```
### Apertura de archivos para escritura y actualización

Para escribir en un archivo existente, debemos agregar un modo como parámetro a la función *open()*:

- "a" - append - agregará al final del archivo, si el archivo no existe, creará un nuevo archivo.
- "w" - write - sobrescribirá cualquier contenido existente, si el archivo no existe, lo creará.

Agreguemos un texto al archivo que hemos estado leyendo:

```python
with open('./files/reading_file_example.txt', 'a') as f:  # Abrir el archivo en modo añadir (append)
    f.write('This text has to be appended at the end')  # Escribir el texto al final del archivo
```

El método siguiente crea un nuevo archivo, si el archivo no existe:

```python
with open('./files/writing_file_example.txt', 'w') as f:  # Abrir el archivo en modo escritura (se sobrescribe si ya existe)
    f.write('This text will be written in a newly created file')  # Escribir el texto en el archivo

```

### Eliminar archivos

En la sección anterior, vimos cómo crear y eliminar un directorio usando el módulo *os*. Ahora, si queremos eliminar un archivo, usamos el módulo *os*.

```python
import os  # Importar el módulo os que contiene funciones para interactuar con el sistema operativo
os.remove('./files/example.txt')  # Eliminar el archivo especificado
```

Si el archivo no existe, el método eliminar dará un error, por lo que es bueno usar una condición como esta:

```python
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
```

## Tipos de archivo

### Archivo con extensión txt

El fichero con extensión *txt* es una forma muy común de datos y lo hemos cubierto en la sección anterior. Pasemos al fichero JSON

### Fichero con extensión json

JSON significa JavaScript Object Notation. En realidad, es un objeto JavaScript stringified o diccionario Python.

*Ejemplo:*

```python
# Diccionario en Python
person_dct = {
    "name": "Nelson",
    "country": "Spain",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}

# JSON: una cadena que representa un diccionario
person_json = '{"name": "Nelson", "country": "Spain", "city": "Helsinki", "skills": ["JavaScript", "React", "Python"]}'

# Usamos tres comillas para hacerlo más legible y representar el JSON en varias líneas
person_json_multiline = '''{
    "name": "Nelson",
    "country": "Spain",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}'''

```

### Cambiando JSON a Diccionario

Para cambiar un JSON a diccionario, primero importamos el módulo json y luego usamos el método *loads*.

```python
import json  # Importamos la librería JSON para manipular datos JSON

# JSON: una cadena que representa un diccionario
person_json = '''{
    "name": "Nelson",
    "country": "Spain",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}'''

# Convertimos la cadena JSON en un diccionario de Python
person_dct = json.loads(person_json)

# Mostrar el tipo de la variable 'person_dct' (debería ser un diccionario)
print(type(person_dct))  # <class 'dict'>

# Mostrar el diccionario convertido
print(person_dct)

# Acceder a un valor usando una clave específica ('name')
print(person_dct['name'])  # Nelson
```

### Cambiar Diccionario a JSON

Para cambiar un diccionario a JSON utilizamos el método *dumps* del módulo json.

```python
import json  # Importamos la librería JSON para manipular datos JSON

# Diccionario de Python
person = {
    "name": "Nelson",
    "country": "Spain",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}

# Convertimos el diccionario de Python a una cadena JSON
person_json = json.dumps(person, indent=4)  # 'indent' puede ser 2, 4, 8. Esto hace que el JSON sea más legible

# Mostrar el tipo de la variable 'person_json' (debería ser una cadena)
print(type(person_json))  # <class 'str'>

# Mostrar la cadena JSON convertida
print(person_json)

```

### Guardar como archivo JSON

También podemos guardar nuestros datos como un archivo json. Guardémoslo como un archivo json siguiendo los siguientes pasos. Para escribir un archivo json, usamos el método json.dump(), puede tomar diccionario, archivo de salida, ensure_ascii y sangría.

```python
import json  # Importamos la librería JSON para manipular datos JSON

# Diccionario de Python
person = {
    "name": "Nelson",
    "country": "Spain",
    "city": "Helsinki",
    "skills": ["JavaScript", "React", "Python"]
}

# Guardamos el diccionario como un archivo JSON
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    # Escribimos el diccionario en el archivo JSON, con indentación y sin escapar los caracteres no ASCII
    json.dump(person, f, ensure_ascii=False, indent=4)
```

En el código anterior, utilizamos la codificación y la sangría. La sangría hace que el archivo json sea fácil de leer.

### Archivo con extensión csv

CSV significa valores separados por comas. CSV es un formato de archivo simple utilizado para almacenar datos tabulares, como una hoja de cálculo o una base de datos. CSV es un formato de datos muy común en la ciencia de datos.

**Ejemplo:**

```
"name","country","city","skills"
"Nelson","Spain","Helsinki","JavaScript"
```

**Ejemplo:**

```python
import csv  # Importamos la librería CSV para manejar archivos CSV

with open('./files/csv_example.csv') as f:  # Abrimos el archivo CSV en modo lectura
    csv_reader = csv.reader(f, delimiter=',')  # Usamos el método 'reader' para leer el archivo CSV

    line_count = 0  # Inicializamos un contador de líneas
    for row in csv_reader:  # Recorremos cada fila del archivo CSV
        if line_count == 0:  # Si estamos en la primera línea (cabeceras)
            print(f'Column names are: {", ".join(row)}')  # Imprimimos los nombres de las columnas
            line_count += 1  # Aumentamos el contador de líneas
        else:
            # Imprimimos la información de cada fila (en este caso, se supone que es un maestro y su ubicación)
            print(f'\t{row[0]} is a teacher. He lives in {row[1]}, {row[2]}.')
            line_count += 1  # Aumentamos el contador de líneas

    print(f'Number of lines: {line_count}')  # Imprimimos el número total de líneas leídas
```

### Archivo con extensión xlsx

Para leer archivos excel necesitamos instalar el paquete *xlrd*. Cubriremos esto después de que cubramos la instalación de paquetes usando pip.

```python
import xlrd
excel_book = xlrd.open_workbook('sample.xls)
print(excel_book.nsheets)
print(excel_book.sheet_names)
```

### Archivo con extensión xml

XML es otro formato de datos estructurados que se parece a HTML. En XML las etiquetas no están predefinidas. La primera línea es una declaración XML. La etiqueta persona es la raíz del XML. La persona tiene un atributo de género.**Ejemplo:XML**

```xml
<?xml version="1.0"?>  <!-- Declaración XML que especifica la versión del XML -->
<person gender="female">  <!-- Elemento principal 'person' con un atributo 'gender' -->
  <name>Nelson</name>  <!-- Elemento 'name' que contiene el valor 'Nelson' -->
  <country>Spain</country>  <!-- Elemento 'country' con el valor 'Spain' -->
  <city>Helsinki</city>  <!-- Elemento 'city' con el valor 'Helsinki' -->
  <skills>  <!-- Elemento 'skills' que contiene varios subelementos 'skill' -->
    <skill>JavaScript</skill>  <!-- Elemento 'skill' con el valor 'JavaScript' -->
    <skill>React</skill>  <!-- Elemento 'skill' con el valor 'React' -->
    <skill>Python</skill>  <!-- Elemento 'skill' con el valor 'Python' -->
  </skills>
</person>

```

Para más información sobre cómo leer un archivo XML consulta la [documentación](https://docs.python.org/2/library/xml.etree.elementtree.html)

```python
import xml.etree.ElementTree as ET  # Importamos el módulo ElementTree para procesar XML

# Cargamos el archivo XML
tree = ET.parse('./files/xml_example.xml')

# Obtenemos el elemento raíz del árbol XML
root = tree.getroot()

# Imprimimos el nombre de la etiqueta raíz
print('Root tag:', root.tag)

# Imprimimos los atributos del elemento raíz
print('Attribute:', root.attrib)

# Iteramos sobre los elementos hijos del elemento raíz
for child in root:
    # Imprimimos el nombre de la etiqueta de cada hijo
    print('Field:', child.tag)
```

Estás haciendo grandes progresos. Mantenga su impulso, mantener el buen trabajo. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## 💻 Ejercicios: Día 16

### Ejercicios: Nivel 1

1. Escribe una función que cuente el número de líneas y el número de palabras de un texto. Todos los archivos están en la carpeta data the:
    1. Leer obama_speech.txt y contar el número de líneas y palabras.
    2. Leer el archivo michelle_obama_speech.txt y contar el número de líneas y palabras
    3. Leer el archivo donald_speech.txt y contar el número de líneas y palabras
    4. Leer el archivo melina_trump_speech.txt y contar el número de líneas y palabras
2. Lee el archivo de datos countries_data.json en el directorio data, crea una función que encuentre los diez idiomas más hablados
    
    ```python
    # Your output should look like thisprint(most_spoken_languages(filename='./data/countries_data.json', 10))
    [(91, 'English'),
    (45, 'French'),
    (25, 'Arabic'),
    (24, 'Spanish'),
    (9, 'Russian'),
    (9, 'Portuguese'),
    (8, 'Dutch'),
    (7, 'German'),
    (5, 'Chinese'),
    (4, 'Swahili'),
    (4, 'Serbian')]
    
    # Your output should look like thisprint(most_spoken_languages(filename='./data/countries_data.json', 3))
    [(91, 'English'),
    (45, 'French'),
    (25, 'Arabic')]
    ```
    
3. Lea el archivo de datos countries_data.json en el directorio data, cree una función que cree una lista de los diez países más poblados
    
    ```python
    # Your output should look like thisprint(most_populated_countries(filename='./data/countries_data.json', 10))
    [
    {'country': 'China', 'population': 1377422166},
    {'country': 'India', 'population': 1295210000},
    {'country': 'United States of America', 'population': 323947000},
    {'country': 'Indonesia', 'population': 258705000},
    {'country': 'Brazil', 'population': 206135893},
    {'country': 'Pakistan', 'population': 194125062},
    {'country': 'Nigeria', 'population': 186988000},
    {'country': 'Bangladesh', 'population': 161006790},
    {'country': 'Russian Federation', 'population': 146599183},
    {'country': 'Japan', 'population': 126960000}
    ]
    # Your output should look like thisprint(most_populated_countries(filename='./data/countries_data.json', 3))
    [
    {'country': 'China', 'population': 1377422166},
    {'country': 'India', 'population': 1295210000},
    {'country': 'United States of America', 'population': 323947000}
    ]
    ```
    

### Ejercicios: Nivel 2

1. Extraiga todas las direcciones de correo electrónico entrantes como una lista del archivo email_exchange_big.txt.
2. Encuentre las palabras más comunes en el idioma inglés. Llame a su función encontrar_palabras_más_comunes, tomará dos parámetros - una cadena o un archivo y un número entero positivo, indicando el número de palabras. Su función devolverá una matriz de tuplas en orden descendente. Comprobar la salida

```python
    # Your output should look like this    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]
    # Your output should look like this    print(find_most_common_words('sample.txt', 5))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]
```

1. Utilice la función, encontrar_palabras_más_frecuentes para encontrar:
    1. Las diez palabras más frecuentes utilizadas en [el discurso de Obama](https://github.com/nediazla/Python/blob/main/data/obama_speech.txt)
    2. Las diez palabras más utilizadas en el [discurso de Michelle](https://github.com/nediazla/Python/blob/main/data/michelle_obama_speech.txt)
    3. Las diez palabras más utilizadas en el [discurso de Trump](https://github.com/nediazla/Python/blob/main/data/donald_speech.txt)
    4. Las diez palabras más utilizadas en el [discurso de Melina](https://github.com/nediazla/Python/blob/main/data/melina_trump_speech.txt)
2. Escribe una aplicación python que compruebe la similitud entre dos textos. Toma un archivo o una cadena como parámetro y evaluará la similitud de los dos textos. Por ejemplo, comprueba la similitud entre las transcripciones del discurso de [Michelle](https://github.com/nediazla/Python/blob/main/data/michelle_obama_speech.txt) y [Melina](https://github.com/nediazla/Python/blob/main/data/melina_trump_speech.txt). Es posible que necesite un par de funciones, una para limpiar el texto (clean_text), otra para eliminar las palabras de apoyo (remove_support_words) y, por último, otra para comprobar la similitud (check_text_similarity). La lista de [palabras de parada](https://github.com/nediazla/Python/blob/main/data/stop_words.py) se encuentra en el directorio de datos
3. Buscar las 10 palabras más repetidas en romeo_and_juliet.txt
4. Lee el archivo [csv de hacker news](https://raw.githubusercontent.com/nediazla/Python/refs/heads/main/data/hacker_news.csv) y averígualo:
    1. Cuente el número de líneas que contienen python o Python
    2. Cuente el número de líneas que contienen JavaScript, javascript o Javascript
    3. Cuente el número de líneas que contienen Java y no JavaScript

🎉 ¡ENHORABUENA! 🎉