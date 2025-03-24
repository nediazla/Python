# Dia 19 - Web Scraping

### Que es Web Scrapping

Internet está repleto de una enorme cantidad de datos que pueden utilizarse para diversos fines. Para recopilarlos, necesitamos saber cómo extraer datos de un sitio web.

El web scraping consiste en extraer y recopilar datos de sitios web y almacenarlos en un equipo local o en una base de datos.

En esta sección, utilizaremos beautifulsoup y el paquete requests para extraer datos. La versión del paquete que utilizamos es beautifulsoup 4.

Para empezar a extraer datos de sitios web, necesitas _requests_, _beautifoulSoup4_ y un _website_.

```sh
pip install requests
pip install beautifulsoup4
```

Para extraer datos de sitios web, se requieren conocimientos básicos de etiquetas HTML y selectores CSS. Dirigimos el contenido de un sitio web mediante etiquetas HTML, clases e identificadores.
Importemos las solicitudes y el módulo BeautifulSoup.

```python
import requests
from bs4 import BeautifulSoup
```

Declararemos la variable URL para el sitio web que vamos a rastrear.

```python
import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

try:
    # Hacemos la solicitud GET
    response = requests.get(url)
    
    # Verificamos el código de estado
    if response.status_code == 200:
        print("La solicitud fue exitosa!")
    else:
        print(f"Error: Código de estado {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Hubo un error al realizar la solicitud: {e}")
```

```sh
200
```

Usando beautifulSoup para analizar el contenido de la página

```python
import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content  # Obtenemos todo el contenido de la página
soup = BeautifulSoup(content, 'html.parser')  # BeautifulSoup lo analiza
print(soup.title)  # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text())  # UCI Machine Learning Repository: Data Sets
print(soup.body)  # Muestra todo el cuerpo de la página
print(response.status_code)

# Buscamos todas las tablas con el atributo 'cellpadding' igual a 3
tables = soup.find_all('table', {'cellpadding': '3'})
# Suponiendo que la primera tabla es la que nos interesa
table = tables[0]

# Recorremos todas las filas de la tabla (no solo la primera)
for tr in table.find_all('tr'):
    # Dentro de cada fila, buscamos las celdas <td>
    for td in tr.find_all('td'):
        print(td.get_text())  # Imprimimos el texto de cada celda
```


Si ejecutas este código, verás que la extracción está a la mitad. Puedes continuar, ya que forma parte del ejercicio 1.
Para consultar la documentación de beautifulsoup, consulta la documentación de [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start).

🌕 Eres tan especial, progresas cada día.

## 💻 Ejercicios: Día 19

1. Extrae datos del siguiente sitio web y guarda los datos como un archivo json (url = 'http://www.bu.edu/president/boston-university-facts-stats/'). 1. Extraiga la tabla en esta URL (https://archive.ics.uci.edu/ml/datasets.php) y conviértala en un archivo JSON.
2. Extraiga la tabla de presidentes y guarde los datos como JSON (https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). La tabla no está muy estructurada y la extracción puede tardar mucho tiempo.

🎉 ¡FELICIDADES! 🎉