from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    name = 'Curso de Programacion con Python'
    return render_template('home.html', name=name, tittle='Inicio')

@app.route('/about')
def about():
    name = 'Curso de Programacion con Python'
    return render_template('about.html', name=name, tittle='Nosotros')

@app.route('/contact')
def contact():
    name = 'Curso de Programacion con Python'
    return render_template('contact.html', name=name, tittle='Contactenos')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
