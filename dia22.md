# Day 22 - Pandas

## Pandas

Pandas es una herramienta de código abierto, de alto rendimiento y fácil de usar para estructuras de datos y análisis de datos en el lenguaje de programación Python.
Pandas añade estructuras de datos y herramientas diseñadas para trabajar con datos de tipo tabla, como *Series* y *Data Frames*.
Pandas proporciona herramientas para la manipulación de datos:

- Remodelación
- Fusión
- Ordenación
- Segmentación
- Agregación
- Imputación.

Si usa Anaconda, no necesita instalar Pandas.

### Instalación de Pandas

Para Mac:

```python
pip install conda
conda install pandas
```

Para Windows:

```python
pip install conda
pip install pandas
```

La estructura de datos de Pandas se basa en *Series* y *DataFrames*.

Una *serie* es una *columna* y un DataFrame es una *tabla multidimensional* compuesta por un conjunto de *series*. Para crear una serie de Pandas, debemos usar numpy para crear matrices unidimensionales o una lista de Python.
Veamos un ejemplo de una serie:

Nombres: Pandas Series

![](30-Days-Of-Pythonimagespandas-series-1.png)

Countries Series

![](30-Days-Of-Pythonimagespandas-series-2.png)

Cities Series

![](30-Days-Of-Pythonimagespandas-series-3.png)

Como puede ver, la serie de Pandas es solo una columna de datos. Si queremos tener varias columnas, usamos marcos de datos. El siguiente ejemplo muestra marcos de datos de Pandas.

Veamos un ejemplo de un marco de datos de Pandas:

![](30-Days-Of-Pythonimagespandas-dataframe-1.png)

Marco de datos de Pandas

Un marco de datos es un conjunto de filas y columnas. Observe la tabla a continuación; tiene muchas más columnas que el ejemplo anterior:

![](30-Days-Of-Pythonimagespandas-dataframe-2.png)

## Marco de datos de Pandas

A continuación, veremos cómo importar Pandas y cómo crear series y marcos de datos con Pandas.
### Importación de Pandas

```python
import pandas as pd  # Importa la librería pandas y la asigna el alias pd
import numpy as np   # Importa la librería numpy y la asigna el alias np

```

### Creación de series de Pandas con índice predeterminado

```python
# Lista de números
nums = [1, 2, 3, 4, 5]  # Definición de la lista de números

# Creación de una Serie de pandas a partir de la lista
s = pd.Series(nums)

# Imprime la Serie resultante
print(s)
```

### Creación de series de Pandas con índice personalizado

```python
# Lista de números
nums = [1, 2, 3, 4, 5]

# Creación de una Serie de pandas utilizando la lista de números
# Se asigna un índice personalizado a cada elemento
s = pd.Series(nums, index=[1, 2, 3, 4, 5])

# Imprime la Serie resultante
print(s)
```

```python
# Lista de frutas
fruits = ['Orange', 'Banana', 'Mango']

# Creación de una Serie de pandas a partir de la lista de frutas
# Se asigna un índice personalizado a cada fruta
fruits = pd.Series(fruits, index=[1, 2, 3])

# Imprime la Serie resultante
print(fruits)
```

### Creación de series de Pandas a partir de un diccionario

```python
# Diccionario con información
dct = {
    'name': 'Nelson',   # Nombre
    'country': 'Espana',  # País
    'city': 'Caceres'     # Ciudad
}

# Creación de una Serie de pandas a partir del diccionario
s = pd.Series(dct)

# Imprime la Serie resultante
print(s)
```

### Creando una serie constante de Pandas

```python
s = pd.Series(10, index = [1, 2, 3])
print(s)
```

### Creación de una serie de Pandas usando Linspace

```python
# Genera una secuencia de 10 números equidistantes entre 5 y 20
# np.linspace(inicio, fin, cantidad_de_elementos)
s = pd.Series(np.linspace(5, 20, 10))

# Imprime la Serie resultante
print(s)
```

## DataFrames

Los dataframes de Pandas se pueden crear de diferentes maneras.

### Creación de DataFrames a partir de una lista de listas

```python
import pandas as pd

# Lista de datos: cada sublista contiene información de una persona: [Nombre, País, Ciudad]
data = [
    ['Nelson', 'Espana, 'Caceres'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]

# Creación de un DataFrame de pandas a partir de la lista de datos
# Se especifican los nombres de las columnas: 'Names', 'Country' y 'City'
df = pd.DataFrame(data, columns=['Names', 'Country', 'City'])

# Imprime el DataFrame resultante
print(df)
```

|     | Names  | Country | City      |
| --- | ------ | ------- | --------- |
| 0   | Nelson | Espana  | Caceres   |
| 1   | David  | UK      | London    |
| 2   | John   | Sweden  | Stockholm |

