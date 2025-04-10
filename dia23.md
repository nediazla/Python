# Dia 23 - python_web

## Python para la Web

Python es un lenguaje de programación de propósito general y se puede usar en muchos entornos. En esta sección, veremos cómo usar Python para la web. Existen muchos frameworks web de Python. Django y Flask son los más populares. Hoy veremos cómo usar Flask para el desarrollo web.

### Flask

Flask es un framework de desarrollo web escrito en Python. Flask utiliza el motor de plantillas Jinja2. Flask también se puede usar con otras bibliotecas front-end modernas como React.

Si aún no ha instalado el paquete virtualenv, instálelo primero. El entorno virtual permitirá aislar las dependencias del proyecto de las dependencias de la máquina local.

### Estructura de carpetas

Después de completar todos los pasos, la estructura de archivos de su proyecto debería verse así:

```bash
├── Procfile
├── app.py
├── env
│   ├── bin
├── requirements.txt
├── static
│   └── css
│       └── main.css
└── templates
    ├── about.html
    ├── home.html
    ├── layout.html
    ├── post.html
    └── result.html
```

Configuración del directorio del proyecto

Sigue los siguientes pasos para empezar a usar Flask.

Paso 1: instala virtualenv con el siguiente comando.

```bash
pip install virtualenv
```

Paso 2:

```bash
xnoxos@ubuntu:~/Desktop$ mkdir python_for_web
xnoxos@ubuntu:~/Desktop$ cd python_for_web/
xnoxos@ubuntu:~/Desktop/python_for_web$ virtualenv venv
xnoxos@ubuntu:~/Desktop/python_for_web$ source venv/bin/activate
(env) xnoxos@ubuntu:~/Desktop/python_for_web$ pip freeze
(env) xnoxos@ubuntu:~/Desktop/python_for_web$ pip install Flask
(env) xnoxos@ubuntu:~/Desktop/python_for_web$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
(env) xnoxos@ubuntu:~/Desktop/python_for_web$
```

Creamos un director de proyecto llamado python_for_web. Dentro del proyecto, creamos un entorno virtual *venv*, que podría tener cualquier nombre, pero yo prefiero llamarlo *venv*. Luego, activamos el entorno virtual. Usamos pip freeze para comprobar los paquetes instalados en el directorio del proyecto. El resultado de pip freeze fue vacío porque aún no se había instalado un paquete.

Ahora, creemos el archivo app.py en el directorio del proyecto y escribamos el siguiente código. El archivo app.py será el archivo principal del proyecto. El siguiente código contiene los módulos flask y os.

### Creando rutas

La ruta de inicio.

```python
# Importamos Flask desde el módulo flask
from flask import Flask

# Importamos el módulo del sistema operativo para acceder a variables de entorno
import os

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta principal (home)
@app.route('/')  # Este decorador define la ruta de inicio ("/")
def home():
    return '<h1>Bienvenido</h1>'  # Respuesta HTML para la ruta principal

# Ruta "about"
@app.route('/about')  # Este decorador define la ruta "/about"
def about():
    return '<h1>Sobre nosotros</h1>'  # Respuesta HTML para la ruta "about"

# Punto de entrada principal de la aplicación
if __name__ == '__main__':
    # Obtenemos el puerto desde la variable de entorno "PORT" si existe,
    # si no, usamos el puerto 5000 por defecto
    port = int(os.environ.get("PORT", 5000))

    # Ejecutamos la aplicación en modo debug y escuchando en todas las interfaces de red
    app.run(debug=True, host='0.0.0.0', port=port)
```

Para ejecutar la aplicación Flask, escriba `python app.py` en el directorio principal de la aplicación Flask.

Después de ejecutar `*python app.py*`, verifique el host local 5000.

Agreguemos una ruta adicional.
Creando una ruta

