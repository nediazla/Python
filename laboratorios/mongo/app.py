from flask import Flask, render_template, request, redirect, url_for
import pymongo
from bson.objectid import ObjectId
import os

# URI de conexión a MongoDB Atlas
MONGODB_URI = 'mongodb+srv://xnoxos:47jMJ0XFmnvYU6SL@cluster0.ly2wqrf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

# Cliente MongoDB
client = pymongo.MongoClient(MONGODB_URI, connect=False)
db = client.db
students = db.students

# Aplicación Flask
app = Flask(__name__)

@app.route('/')
def home():
    try:
        datos = list(students.find())
        return render_template('home.html', students=datos)
    except Exception as e:
        return f"<h1>[ ! ] Error al conectar con MongoDB:</h1><p>{e}</p>"

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        city = request.form['city']
        age = request.form['age']

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
                error = f"Error al guardar estudiante: {e}"

    return render_template('add.html', error=error)

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

@app.route('/delete/<id>')
def delete_student(id):
    try:
        students.delete_one({ "_id": ObjectId(id) })
        return redirect(url_for('home'))
    except Exception as e:
        return f"<h1>Error al eliminar estudiante:</h1><p>{e}</p>"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
