from flask import Blueprint, render_template, request, redirect, session, flash
from models.db import mysql

auth = Blueprint('auth', __name__)

@auth.route('/')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
    user = cursor.fetchone()

    if user:
        session['usuario'] = username
        return redirect('/ventas')
    else:
        flash('Credenciales incorrectas')
        return redirect('/')





