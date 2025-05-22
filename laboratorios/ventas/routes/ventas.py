from flask import Blueprint, render_template, request, redirect, session, url_for
from models.db import mysql

ventas = Blueprint('ventas', __name__)

@ventas.route('/ventas')
def ventas_page():
    if 'usuario' not in session:
        return redirect('/')
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    return render_template('ventas.html', productos=productos)

@ventas.route('/realizar_venta', methods=['POST'])
def realizar_venta():
    producto_id = request.form['producto_id']
    cantidad = int(request.form['cantidad'])

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT nombre, precio FROM productos WHERE id = %s', [producto_id])
    producto = cursor.fetchone()
    nombre_producto, precio = producto
    total = precio * cantidad

    # Guardar venta
    cursor.execute('INSERT INTO ventas (producto_id, cantidad, total) VALUES (%s, %s, %s)', (producto_id, cantidad, total))
    cursor.execute('UPDATE productos SET stock = stock - %s WHERE id = %s', (cantidad, producto_id))
    mysql.connection.commit()

    # Redirigir a la factura
    return redirect(url_for('ventas.mostrar_factura', nombre=nombre_producto, precio=precio, cantidad=cantidad, total=total))

@ventas.route('/factura')
def mostrar_factura():
    nombre = request.args.get('nombre')
    precio = float(request.args.get('precio'))
    cantidad = int(request.args.get('cantidad'))
    total = float(request.args.get('total'))

    return render_template('factura.html', nombre=nombre, precio=precio, cantidad=cantidad, total=total)
