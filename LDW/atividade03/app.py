# Do pacote importe Flask e o renderizador de páginas
from flask import Flask, render_template, request
from controllers import routes
from models.database import db
import pymysql

# Criando instância do Flask
app = Flask(__name__, template_folder='views') # __name__ representa o nome da aplicação
routes.init_app(app)

DB_NAME = 'streamx'
app.config['DATABASE_NAME'] = DB_NAME

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/streamx'

# Secret para as flash messages
app.config['SECRET_KEY'] = 'streamxsecret'

if __name__ == '__main__':
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            print(f"Banco de dados está criado!")
    except Exception as e:
        print(f"Erro ao criar o banco de dados: {e}")   
    finally:
        connection.close()

    db.init_app(app=app)

    with app.test_request_context():
        db.create_all()
    app.run(host='localhost', port=5000, debug=True)