### Creating DataFrame Using Dictionary

```python
# Diccionario con datos de personas, incluyendo nombre, país y ciudad
data = {
    'Name': ['Nelson', 'David', 'John'],           # Lista de nombres
    'Country': ['Espana', 'UK', 'Sweden'],          # Lista de países
    'City': ['Caceres', 'London', 'Stockholm']      # Lista de ciudades (corregido "Helsiki" por "Caceres")
}

# Creación de un DataFrame a partir del diccionario
df = pd.DataFrame(data)

# Imprime el DataFrame resultante
print(df)
```

|  | Name | Country | City |
| --- | --- | --- | --- |
| 0 | Nelson | Espana | Helsiki |
| 1 | David | UK | London |
| 2 | John | Sweden | Stockholm |

### Creating DataFrames from a List of Dictionaries

```python
# Lista de diccionarios, cada uno representa una fila de datos con nombre, país y ciudad
data = [
    {'Name': 'Nelson', 'Country': 'Espana', 'City': 'Caceres'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}
]

# Creación de un DataFrame de pandas a partir de la lista de diccionarios
df = pd.DataFrame(data)

# Imprime el DataFrame resultante
print(df)
```

|  | Name | Country | City |
| --- | --- | --- | --- |
| 0 | Nelson | Espana | Caceres |
| 1 | David | UK | London |
| 2 | John | Sweden | Stockholm |
## Lectura de archivos CSV con Pandas

Para descargar el archivo CSV, en este ejemplo, basta con usar la consola o la línea de comandos:

```bash
curl -O https://raw.githubusercontent.com/nediazla/Python/refs/heads/main/data/weight-height.csv
```

Coloque el archivo descargado en su directorio de trabajo.

```python
import pandas as pd  # Importa la librería pandas

# Lee un archivo CSV llamado 'weight-height.csv' y lo guarda en un DataFrame
df = pd.read_csv('weight-height.csv')

# Imprime el contenido del DataFrame
print(df)
```

Exploración de datos

Leamos solo las primeras 5 filas usando head()

```python
# Muestra las primeras 5 filas del DataFrame
# Podemos aumentar la cantidad de filas pasando un número como argumento al método head()
print(df.head())
```

```python
print(df.head(10))  # Muestra las primeras 10 filas
```

|  | Gender | Height | Weight |
| --- | --- | --- | --- |
| 0 | Male | 73.847017 | 241.893563 |
| 1 | Male | 68.781904 | 162.310473 |
| 2 | Male | 74.110105 | 212.740856 |
| 3 | Male | 71.730978 | 220.042470 |
| 4 | Male | 69.881796 | 206.349801 |

Exploremos también las últimas grabaciones del marco de datos usando los métodos tail().

```python
# Muestra las últimas 5 filas del DataFrame
# Podemos aumentar la cantidad de filas pasando un número como argumento al método tail()
print(df.tail())
```

```python
print(df.tail(8))  # Muestra las últimas 8 filas del DataFrame
```

|  | Gender | Height | Weight |
| --- | --- | --- | --- |
| 9995 | Female | 66.172652 | 136.777454 |
| 9996 | Female | 67.067155 | 170.867906 |
| 9997 | Female | 63.867992 | 128.475319 |
| 9998 | Female | 69.034243 | 163.852461 |
| 9999 | Female | 61.944246 | 113.649103 |

Como puede ver, el archivo CSV tiene tres filas: género, altura y peso. Si el DataFrame tuviera filas largas, sería difícil conocer todas las columnas. Por lo tanto, deberíamos usar un método para conocer las columnas. Desconocemos el número de filas. Usemos el método de forma.

```python
print(df.shape) # as you can see 10000 rows and three columns
```

Obtengamos todas las columnas usando columnas.

```python
print(df.columns)
```

Ahora, obtengamos una columna específica usando la clave de columna

```python
heights = df['Height'] # this is now a series
```

```python
print(heights)
```

```python
weights = df['Weight'] # this is now a series
```

```python
print(weights)
```

```python
print(len(heights) == len(weights))
```

El método describe() proporciona valores estadísticos descriptivos de un conjunto de datos.

```python
# Muestra información estadística descriptiva de los datos de altura
print(heights.describe())
```

```python
# Muestra información estadística descriptiva sobre los datos de peso
print(weights.describe())
```

```python
# Muestra información estadística descriptiva de todas las columnas numéricas del DataFrame
print(df.describe())
```

|  | Height | Weight |
| --- | --- | --- |
| count | 10000.000000 | 10000.000000 |
| mean | 66.367560 | 161.440357 |
| std | 3.847528 | 32.108439 |
| min | 54.263133 | 64.700127 |
| 25% | 63.505620 | 135.818051 |
| 50% | 66.318070 | 161.212928 |
| 75% | 69.174262 | 187.169525 |
| max | 78.998742 | 269.989699 |
Similar a describe(), el método info() también proporciona información sobre el conjunto de datos.

