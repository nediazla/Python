from config import create_app
from models.db import mysql
from routes.auth import auth
from routes.inventario import inventario
from routes.ventas import ventas

app = create_app()
mysql.init_app(app)

# Registrar Blueprints
app.register_blueprint(auth)
app.register_blueprint(inventario)
app.register_blueprint(ventas)

if __name__ == '__main__':
    app.run(debug=True)
