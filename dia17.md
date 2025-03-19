# Dia 17: python Administradora de paquetes

### ¿Qué es PIP?

PIP significa programa de instalación preferido. Usamos *pip* para instalar diferentes paquetes de Python.
Un paquete es un módulo de Python que puede contener uno o más módulos u otros paquetes. Un módulo o módulos que podemos instalar en nuestra aplicación es un paquete.
En programación, no tenemos que escribir todos los programas de utilidad, en lugar de eso, instalamos paquetes y los importamos a nuestras aplicaciones.

### Instalación de PIP

Si no instaló pip, déjenos instalarlo ahora. Vaya a su terminal o símbolo del sistema y copie y pegue esto:

```bash
xnoxos@ubuntu:~$ pip install pip
```

Comprueba si pip está instalado escribiendo

```bash
pip --version
```

```python
xnoxos@ubuntu:~$ pip --version
pip 21.1.3 from /usr/local/lib/python3.7/site-packages/pip (python 3.9.6)
```

Como puede ver, estoy usando la versión 21.1.3 de pip. Si ve un número un poco por debajo o por encima de ese, significa que tiene pip instalado.

Veamos algunos de los paquetes que se usan en la comunidad de Python para diferentes propósitos. Solo para informarle que hay muchos paquetes disponibles para usar con diferentes aplicaciones.

### Instalación de paquetes con pip

Intentemos instalar *numpy*, llamado numeric python. Es uno de los paquetes más populares en la comunidad de aprendizaje automático y ciencia de datos.

- NumPy es el paquete fundamental para computación científica con Python. Contiene, entre otras cosas:
- un poderoso objeto de matriz N-dimensional
- funciones sofisticadas (de transmisión)
- herramientas para integrar código C/C++ y Fortran
- capacidades útiles de álgebra lineal, transformada de Fourier y números aleatorios

```bash
xnoxos@ubuntu:~$ pip install numpy
```

Comencemos a utilizar Numpy. Abra su consola interactiva de Python, escriba Python y luego importe Numpy de la siguiente manera:

```python
import numpy as np

lst = [1, 2, 3, 4, 5]
np_arr = np.array(lst)

# Imprimir el array original
print(np_arr)  # array([1, 2, 3, 4, 5])

# Multiplicar el array por 2
print(np_arr * 2)  # array([ 2,  4,  6,  8, 10])

# Sumar 2 al array
print(np_arr + 2)  # array([3, 4, 5, 6, 7])
```

Pandas es una biblioteca de código abierto con licencia BSD que ofrece estructuras de datos y herramientas de análisis de datos de alto rendimiento y fáciles de usar para el lenguaje de programación Python. Instalemos el hermano mayor de numpy, pandas:

```bash
xnoxos@ubuntu:~$ pip install pandas
```

```python
xnoxos@ubuntu:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas
```

Esta sección no trata sobre numpy ni pandas, aquí estamos tratando de aprender cómo instalar paquetes y cómo importarlos. Si es necesario, hablaremos sobre diferentes paquetes en otras secciones.

Vamos a importar un módulo de navegador web, que nos puede ayudar a abrir cualquier sitio web. No necesitamos instalar este módulo, ya está instalado por defecto con Python 3. Por ejemplo, si te gusta abrir cualquier cantidad de sitios web en cualquier momento o si te gusta programar algo, puedes usar este módulo *webbrowser*.

```python
import webbrowser  # web browser module to open websites

# List of URLs
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/Nelson/',
    'https://github.com/Nelson',
    'https://twitter.com/Nelson',
]

# Open the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)
```

### Desinstalación de paquetes

Si no desea conservar los paquetes instalados, puede eliminarlos con el siguiente comando.

```bash
pip uninstall packagename
```

### Lista de paquetes

Para ver los paquetes instalados en nuestra máquina podemos utilizar pip seguido de list.

```bash
pip list
```

### Mostrar paquete

Para mostrar información sobre un paquete

```bash
pip show packagename
```

```bash
xnoxos@ubuntu:~$ pip show pandas
Name: pandas
Version: 1.2.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: python-dateutil, pytz, numpy
Required-by:
```

Si queremos aún más detalles, simplemente agreguemos –verbose

