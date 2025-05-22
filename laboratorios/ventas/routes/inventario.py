from flask import Blueprint, render_template, request, redirect
from models.db import mysql

inventario = Blueprint('inventario', __name__)

@inventario.route('/inventario')
def ver_inventario():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    return render_template('inventario.html', productos=productos)

@inventario.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    nombre = request.form['nombre']
    precio = request.form['precio']
    stock = request.form['stock']

    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)', (nombre, precio, stock))
    mysql.connection.commit()
    return redirect('/inventario')