```python
# Importamos Flask desde el módulo flask
from flask import Flask

# Importamos el módulo del sistema operativo para usar variables de entorno
import os

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta principal ("/")
@app.route('/')  # Este decorador define la ruta de inicio
def home():
    return '<h1>Bienvenido</h1>'  # Respuesta HTML para la página principal

# Ruta secundaria ("/about")
@app.route('/about')  # Este decorador define la ruta "/about"
def about():
    return '<h1>Sobre nosotros</h1>'  # Respuesta HTML para la página "Sobre nosotros"

# Punto de entrada principal de la aplicación
if __name__ == '__main__':
    # Para despliegue usamos la variable de entorno "PORT"
    # Esto permite que funcione tanto en desarrollo como en producción
    port = int(os.environ.get("PORT", 5000))

    # Ejecutamos la app en modo debug, escuchando en todas las interfaces
    app.run(debug=True, host='0.0.0.0', port=port)
```

Ahora, añadimos la ruta "about" al código anterior. ¿Qué sucede si queremos renderizar un archivo HTML en lugar de una cadena? Es posible renderizar un archivo HTML mediante la función *render_templae*. Creamos una carpeta llamada "templates" y creamos "home.html" y "about.html" en el directorio del proyecto. También importamos la función *render_template* desde Flask.

### Creación de plantillas

Crea los archivos HTML dentro de la carpeta "templates".

home.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Home</title>
</head>
<body>
  <h1>Welcome Home</h1> <!-- Encabezado principal de la página -->
</body>
</html>
```

about.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>About</title>
</head>
<body>
  <h1>About Us</h1> <!-- Encabezado principal de la página "Sobre nosotros" -->
</body>
</html>
```

### Python Script

app.py

```python
# Importamos Flask y la función render_template para usar plantillas HTML
from flask import Flask, render_template

# Importamos el módulo del sistema operativo para acceder a variables de entorno
import os

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta principal ("/")
@app.route('/')  # Este decorador define la ruta de inicio
def home():
    return render_template('home.html')  # Renderiza el archivo home.html desde la carpeta "templates"

# Ruta secundaria ("/about")
@app.route('/about')  # Este decorador define la ruta "/about"
def about():
    return render_template('about.html')  # Renderiza el archivo about.html desde la carpeta "templates"

# Punto de entrada principal de la aplicación
if __name__ == '__main__':
    # Usamos la variable de entorno "PORT" si está definida, de lo contrario usamos 5000 por defecto
    port = int(os.environ.get("PORT", 5000))

    # Ejecutamos la aplicación en modo debug, accesible desde cualquier IP (0.0.0.0)
    app.run(debug=True, host='0.0.0.0', port=port)
```

Como pueden ver, para acceder a diferentes páginas o navegar, necesitamos un menú de navegación. Añadamos un enlace a cada página o creemos un diseño que usemos para cada página.

### Navegación

```html
  <!-- Menú de navegación -->
  <nav>
    <ul>
      <li><a href="/">Home</a></li>
      <li><a href="/about">About</a></li>
    </ul>
  </nav>
```

Ahora podemos navegar entre las páginas usando el enlace anterior. Vamos a crear una página adicional que gestione los datos del formulario. Puedes llamarla como quieras; yo la llamo post.html.

Podemos inyectar datos en los archivos HTML usando el motor de plantillas Jinja2.

```python
# Importamos Flask y funciones útiles para plantillas y redirecciones
from flask import Flask, render_template, request, redirect, url_for

# Importamos el módulo del sistema operativo para variables de entorno
import os

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta principal ("/")
@app.route('/')  # Ruta de inicio
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']  # Lista de tecnologías
    name = '30 Days Of Python Programming'  # Nombre del proyecto
    return render_template(
        'home.html',
        techs=techs,
        name=name,
        title='Home'
    )

# Ruta "about"
@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template(
        'about.html',
        name=name,
        title='About Us'
    )

# Ruta "post"
@app.route('/post')
def post():
    name = 'Text Analyzer'
    return render_template(
        'post.html',
        name=name,
        title=name
    )

# Ejecutamos la aplicación
if __name__ == '__main__':
    # Obtenemos el puerto desde una variable de entorno o usamos 5000 por defecto
    port = int(os.environ.get("PORT", 5000))

    # Ejecutamos la app en modo debug y escuchando desde cualquier IP
    app.run(debug=True, host='0.0.0.0', port=port)
```

Veamos también las plantillas:

home.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Home</title>
</head>
<body>

  <!-- Menú de navegación -->
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>

  <!-- Título dinámico usando la variable 'name' -->
  <h1>Welcome to {{ name }}</h1>

  <!-- Lista de tecnologías (usando bucle for de Jinja2) -->
  <ul>
    {% for tech in techs %}
      <li>{{ tech }}</li>
    {% endfor %}
  </ul>

</body>
</html>
```

about.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>About Us</title>
</head>
<body>

  <!-- Menú de navegación -->
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>

  <!-- Contenido de la página "About" -->
  <h1>About Us</h1>

  <!-- Subtítulo dinámico con la variable 'name' -->
  <h2>{{ name }}</h2>

</body>
</html>

```

### Creación de un diseño

En los archivos de plantilla, hay mucho código repetido. Podemos escribir un diseño y eliminar la repetición. Crearemos el archivo layout.html dentro de la carpeta de plantillas.
Después de crear el diseño, lo importaremos a todos los archivos.

### Entrega de archivos estáticos

Crea una carpeta estática en el directorio de tu proyecto. Dentro de esta carpeta, crea la carpeta CSS o de estilos y crea una hoja de estilos CSS. Usamos el módulo *url_for* para entregar el archivo estático.

layout.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <!-- Fuentes de Google -->
  <link href="https://fonts.googleapis.com/css?family=Lato:300,400|Nunito:300,400|Raleway:300,400,500&display=swap" rel="stylesheet" />

  <!-- Hoja de estilos principal -->
  <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}" />

  <!-- Título dinámico según el bloque "title" -->
  {% if title %}
    <title>30 Days of Python - {{ title }}</title>
  {% else %}
    <title>30 Days of Python</title>
  {% endif %}
</head>
<body>

  <!-- Encabezado y menú de navegación -->
  <header>
    <div class="menu-container">
      <div>
        <a class="brand-name nav-link" href="/">30DaysOfPython</a>
      </div>
      <ul class="nav-lists">
        <li class="nav-list">
          <a class="nav-link active" href="{{ url_for('home') }}">Home</a>
        </li>
        <li class="nav-list">
          <a class="nav-link active" href="{{ url_for('about') }}">About</a>
        </li>
        <li class="nav-list">
          <a class="nav-link active" href="{{ url_for('post') }}">Text Analyzer</a>
        </li>
      </ul>
    </div>
  </header>

  <!-- Contenido específico de cada plantilla hija -->
  <main>
    {% block content %}{% endblock %}
  </main>

</body>
</html>
```

Ahora, eliminemos todo el código repetido en los demás archivos de plantilla e importemos el archivo layout.html. El href usa la función *url_for* con el nombre de la función de ruta para conectar cada ruta de navegación.

home.html

```html
{% extends 'layout.html' %}

{% block content %}
<div class="container">
  <h1>Welcome to {{ name }}</h1>

  <p>
    Esta aplicación limpia textos y analiza la cantidad de palabras, caracteres y 
    las palabras más frecuentes. Pruébala haciendo clic en "Text Analyzer" en el menú.
  </p>

  <p>Necesitas las siguientes tecnologías para construir esta aplicación web:</p>

  <ul class="tech-lists">
    {% for tech in techs %}
      <li class="tech">{{ tech }}</li>
    {% endfor %}
  </ul>
</div>
{% endblock %}
```

about.html

```html
{% extends 'layout.html' %}

{% block content %}
<div class="container">
  <h1>About {{ name }}</h1>

  <p>
    Este es un reto de programación en Python de 30 días. Si has llegado hasta aquí,
    ¡eres increíble! Felicitaciones por el excelente trabajo realizado.
  </p>
</div>
{% endblock %}
```

post.html

```html
{% extends 'layout.html' %}

{% block content %}
<div class="container">
  <h1>Text Analyzer</h1>

  <!-- Formulario que envía el contenido del texto a la ruta /post por método POST -->
  <form action="{{ url_for('post') }}" method="POST">
    <div>
      <textarea rows="25" name="content" autofocus></textarea>
    </div>
    <div>
      <input type="submit" class="btn" value="Process Text" />
    </div>
  </form>
