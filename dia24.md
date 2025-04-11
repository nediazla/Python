# Dia 24 - Python with MongoDB

# Python con MongoDB

Python es una tecnología backend que se puede conectar con diferentes aplicaciones de bases de datos. Se puede conectar tanto a bases de datos SQL como NoSQL. En esta sección, conectaremos Python con MongoDB, que es una base de datos NoSQL.

## MongoDB

MongoDB es una base de datos NoSQL. Almacena datos en un documento JSON, lo que la hace muy flexible y escalable. Veamos las diferentes terminologías de las bases de datos SQL y NoSQL. La siguiente tabla muestra la diferencia entre bases de datos SQL y NoSQL.

### SQL versus NoSQL

![](30-Days-Of-PythonimagesmongoDBsql-vs-nosql.png)

En esta sección, nos centraremos en MongoDB, una base de datos NoSQL. Regístrese en [mongoDB](https://www.mongodb.com/) haciendo clic en el botón de inicio de sesión y luego en "Registrarse" en la página siguiente.

![](img/20250409111303.png)
Páginas de registro de MongoDB

Complete los campos y haga clic en Continuar.

![](img/20250409111330.png)

Personalice su entorno
![](img/20250409111546.png)

Registro en MongoDB

Selecciona el plan gratuito

![](img/20250409111625.png)

Plan gratuito de MongoDB

Seleccione la región gratuita más cercana y asigne un nombre a su clúster.

![](img/20250409111646.png)

Nombre del clúster de MongoDB

Ahora se ha creado un entorno de pruebas gratuito. seleccione el tipo de conexion (Drivers)

![](img/20250409112012.png)

### Obtención de la cadena de conexión (URI de MongoDB)

![](img/20250409112048.png)

Copia el enlace de la cadena de conexión y obtendrás algo similar a esto:

```bash
'mongodb+srv://xnoxos:47jMJ0XFmnvYU6SL@cluster0.ly2wqrf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
```

No te preocupes por la URL, es un medio para conectar tu aplicación con MongoDB.

Python necesita un controlador MongoDB para acceder a la base de datos MongoDB. Usaremos *pymongo* con *dnspython* para conectar nuestra aplicación con MongoDB base. Dentro del directorio de tu proyecto, instala Pymongo y dnspython.

```bash
pip install pymongo dnspython
```

Se requiere instalar el módulo "dnspython" para usar las URI mongodb+srv://. dnspython es un kit de herramientas DNS para Python. Es compatible con casi todos los tipos de registros.

### Conexión de la aplicación Flask al clúster MongoDB

```python
# Importamos los módulos necesarios
from flask import Flask, render_template  # Flask para la app web
import os  # Para acceder a variables de entorno del sistema operativo
import pymongo  # PyMongo nos permite conectarnos y trabajar con MongoDB

# URI de conexión a MongoDB Atlas
# ⚠️ IMPORTANTE: Nunca debes compartir esta URI con credenciales reales en un repositorio público
# En producción se debe usar una variable de entorno para mayor seguridad
MONGODB_URI = 'mongodb+srv://usuario:contraseña@cluster0.ly2wqrf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

# Creamos el cliente MongoDB a partir de la URI
# Esto no abre la conexión inmediatamente, sino cuando sea necesario
client = pymongo.MongoClient(MONGODB_URI)

# ✅ Verificación de conexión:
# Esta línea imprime las bases de datos disponibles en el clúster
# Solo debe usarse para pruebas o depuración
print("Bases de datos disponibles:", client.list_database_names())

# Creamos una instancia de nuestra aplicación Flask
app = Flask(__name__)

# Punto de entrada principal del programa
if __name__ == '__main__':
    # Obtenemos el puerto desde una variable de entorno (si existe) o usamos 5000 por defecto
    port = int(os.environ.get("PORT", 5000))

    # Ejecutamos la aplicación en modo de depuración
    # 'host=0.0.0.0'
```

### Creación de una base de datos y una colección

### 🧩 Conceptos clave

|Concepto|Explicación|
|---|---|
|**Base de datos**|Es un contenedor donde se almacenan colecciones. Ej: `thirty_days_of_python`|
|**Colección**|Similar a una tabla en SQL. Contiene documentos (registros). Ej: `students`|
|**Documento**|Es un registro de datos en formato JSON. Ej: `{ name: 'Juan', age: 20 }`|
|**MongoDB Atlas**|Es la plataforma de base de datos en la nube que usamos para conectarnos remotamente desde Python.|

### 🧪 Ejemplo práctico: creación automática

```python
import pymongo

# URI de conexión (¡nunca publiques tus credenciales reales!)
MONGODB_URI = 'mongodb+srv://usuario:contraseña@cluster.mongodb.net/?retryWrites=true&w=majority'

# Creamos el cliente de MongoDB
client = pymongo.MongoClient(MONGODB_URI)

# Accedemos a la base de datos (se crea automáticamente si no existe)
db = client.mi_base_de_datos

# Accedemos a una colección llamada "estudiantes"
# MongoDB crea esta colección automáticamente cuando insertamos algo
students = db.estudiantes

# Insertamos un documento en la colección
students.insert_one({
    'name': 'Ana',
    'country': 'España',
    'city': 'Madrid',
    'age': 22
})
```
### 🔎 ¿Qué sucede internamente?

1. **`client = pymongo.MongoClient(...)`**  
    → Se establece conexión con el clúster MongoDB en la nube.
2. **`db = client.mi_base_de_datos`**  
    → MongoDB no necesita que crees la base de datos manualmente. Basta con usarla y se crea al guardar datos.
3. **`db.estudiantes.insert_one(...)`**  
    → Inserta un documento en una colección. Si la colección no existe, MongoDB la crea.

### Inserción de varios documentos en la colección

### 🧩 Conceptos clave

|Concepto|Explicación|
|---|---|
|**Documento**|Registro individual en MongoDB (formato tipo JSON).|
|**Colección**|Contenedor de documentos (como una tabla en SQL).|
|**Insertar varios documentos**|Podemos insertar uno por uno en un bucle, o todos juntos con `insert_many()`.|
|**Bucle `for`**|Nos permite recorrer listas de datos e insertar uno por uno.|

### 🧪 Opción 1: Insertar varios documentos con un bucle `for`

```python
import pymongo

# Conexión a MongoDB
MONGODB_URI = 'mongodb+srv://usuario:contraseña@cluster.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)

# Seleccionamos la base de datos y colección
db = client.mi_base_de_datos
students = db.estudiantes

# Lista de estudiantes a insertar
lista_estudiantes = [
    {'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34},
    {'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28},
    {'name': 'Sami', 'country': 'Finland', 'city': 'Cáceres', 'age': 25},
]

# Insertamos uno por uno
for estudiante in lista_estudiantes:
    students.insert_one(estudiante)
```

### 🧪 Opción 2: Insertar todos de una vez con `insert_many()`

```python
# Insertar todos los documentos al mismo tiempo
students.insert_many(lista_estudiantes)
```

### MongoDB Find

### 🧩 Conceptos clave

|Función|Uso|
|---|---|
|`find()`|Recupera todos los documentos de una colección. Retorna un cursor iterable.|
|`find_one()`|Devuelve solo **un** documento (el primero que encuentre).|
|`list()`|Convierte el resultado de `.find()` en una lista que se puede recorrer o pasar a HTML.|

```python
import pymongo

# Conectamos a MongoDB
client = pymongo.MongoClient("mongodb+srv://usuario:contraseña@cluster.mongodb.net/?retryWrites=true&w=majority")
db = client.mi_base_de_datos
students = db.estudiantes

# Obtenemos todos los documentos de la colección
resultado = students.find()

# Mostramos los documentos en consola
for estudiante in resultado:
    print(estudiante)
```

### 🧪 Ejemplo: Usar `find()` en Flask y mostrar en una página

#### 🧠 Ruta Flask (`app.py`)

```python
from flask import Flask, render_template
import pymongo

client = pymongo.MongoClient("mongodb+srv://usuario:contraseña@cluster.mongodb.net/?retryWrites=true&w=majority")
db = client.mi_base_de_datos
students = db.estudiantes

app = Flask(__name__)

@app.route('/')
def home():
    todos = list(students.find())  # Convertimos el cursor en lista
    return render_template('home.html', students=todos)

if __name__ == '__main__':
    app.run(debug=True)
```

### 🖼️ Plantilla HTML (`home.html`)

```html
<h1>Estudiantes</h1>
<ul>
  {% for student in students %}
    <li>{{ student.name }} ({{ student.age }} años) - {{ student.city }}, {{ student.country }}</li>
  {% endfor %}
</ul
```

### Find with Query

### 🧩 ¿Qué es un Query?

Un **query** en MongoDB es un filtro en forma de diccionario que le dice a la base de datos **qué documentos queremos obtener**.

Ejemplo:
```python
{ "country": "UK" }
```

Esto significa: _"Traeme todos los documentos donde el campo `country` sea igual a `UK`"._

### 🧪 Ejemplo 1: Búsqueda simple por país

```python
import pymongo

client = pymongo.MongoClient("mongodb+srv://usuario:contraseña@cluster.mongodb.net/?retryWrites=true&w=majority")
db = client.mi_base_de_datos
students = db.estudiantes

# Buscamos los estudiantes que viven en 'UK'
resultado = students.find({ "country": "UK" })

# Mostramos los resultados
for estudiante in resultado:
    print(estudiante)
```

### 🧪 Ejemplo 2: Búsqueda por edad mayor a 25

```python
# Buscamos estudiantes mayores de 25 años
resultado = students.find({ "age": { "$gt": 25 } })

for estudiante in resultado:
    print(estudiante)
```


|Operador|Significado|
|---|---|
|`$gt`|Mayor que (>)|
|`$lt`|Menor que (<)|
|`$gte`|Mayor o igual (>=)|
|`$lte`|Menor o igual (<=)|
|`$eq`|Igual (=)|
|`$ne`|Distinto (!=)|

### 🧪 Ejemplo 3: Múltiples condiciones

```python
# Estudiantes de España y mayores de 30 años
resultado = students.find({
    "country": "España",
    "age": { "$gt": 30 }
})
```
## MongoDB `find()` con modificadores (query modifiers)

### 🧩 ¿Qué son los modificadores?

Son funciones adicionales que se aplican **después** de un `.find()` para controlar **cuántos documentos devuelve**, **en qué orden**, y **desde dónde empezar**.

## 🔧 Modificadores principales

|Modificador|Uso|
|---|---|
|`.limit(n)`|Limita el número de resultados|
|`.skip(n)`|Salta los primeros `n` resultados|
|`.sort("campo", orden)`|Ordena los resultados por un campo (1: ascendente, -1: descendente)|

### 🧪 Ejemplo 1: Mostrar solo los primeros 3 documentos

```python
resultado = students.find().limit(3)

for estudiante in resultado:
    print(estudiante)
```

### 🧪 Ejemplo 2: Saltar los primeros 2 documentos y mostrar los siguientes

```python
resultado = students.find().skip(2)

for estudiante in resultado:
    print(estudiante)
```

### 🧪 Ejemplo 3: Ordenar por edad de menor a mayor

```python
resultado = students.find().sort("age", 1)  # 1 = ascendente

for estudiante in resultado:
    print(estudiante)
```

### 🧪 Ejemplo 4: Ordenar por edad de mayor a menor

```python
resultado = students.find().sort("age", -1)  # -1 = descendente

for estudiante in resultado:
    print(estudiante)
```

### 🧠 ¿Cómo lo explicás?

- `.find()` devuelve un **cursor**, y los modificadores se encadenan.
- `limit()` es útil para paginación o pruebas.
- `sort()` ayuda cuando queremos ver los más jóvenes o los más viejos.
- `skip()` permite implementar "paginación" avanzada.

#### Extra: combinar todo

```python
# Mostrar los 3 estudiantes más jóvenes, saltando el primero (paginación)
resultado = students.find().sort("age", 1).skip(1).limit(3)
```

### `find()` con Query y Modificadores en MongoDB

### 🔧 Sintaxis general

```python
collection.find({ "campo": "valor" }).sort("otro_campo", 1).limit(5)
```
### 🧪 Ejemplo 1: Mostrar los estudiantes de "España", ordenados por edad de menor a mayor

```python
resultado = students.find({ "country": "España" }).sort("age", 1)

for estudiante in resultado:
    print(estudiante)
```
### 🧪 Ejemplo 2: Mostrar los estudiantes mayores de 25, ordenados por nombre y limitar a 3 resultados

```python
resultado = students.find({ "age": { "$gt": 25 } }).sort("name", 1).limit(3)

for estudiante in resultado:
    print(estudiante)
```

### 🧪 Ejemplo 3: Paginación – mostrar página 2 de resultados, 3 por página

```python
pagina = 2
por_pagina = 3
saltos = (pagina - 1) * por_pagina

resultado = students.find().skip(saltos).limit(por_pagina)

for estudiante in resultado:
    print(estudiante)
```
### 🔍 Modificadores útiles

|Modificador|Descripción|
|---|---|
|`.sort("campo", 1/-1)`|Ordena ascendente (1) o descendente (-1)|
|`.limit(n)`|Muestra solo los primeros `n` resultados|
|`.skip(n)`|Omite los primeros `n` documentos (ideal para paginar)|

### Limitar documentos con `.limit()` en MongoDB

### 🧩 ¿Qué hace `.limit()`?

Cuando hacemos una consulta con `find()`, MongoDB devuelve **todos** los documentos que coinciden. Pero a veces solo queremos los primeros `n`.

📌 `.limit(n)` indica que solo se devuelvan los primeros **n resultados**.

---

### 🧪 Ejemplo 1: Mostrar solo los primeros 5 documentos

```python
resultado = students.find().limit(5)

for estudiante in resultado:
    print(estudiante)
```
### 🧪 Ejemplo 2: Limitar resultados con filtro

```python
# Solo queremos los 2 primeros estudiantes que son de Suecia
resultado = students.find({ "country": "Sweden" }).limit(2)

for estudiante in resultado:
    print(estudiante)
```
### 🧠 ¿Por qué usar `.limit()`?

- Para **evitar mostrar demasiados datos** (por ejemplo, en una tabla HTML).
- Para implementar **paginación** (mostrar 5 por página, luego los siguientes).
- Para hacer **consultas más rápidas** en bases de datos grandes.
### 💡 Actividad sugerida

> "Mostrá solo los primeros 3 estudiantes de la base de datos ordenados por edad (del menor al mayor)."

```python
resultado = students.find().sort("age", 1).limit(3)

for estudiante in resultado:
    print(estudiante)
```
### Extra: `.limit()` + `.skip()` → paginación

```python
pagina = 2
por_pagina = 3
saltos = (pagina - 1) * por_pagina

resultado = students.find().skip(saltos).limit(por_pagina)
```

📌 Esto muestra la "página 2", con 3 documentos por página.

### Inserción de datos desde un formulario web usando Flask + MongoDB

## 🧩 Estructura general

- **Ruta `/add` en Flask** → recibe los datos del formulario.
- **`add.html`** → contiene el formulario que el usuario llena.
- Flask usa `request.form` para obtener los datos.
- Luego guarda esos datos con `insert_one()` en MongoDB.

## 🧪 Código Flask: `app.py` (ruta `/add`)

```python
from flask import Flask, render_template, request, redirect, url_for
import pymongo

client = pymongo.MongoClient("mongodb+srv://usuario:contraseña@cluster.mongodb.net/?retryWrites=true&w=majority")
db = client.mi_base_de_datos
students = db.estudiantes

app = Flask(__name__)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        # Tomamos los datos del formulario
        name = request.form['name']
        country = request.form['country']
        city = request.form['city']
        age = int(request.form['age'])  # Convertimos edad a número

        # Insertamos en MongoDB
        students.insert_one({
            'name': name,
            'country': country,
            'city': city,
            'age': age
        })

        return redirect(url_for('home'))  # Redireccionamos al inicio

    # Si es GET, mostramos el formulario
    return render_template('add.html')
```
## 🖼️ Código HTML: `templates/add.html`

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Agregar estudiante</title>
</head>
<body>
    <h1>Agregar nuevo estudiante</h1>

    <form method="post">
        <label>Nombre:</label><br>
        <input type="text" name="name" required><br><br>

        <label>País:</label><br>
        <input type="text" name="country" required><br><br>

        <label>Ciudad:</label><br>
        <input type="text" name="city" required><br><br>

        <label>Edad:</label><br>
        <input type="number" name="age" required><br><br>

        <button type="submit">Guardar</button>
    </form>

    <br>
    <a href="{{ url_for('home') }}">⬅ Volver al inicio</a>
</body>
</html>
```

### Mostrar los datos guardados desde MongoDB en una tabla HTML (ruta `/`)

## 🧩 Estructura del flujo

- Flask consulta los documentos con `students.find()`.
- Convierte los resultados en una lista con `list(...)`.
- Envía esa lista al HTML con `render_template()`.
- El HTML recorre la lista con un bucle `for` y los muestra en pantalla.

### 🧪 Código Flask: `app.py` (ruta `/`)

```python
@app.route('/')
def home():
    try:
        todos = list(students.find())  # Obtenemos todos los documentos
        return render_template('home.html', students=todos)
    except Exception as e:
        return f"<h1>Error al conectar con MongoDB:</h1><p>{e}</p>"
```
### 🖼️ Código HTML: `templates/home.html`

```html
@app.route('/')
def home():
    try:
        todos = list(students.find())  # Obtenemos todos los documentos
        return render_template('home.html', students=todos)
    except Exception as e:
        return f"<h1>Error al conectar con MongoDB:</h1><p>{e}</p>"
```

### Validación de formularios y manejo de errores en Flask

## 🧩 ¿Por qué validar?

- Para asegurar que los campos obligatorios estén completos.
- Para evitar errores al insertar datos en la base.
- Para controlar tipos de datos (por ejemplo, que `edad` sea un número).
- Para dar retroalimentación al usuario si falta algo.

### 🧪 Validación básica en `app.py` (`/add`)

```python
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    error = None

    if request.method == 'POST':
        name = request.form['name'].strip()
        country = request.form['country'].strip()
        city = request.form['city'].strip()
        age = request.form['age'].strip()

        # Validamos que todos los campos estén completos
        if not name or not country or not city or not age:
            error = "Todos los campos son obligatorios."
        else:
            try:
                age = int(age)
                students.insert_one({
                    'name': name,
                    'country': country,
                    'city': city,
                    'age': age
                })
                return redirect(url_for('home'))
            except ValueError:
                error = "La edad debe ser un número entero."
            except Exception as e:
                error = f"Error al guardar: {e}"

    return render_template('add.html', error=error)
```
### 🖼️ Modificar `add.html` para mostrar errores

```html
<h1>Agregar nuevo estudiante</h1>

{% if error %}
    <p style="color: red;"><strong>{{ error }}</strong></p>
{% endif %}

<form method="post">
    <label>Nombre:</label><br>
    <input type="text" name="name" required><br><br>

    <label>País:</label><br>
    <input type="text" name="country" required><br><br>

    <label>Ciudad:</label><br>
    <input type="text" name="city" required><br><br>

    <label>Edad:</label><br>
    <input type="number" name="age" required><br><br>

    <button type="submit">Guardar</button>
</form>
```

### Eliminar documentos desde una interfaz web en Flask (DELETE)

### 🧩 Paso a paso

1. En la tabla (`home.html`), agregamos un botón "Eliminar" por cada estudiante.
2. Ese botón va a una ruta como `/delete/<id>`.
3. En `app.py`, definimos una ruta que recibe el ID y elimina el documento.
### 🧪 `app.py` – Ruta para eliminar

```python
from bson.objectid import ObjectId  # Necesario para trabajar con _id de MongoDB

@app.route('/delete/<id>')
def delete_student(id):
    try:
        students.delete_one({ "_id": ObjectId(id) })
        return redirect(url_for('home'))
    except Exception as e:
        return f"<h1>Error al eliminar estudiante:</h1><p>{e}</p>"
```

### 🖼️ `home.html` – Agregar botón "Eliminar"

```html
<td>
    <a href="{{ url_for('delete_student', id=student._id) }}">🗑 Eliminar</a>
</td>
```

### Actualizar documentos desde Flask (UPDATE)

### 🧩 Flujo de actualización

1. En la tabla, agregamos un botón "Editar".
2. El botón lleva a una ruta como `/edit/<id>`.
3. Esa ruta muestra un formulario **prellenado** con los datos actuales.
4. El usuario los edita y guarda → se actualiza el documento en MongoDB.

### 🧪 `app.py` – Ruta para mostrar y guardar cambios

```python
@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_student(id):
    student = students.find_one({ "_id": ObjectId(id) })

    if request.method == 'POST':
        updated_data = {
            'name': request.form['name'],
            'country': request.form['country'],
            'city': request.form['city'],
            'age': int(request.form['age'])
        }
        students.update_one({ "_id": ObjectId(id) }, { "$set": updated_data })
        return redirect(url_for('home'))

    return render_template('edit.html', student=student)
```

### 🖼️ `edit.html` – Formulario para editar

```html
<h1>Editar Estudiante</h1>
<form method="post">
    <label>Nombre:</label><br>
    <input type="text" name="name" value="{{ student.name }}" required><br><br>

    <label>País:</label><br>
    <input type="text" name="country" value="{{ student.country }}" required><br><br>

    <label>Ciudad:</label><br>
    <input type="text" name="city" value="{{ student.city }}" required><br><br>

    <label>Edad:</label><br>
    <input type="number" name="age" value="{{ student.age }}" required><br><br>

    <button type="submit">Guardar cambios</button>
</form>
```

### 🖼️ `home.html` – Agregar botón "Editar"

```html
<td>
    <a href="{{ url_for('edit_student', id=student._id) }}">✏️ Editar</a>
</td>
```

## 💻 Exercises: Day 24

🎉 Felicidades! 🎉