## Modificación de un DataFrame

Modificación de un DataFrame:
* Podemos crear un nuevo DataFrame
* Podemos crear una nueva columna y añadirla al DataFrame
* Podemos eliminar una columna existente de un DataFrame
* Podemos modificar una columna existente en un DataFrame
* Podemos cambiar el tipo de datos de los valores de columna en el DataFrame

### Creación de un DataFrame

Como siempre, primero importamos los paquetes necesarios. Ahora, importemos pandas y numpy, dos grandes amigos.

```python
import pandas as pd  # Importa la librería pandas
import numpy as np   # Importa la librería numpy

# Lista de diccionarios, donde cada diccionario representa una fila con datos personales
data = [
    {"Name": "Nelson", "Country": "Espana", "City": "Caceres"},
    {"Name": "David", "Country": "UK", "City": "London"},
    {"Name": "John", "Country": "Sweden", "City": "Stockholm"}
]

# Creación de un DataFrame a partir de la lista de diccionarios
df = pd.DataFrame(data)

# Imprime el DataFrame resultante
print(df)
```

|  | Name | Country | City |
| --- | --- | --- | --- |
| 0 | Nelson | Espana | Caceres |
| 1 | David | UK | London |
| 2 | John | Sweden | Stockholm |
Añadir una columna a un DataFrame es como añadir una clave a un diccionario.

Primero, usemos el ejemplo anterior para crear un DataFrame. Después de crearlo, comenzaremos a modificar las columnas y sus valores.

### Añadir una nueva columna

Agreguemos una columna de peso al DataFrame.

```python
# Lista de pesos correspondientes a cada persona
weights = [74, 78, 69]

# Agrega la columna 'Weight' al DataFrame
df['Weight'] = weights

# Muestra el DataFrame actualizado con la nueva columna
print(df)
```

|  | Name | Country | City | Weight |
| --- | --- | --- | --- | --- |
| 0 | Nelson | Espana | Caceres | 74 |
| 1 | David | UK | London | 78 |
| 2 | John | Sweden | Stockholm | 69 |

Agreguemos también una columna de altura al DataFrame.

```python
# Lista de alturas correspondientes a cada persona (en centímetros)
heights = [173, 175, 169]

# Agrega la columna 'Height' al DataFrame
df['Height'] = heights

# Muestra el DataFrame actualizado con la nueva columna
print(df)
```

|  | Name | Country | City | Weight | Height |
| --- | --- | --- | --- | --- | --- |
| 0 | Nelson | Espana | Caceres | 74 | 173 |
| 1 | David | UK | London | 78 | 175 |
| 2 | John | Sweden | Stockholm | 69 | 169 |
Como puede ver en el DataFrame anterior, añadimos las columnas Peso y Altura. Añadamos una columna adicional llamada IMC (Índice de Masa Corporal), calculando el IMC a partir de su masa y altura. El IMC se obtiene dividiendo la masa por el cuadrado de la altura (en metros): Peso/Altura * Altura.

Como puede ver, la altura está en centímetros, así que debemos cambiarla a metros. Modifiquemos la fila de altura.

### Modificación de los valores de las columnas

```python
# Convierte la altura de centímetros a metros
df['Height'] = df['Height'] * 0.01

# Muestra el DataFrame actualizado
print(df)
```

|  | Name | Country | City | Weight | Height |
| --- | --- | --- | --- | --- | --- |
| 0 | Nelson | Espana | Caceres | 74 | 1.73 |
| 1 | David | UK | London | 78 | 1.75 |
| 2 | John | Sweden | Stockholm | 69 | 1.69 |

```python
# Usar funciones hace que nuestro código sea más limpio, pero también se puede calcular el IMC sin una función

# Definición de la función para calcular el IMC
def calcular_bmi():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w, h in zip(weights, heights):
        b = w / (h * h)
        bmi.append(b)
    return bmi

# Llama a la función y guarda los resultados
bmi = calcular_bmi()

# Agrega los valores de IMC al DataFrame como una nueva columna
df['BMI'] = bmi

# Muestra el DataFrame actualizado
print(df)
```

|  | Name | Country | City | Weight | Height | BMI |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Nelson | Espana | Caceres | 74 | 1.73 | 24.725183 |
| 1 | David | UK | London | 78 | 1.75 | 25.469388 |
| 2 | John | Sweden | Stockholm | 69 | 1.69 | 24.158818 |
### Formato de columnas del DataFrame

Los valores de la columna BMI del DataFrame son de coma flotante con muchos dígitos significativos después del decimal. Cámbielos a un dígito significativo después del punto.

