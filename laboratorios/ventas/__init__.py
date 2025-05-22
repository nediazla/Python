from flask import Flask
from ventas.routes import auth, inventario, ventas

def create_app():
    app = Flask(__name__)
    app.secret_key = '12345'

    app.register_blueprint(auth.bp)
    app.register_blueprint(inventario.bp)
    app.register_blueprint(ventas.bp)

    return app