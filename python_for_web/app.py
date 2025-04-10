# Importamos Flask y sus funciones necesarias
from flask import Flask, render_template, request, redirect, url_for
import os  # Importamos el módulo del sistema operativo

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Desactivamos el almacenamiento en caché de archivos estáticos
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


# Ruta principal o página de inicio
@app.route('/')  # Este decorador crea la ruta para la página de inicio
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']  # Lista de tecnologías
    name = 'Class Of Python Programming'  # Nombre de la clase o curso
    return render_template('home.html', techs=techs, name=name, title='Home')


# Ruta para la página "Acerca de"
@app.route('/about')
def about():
    name = 'Class Of Python Programming'
    return render_template('about.html', name=name, title='About Us')


# Ruta para la página de resultados
@app.route('/result')
def result():
    return render_template('result.html')


# Ruta para el formulario y procesamiento de texto
@app.route('/post', methods=['GET', 'POST'])
def post():
    name = 'Text Analyzer'

    # Si se accede a la ruta con GET, se muestra el formulario
    if request.method == 'GET':
        return render_template('post.html', name=name, title=name)

    # Si se envía el formulario con POST, se procesa el contenido
    if request.method == 'POST':
        content = request.form['content']  # Se obtiene el contenido del formulario
        return redirect(url_for('result'))  # Se redirige a la página de resultados


# Bloque principal para ejecutar la app
if __name__ == '__main__':
    # Configuramos el puerto para producción o desarrollo
    port = int(os.environ.get("PORT", 5000))

    # Ejecutamos la app con depuración activada y accesible desde cualquier host
    app.run(debug=True, host='0.0.0.0', port=port)
