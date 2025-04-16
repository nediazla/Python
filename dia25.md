
# Día 25 - APIs en Python con Flask y MongoDB

## 🧠 ¿Qué es una API?

Una **API** (*Application Programming Interface*) es un conjunto de reglas que permite que diferentes programas se comuniquen entre sí. En el contexto web, las APIs permiten que aplicaciones compartan datos y funcionalidades usando **HTTP** y formatos como **JSON**.

---

## 🌍 ¿Qué es una API RESTful?

Una API RESTful sigue el estilo REST, usando métodos HTTP estándar para interactuar con recursos:

| Método | Acción     |
|--------|------------|
| GET    | Obtener    |
| POST   | Crear      |
| PUT    | Actualizar |
| DELETE | Eliminar   |

---

## 🚦 Ciclo de Solicitud y Respuesta HTTP

1. El **cliente** (navegador o app) hace una solicitud HTTP.
2. El **servidor** responde con un código de estado (ej: 200 OK) y datos si corresponde.

---

## 🧪 Consumiendo una API pública con Python

```python
import requests

url = "https://api.thecatapi.com/v1/breeds"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Total razas: {len(data)}")
    print("Ejemplo:", data[0]["name"])
```

---

## 🛠 Crear una API RESTful con Flask y MongoDB

### Setup inicial

```bash
pip install flask pymongo
```

---

## 🌐 Estructura general de una API con Flask

```python
from flask import Flask, request, Response, jsonify
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

MONGODB_URI = "mongodb+srv://usuario:contraseña@cluster0.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(MONGODB_URI)
db = client["thirty_days_of_python"]
students = db.students
```

---

### 📥 GET - Obtener todos los estudiantes

```python
@app.route('/api/v1.0/students', methods=['GET'])
def get_students():
    data = list(students.find())
    return Response(dumps(data), mimetype='application/json')
```

---

### 🔍 GET - Obtener un estudiante por ID

```python
@app.route('/api/v1.0/students/<id>', methods=['GET'])
def get_student(id):
    student = students.find_one({"_id": ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')
```

---

### 📝 POST - Crear nuevo estudiante

```python
@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    data = request.get_json()
    data["created_at"] = datetime.now()
    result = students.insert_one(data)
    return jsonify({"id": str(result.inserted_id)}), 201
```

---

### 🛠 PUT - Actualizar estudiante

```python
@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    students.update_one({"_id": ObjectId(id)}, {"$set": data})
    return jsonify({"message": "Estudiante actualizado"})
```

---

### 🗑 DELETE - Eliminar estudiante

```python
@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    students.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Estudiante eliminado"})
```

---

### ▶ Ejecutar la aplicación

```python
if __name__ == "__main__":
    app.run(debug=True, port=5000)
```

---

## 🧪 Prueba la API

- Utilizá [Postman](https://www.postman.com/) o [Insomnia](https://insomnia.rest/)
- Endpoints:
  - `GET /api/v1.0/students`
  - `GET /api/v1.0/students/<id>`
  - `POST /api/v1.0/students`
  - `PUT /api/v1.0/students/<id>`
  - `DELETE /api/v1.0/students/<id>`

---

## 💻 Ejercicios sugeridos

1. Crear una API para productos (nombre, precio, categoría).
2. Implementar búsqueda por nombre.
3. Agregar campo "activo" y filtrar solo productos activos.



## 🚀 Instrucciones para desplegar en **Replit** o **Render**

---

### 🛠 1. Archivos necesarios

Además de `archivo.py`, necesitás:

#### 📄 `requirements.txt`

```text
flask 
pymongo 
dnspython
```
### 🔐 2. Configurar variables de entorno

En **Replit** o **Render**, añadí:

|Variable|Valor|
|---|---|
|`MONGODB_URI`|tu URI de conexión MongoDB Atlas|
|`PORT`|(Render lo define automáticamente)|

### 🌐 3. Subida a Replit

1. Crea un nuevo Repl (tipo: **Python Flask**).
2. Sube `archivo.py` y `requirements.txt`.
3. En “Secrets” agregá tu `MONGODB_URI`.
4. Ejecutá y abrí la URL que te genera.

### 🚀 4. Despliegue en Render (opcional)

1. Sube el proyecto a GitHub.
2. Ve a [render.com](https://render.com) y crea un nuevo “Web Service”.
3. Conectá tu repo.
4. Configurá:
    - **Runtime**: Python
    - **Start command**: `python archivo.py`
    - **Environment**: agregar `MONGODB_URI` como variable