</div>
{% endblock %}
```

Existen diferentes métodos de solicitud (GET, POST, PUT, DELETE). Estos métodos son comunes y permiten realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

En la ruta POST, usaremos los métodos GET y POST según el tipo de solicitud. Vea cómo se ve en el código a continuación. El método de solicitud es una función que gestiona los métodos de solicitud y también accede a los datos del formulario.
app.py

```python
# Importamos Flask y funciones necesarias
from flask import Flask, render_template, request, redirect, url_for
import os  # Para acceder a variables del sistema

# Creamos la instancia de la aplicación Flask
app = Flask(__name__)

# Desactivamos el cache de archivos estáticos (útil durante el desarrollo)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Ruta principal (home)
@app.route('/')
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name=name, title='Home')

# Ruta "about"
@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name=name, title='About Us')

# Ruta para mostrar resultados después del análisis de texto
@app.route('/result')
def result():
    return render_template('result.html')

# Ruta para el formulario de análisis de texto
@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)

    if request.method == 'POST':
        content = request.form['content']
        print(content)  # Aquí se puede analizar el texto

        # Puedes procesar el texto y enviar resultados a result.html
        # Por ahora redirigimos simplemente a la vista de resultado
        return redirect(url_for('result'))

# Ejecutamos la aplicación Flask
if __name__ == '__main__':
    # Obtenemos el puerto desde variable de entorno o usamos 5000 por defecto
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

Hasta ahora, hemos visto cómo usar plantillas, inyectar datos y crear un diseño común.
Ahora, gestionemos archivos estáticos. Crea una carpeta llamada static en el directorio del proyecto y una carpeta llamada css. Dentro de la carpeta css, crea el archivo main.css. Tu archivo main.css se vinculará al archivo layout.html.

No es necesario escribir el archivo css; cópialo y úsalo. Pasemos a la implementación.

### Implementación

### Creación de una cuenta de Heroku

Heroku ofrece un servicio gratuito de implementación para aplicaciones front-end y full-stack. Crea una cuenta en [heroku](https://www.heroku.com/) e instala la [CLI](https://devcenter.heroku.com/articles/heroku-cli) de Heroku en tu equipo.
Después de instalar Heroku, escribe el siguiente comando:

### Inicia sesión en Heroku

```bash
xnoxos@ubuntu:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
```

Veamos el resultado pulsando cualquier tecla. Al pulsar cualquier tecla, se abrirá la página de inicio de sesión de Heroku. Haga clic en ella. Su equipo local se conectará al servidor remoto de Heroku. Si está conectado al servidor remoto, verá esto.

```bash
xnoxos@ubuntu:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/browser/be12987c-583a-4458-a2c2-ba2ce7f41610
Logging in... done
Logged in as asabeneh@gmail.com
xnoxos@ubuntu:~$
```

### Crear requisitos y Procfile

Antes de enviar nuestro código al servidor remoto, necesitamos los requisitos.

- requirements.txt
- Procfile

```bash
(env) xnoxos@ubuntu:~/Desktop/python_for_web$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
(env) xnoxos@ubuntu:~/Desktop/python_for_web$ touch requirements.txt
(env) xnoxos@ubuntu:~/Desktop/python_for_web$ pip freeze > requirements.txt
(env) xnoxos@ubuntu:~/Desktop/python_for_web$ cat requirements.txt
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
(env) xnoxos@ubuntu:~/Desktop/python_for_web$ touch Procfile
(env) xnoxos@ubuntu:~/Desktop/python_for_web$ ls
Procfile          env/              static/
app.py            requirements.txt  templates/
(env) xnoxos@ubuntu:~/Desktop/python_for_web$
```

El Procfile tendrá el comando que ejecutará la aplicación en el servidor web en nuestro caso en Heroku.

```bash
web: python app.py
```

### Subiendo el proyecto a Heroku

Ahora está listo para desplegarse. Pasos para desplegar la aplicación en Heroku:

1. git init
2. git add
3. git commit -m “mensaje de confirmación”
4. heroku create “nombre de la aplicación en una sola palabra”
5. git push heroku master
6. heroku open (para lanzar la aplicación desplegada)

Después de este paso, obtendrás una aplicación como [esta](http://thirdaysofpython-practice.herokuapp.com/)

## Ejercicios: Día 23

1. Construirás [esta aplicación](https://thirtydaysofpython-v1-final.herokuapp.com/). Solo falta la parte del analizador de texto.

🎉 ¡FELICIDADES! 🎉