```python
# Redondea los valores del IMC a un decimal y los guarda en la misma columna 'BMI'
df['BMI'] = round(df['BMI'], 1)

# Muestra el DataFrame actualizado con el IMC redondeado
print(df)
```

|  | Name | Country | City | Weight | Height | BMI |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Nelson | Espana | Caceres | 74 | 1.73 | 24.7 |
| 1 | David | UK | London | 78 | 1.75 | 25.5 |
| 2 | John | Sweden | Stockholm | 69 | 1.69 | 24.2 |
La información en el DataFrame parece aún no estar completa, agreguemos las columnas de año de nacimiento y año actual.

```python
# Lista de años de nacimiento como enteros
birth_year = [1769, 1985, 1990]

# Serie con el año actual para cada persona
current_year = pd.Series(2025, index=[0, 1, 2])

# Agrega ambas columnas al DataFrame
df['Birth Year'] = birth_year
df['Current Year'] = current_year

# Muestra el DataFrame actualizado
print(df)
```

|     | Name     | Country | City      | Weight | Height | BMI  | Birth Year | Current Year |
| --- | -------- | ------- | --------- | ------ | ------ | ---- | ---------- | ------------ |
| 0   | Nelson | Espana | Caceres  | 74     | 1.73   | 24.7 | 1769       | 2025         |
| 1   | David    | UK      | London    | 78     | 1.75   | 25.5 | 1985       | 2025         |
| 2   | John     | Sweden  | Stockholm | 69     | 1.69   | 24.2 | 1990       | 2025         |

## Comprobación de los tipos de datos de los valores de columna

```python
print(df.Weight.dtype)
```

```python
# Convierte la columna 'Birth Year' a tipo numérico (entero)
df['Birth Year'] = pd.to_numeric(df['Birth Year'])

# Verifica el tipo de datos actualizado
print(df['Birth Year'].dtype)
```

Ahora mismo para el año en curso:

```python
# Convierte la columna 'Current Year' al tipo entero
df['Current Year'] = df['Current Year'].astype('int')

# Verifica el tipo de dato de la columna 'Current Year'
print(df['Current Year'].dtype)
```

Now, the column values of birth year and current year are integers. We can calculate the age.

```python
# Calcula la edad a partir del año actual y el año de nacimiento
df['Age'] = df['Current Year'] - df['Birth Year']
print(df)
```


```python
# Calcula las edades restando el año de nacimiento al año actual
ages = df['Current Year'] - df['Birth Year']

# Asigna las edades a una nueva columna llamada 'Ages'
df['Ages'] = ages

# Muestra el DataFrame actualizado
print(df)
```

|     | Name     | Country | City      | Weight | Height | BMI  | Birth Year | Current Year | Ages |
| --- | -------- | ------- | --------- | ------ | ------ | ---- | ---------- | ------------ | ---- |
| 0   | Nelson | Espana | Caceres  | 74     | 1.73   | 24.7 | 1769       | 2025         | 255  |
| 1   | David    | UK      | London    | 78     | 1.75   | 25.5 | 1985       | 2025         | 39   |
| 2   | John     | Sweden  | Stockholm | 69     | 1.69   | 24.2 | 1990       | 2025         | 34   |

La persona de la primera fila ha vivido hasta ahora 251 años. Es improbable que alguien viva tanto. O bien es un error tipográfico o los datos están manipulados. Por lo tanto, completemos esos datos con el promedio de las columnas sin incluir los valores atípicos.

Media = (35 + 30)/2


```python
# Calcula la media de dos edades (por ejemplo, 35 y 30)
mean = (35 + 30) / 2

# Imprime el resultado con una descripción clara
print('Media de edades:', mean)
```

### Boolean Indexing

```python
# Muestra las filas del DataFrame donde la edad es mayor a 120 (posibles datos atípicos)
print(df[df['Ages'] > 120])
```

|  | Name | Country | City | Weight | Height | BMI | Birth Year | Current Year | Ages |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Nelson | Espana | Caceres | 74 | 1.73 | 24.7 | 1769 | 2020 | 251 |

```python
print(df[df['Ages'] < 120])
```

|  | Name | Country | City | Weight | Height | BMI | Birth Year | Current Year | Ages |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | David | UK | London | 78 | 1.75 | 25.5 | 1985 | 2020 | 35 |
| 2 | John | Sweden | Stockholm | 69 | 1.69 | 24.2 | 1990 | 2020 | 30 |
## Ejercicios: Día 22

1. Leer el archivo hacker_news.csv del directorio de datos
2. Obtener las primeras cinco filas
3. Obtener las últimas cinco filas
4. Obtener la columna de título como serie de pandas
5. Contar el número de filas y columnas
- Filtrar los títulos que contienen Python
- Filtrar los títulos que contienen JavaScript
- Explorar los datos y comprenderlos

🎉 ¡FELICIDADES! 🎉