```bash
xnoxos@ubuntu:~$ pip show --verbose pandas
Name: pandas
Version: 1.2.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: numpy, pytz, python-dateutil
Required-by:Metadata-Version: 2.1
Installer: pip
Classifiers:  Development Status :: 5 - Production/Stable
  Environment :: Console
  Operating System :: OS Independent
  Intended Audience :: Science/Research
  Programming Language :: Python
  Programming Language :: Python :: 3
  Programming Language :: Python :: 3.5
  Programming Language :: Python :: 3.6
  Programming Language :: Python :: 3.7
  Programming Language :: Python :: 3.8
  Programming Language :: Cython
  Topic :: Scientific/Engineering
Entry-points:  [pandas_plotting_backends]  matplotlib = pandas:plotting._matplotlib
```

### PIP Freeze

Genera paquetes de Python instalados con su versión y el resultado es adecuado para usarlo en un archivo de requisitos. Un archivo requirements.txt es un archivo que debe contener todos los paquetes de Python instalados en un proyecto de Python.

```bash
xnoxos@ubuntu:~$ pip freeze
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
```

El pip freeze nos proporcionó los paquetes utilizados, instalados y su versión. Lo usamos con el archivo requirements.txt para la implementación.

### Lectura desde URL

A esta altura, ya está familiarizado con la forma de leer o escribir en un archivo ubicado en su máquina local. A veces, nos gustaría leer desde un sitio web mediante una URL o desde una API.
API significa Interfaz de Programación de Aplicaciones. Es un medio para intercambiar datos estructurados entre servidores, principalmente como datos json. Para abrir una conexión de red, necesitamos un paquete llamado *requests*: permite abrir una conexión de red e implementar operaciones CRUD (crear, leer, actualizar y eliminar). En esta sección, cubriremos solo la lectura o la obtención de parte de un CRUD.

Instalemos *requests*:

```python
xnoxos@ubuntu:~$ pip install requests
```

Veremos los métodos get, status_code, headers, text y json en el módulo de solicitudes:

- get(): para abrir una red y obtener datos de la URL; devuelve un objeto de respuesta
- status_code: después de obtener los datos, podemos verificar el estado de la operación (éxito, error, etc.)
- headers: para verificar los tipos de encabezado
- text: para extraer el texto del objeto de respuesta obtenido
- json: para extraer datos json
Leamos un archivo txt de este sitio web, [https://www.w3.org/TR/PNG/iso_8859-1.txt](https://www.w3.org/TR/PNG/iso_8859-1.txt).

```python
import requests  # Importamos el módulo requests para hacer solicitudes HTTP

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'  # URL de un archivo de texto en la web

response = requests.get(url)  # Realizamos una solicitud GET a la URL para obtener el contenido

# Imprimimos el objeto de respuesta (esto incluye información como el código de estado y los headers)
print(response)

# Imprimimos el código de estado de la respuesta (200 significa éxito)
print(response.status_code)

# Imprimimos las cabeceras de la respuesta, que contienen metadatos sobre la respuesta
print(response.headers)

# Imprimimos el contenido del cuerpo de la respuesta (el texto real de la página solicitada)
print(response.text)
```

```bash
import requests
import gzip
from io import BytesIO

# URL del archivo de texto en el servidor
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

# Realizar la solicitud GET
response = requests.get(url)

# Comprobar si el contenido está comprimido en gzip
if response.headers.get('content-encoding') == 'gzip':
    # Si está comprimido, descomprimirlo
    buf = BytesIO(response.content)  # Crear un buffer en memoria con los datos comprimidos
    f = gzip.GzipFile(fileobj=buf)   # Usamos GzipFile para leer el contenido comprimido
    decompressed_text = f.read().decode('iso-8859-1')  # Descomprimir y decodificar el contenido con la codificación adecuada
    print(decompressed_text)  # Imprimir el texto descomprimido
else:
    # Si no está comprimido, simplemente imprimir el contenido como texto
    print(response.text)  # Imprimir el contenido de la respuesta directamente
```

- Leamos una API. API significa Interfaz de Programación de Aplicaciones. Es un medio para intercambiar datos de estructura entre servidores, principalmente datos json. Un ejemplo de API: [https://restcountries.eu/rest/v2/all](https://restcountries.eu/rest/v2/all). Leamos esta API usando el módulo de solicitudes.

```python
import requests

url = 'https://restcountries.eu/rest/v2/all'  # API de países

response = requests.get(url)  # Realiza una solicitud para obtener los datos

# Imprimir el objeto de respuesta
print(response)

# Imprimir el código de estado (200 significa éxito)
print(response.status_code)

# Obtener los países en formato JSON
countries = response.json()

# Imprimir el primer país (usamos slicing para obtener solo el primero)
print(countries[:1])  # Se muestra solo el primer país. Si quieres ver todos los países, elimina el slicing.
```

```bash
<Response [200]>200[{'alpha2Code': 'AF',
  'alpha3Code': 'AFG',
  'altSpellings': ['AF', 'Afġānistān'],
  'area': 652230.0,
  'borders': ['IRN', 'PAK', 'TKM', 'UZB', 'TJK', 'CHN'],
  'callingCodes': ['93'],
  'capital': 'Kabul',
  'cioc': 'AFG',
  'currencies': [{'code': 'AFN', 'name': 'Afghan afghani', 'symbol': '؋'}],
  'demonym': 'Afghan',
  'flag': 'https://restcountries.eu/data/afg.svg',
  'gini': 27.8,
  'languages': [{'iso639_1': 'ps',
                 'iso639_2': 'pus',
                 'name': 'Pashto',
                 'nativeName': 'پښتو'},
                {'iso639_1': 'uz',
                 'iso639_2': 'uzb',
                 'name': 'Uzbek',
                 'nativeName': 'Oʻzbek'},
                {'iso639_1': 'tk',
                 'iso639_2': 'tuk',
                 'name': 'Turkmen',
                 'nativeName': 'Türkmen'}],
  'latlng': [33.0, 65.0],
  'name': 'Afghanistan',
  'nativeName': 'افغانستان',
  'numericCode': '004',
  'population': 27657145,
  'region': 'Asia',
  'regionalBlocs': [{'acronym': 'SAARC',
                     'name': 'South Asian Association for Regional Cooperation',
                     'otherAcronyms': [],
                     'otherNames': []}],
  'subregion': 'Southern Asia',
  'timezones': ['UTC+04:30'],
  'topLevelDomain': ['.af'],
  'translations': {'br': 'Afeganistão',
                   'de': 'Afghanistan',
                   'es': 'Afganistán',
                   'fa': 'افغانستان',
                   'fr': 'Afghanistan',
                   'hr': 'Afganistan',
                   'it': 'Afghanistan',
                   'ja': 'アフガニスタン',
                   'nl': 'Afghanistan',
                   'pt': 'Afeganistão'}}]
```

Usamos el método *json()* del objeto de respuesta si estamos obteniendo datos JSON. Para archivos txt, html, xml y otros formatos, podemos usar *text*.

### Creación de un paquete

Organizamos una gran cantidad de archivos en diferentes carpetas y subcarpetas según algunos criterios, de modo que podamos encontrarlos y administrarlos fácilmente. Como sabes, un módulo puede contener varios objetos, como clases, funciones, etc. Un paquete puede contener uno o más módulos relevantes. Un paquete es en realidad una carpeta que contiene uno o más archivos de módulo. Creemos un paquete llamado mypackage, siguiendo estos pasos:

Cree una nueva carpeta llamada mypacakge dentro de la carpeta 30DaysOfPython
Cree un archivo **init**.py vacío en la carpeta mypackage.
Cree los módulos [arithmetic.py](http://arithmetic.py/) y [greeting.py](http://greeting.py/) con el siguiente código:

```python
# mypackage/arithmetics.py

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

def subtract(a, b):
    return a - b

def multiple(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

def remainder(a, b):
    return a % b

def power(a, b):
    return a ** b
```

```python
# mypackage/greet.py

def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to Course Of Python!'

```

La estructura de carpetas de su paquete debería verse así:

```bash
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```

Ahora abramos el shell interactivo de Python y probemos el paquete que hemos creado:

```bash
xnoxos@ubuntu:~/Desktop/ClassOfPython$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from mypackage import arithmetics
>>> arithmetics.add_numbers(1, 2, 3, 5)11
>>> arithmetics.subtract(5, 3)2
>>> arithmetics.multiple(5, 3)15
>>> arithmetics.division(5, 3)1.6666666666666667
>>> arithmetics.remainder(5, 3)2
>>> arithmetics.power(5, 3)125
>>> from mypackage import greet
>>> greet.greet_person('Nelson', 'Diaz')'Nelson Diaz, welcome to CourseOfPython!'
>>>
```

Como puede ver, nuestro paquete funciona perfectamente. La carpeta del paquete contiene un archivo especial llamado **init**.py, que almacena el contenido del paquete. Si colocamos **init**.py en la carpeta del paquete, Python start lo reconoce como un paquete.
El **init**.py expone recursos específicos de sus módulos para que se importen a otros archivos de Python. Un archivo **init**.py vacío hace que todas las funciones estén disponibles cuando se importa un paquete. El **init**.py es esencial para que Python reconozca la carpeta como un paquete.

### Más información sobre los paquetes

- Base de datos
    - SQLAlchemy o SQLObject - Acceso orientado a objetos a varios sistemas de bases de datos diferentes
        - *pip install SQLAlchemy*
- Desarrollo web
    - Django - Marco web de alto nivel.
        - *pip install django*
- Flask: micro framework para Python basado en Werkzeug, Jinja 2. (Tiene licencia BSD)
    - *pip install flask*
- Analizador HTML
    - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    - - Analizador HTML/XML diseñado para proyectos de rápida ejecución como el raspado de pantalla, que acepta marcado incorrecto.
        - *pip install beautifulsoup4*
    - PyQuery: implementa jQuery en Python; aparentemente, es más rápido que BeautifulSoup.
- XML Processing
    - ElementTree - The Element type is a simple but flexible container object, designed to store hierarchical data structures, such as simplified XML infosets, in memory. –Note: Python 2.5 and up has ElementTree in the Standard Library
- GUI
    - PyQt - Enlaces para el marco multiplataforma Qt.
    - TkInter - El kit de herramientas de interfaz de usuario tradicional de Python.
- Análisis de datos, ciencia de datos y aprendizaje automático
    - Numpy: Numpy (Pytón numérico) es conocida como una de las bibliotecas de aprendizaje automático más populares en Python.
- Pandas: es una biblioteca de análisis de datos, ciencia de datos y aprendizaje automático en Python que proporciona estructuras de datos de alto nivel y una amplia variedad de herramientas para el análisis.
- SciPy: SciPy es una biblioteca de aprendizaje automático para desarrolladores e ingenieros de aplicaciones. La biblioteca SciPy contiene módulos para optimización, álgebra lineal, integración, procesamiento de imágenes y estadísticas.
- Scikit-Learn: es NumPy y SciPy. Se considera una de las mejores bibliotecas para trabajar con datos complejos.
- TensorFlow: es una biblioteca de aprendizaje automático creada por Google.
- Keras: se considera una de las mejores bibliotecas de aprendizaje automático en Python. Proporciona un mecanismo más sencillo para expresar redes neuronales. Keras también ofrece algunas de las mejores utilidades para compilar modelos, procesar conjuntos de datos, visualizar gráficos y mucho más.
- Red:
    - solicitudes: es un paquete que podemos usar para enviar solicitudes a un servidor (GET, POST, DELETE, PUT)
        - *pip install requests*

🌕 Siempre estás progresando y estás a 17 pasos de tu camino hacia la grandeza. Ahora haz algunos ejercicios para tu cerebro y tus músculos.

## Ejercicios: Día 17

1. Lee esta URL y encuentra las 10 palabras más frecuentes. romeo_and_juliet = [https://www.gutenberg.org/cache/epub/1513/pg1513.txt](https://www.gutenberg.org/cache/epub/1513/pg1513.txt)
2. Lee la API de gatos  [https://api.thecatapi.com/v1/breeds](https://api.thecatapi.com/v1/breeds) y encuentra:
    1. el mínimo, máximo, media, mediana y desviación estándar del peso de los gatos en unidades métricas.
    2. el mínimo, máximo, media, mediana y desviación estándar de la esperanza de vida de los gatos en años.
    3. Crea una tabla de frecuencias de países y razas de gatos
3. Lee la [API de países](https://restfulcountries.com/api-documentation/version/1) y encuentra
    1. los 10 países más grandes
    2. los 10 idiomas más hablados
    3. el número total de idiomas en la API de países

🎉 ¡FELICITACIONES! 🎉