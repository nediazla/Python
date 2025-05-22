import pymysql
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = '12345'

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'Lara1382'
    app.config['MYSQL_DB'] = 'login_system'

    return app
