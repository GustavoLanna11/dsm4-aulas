# Do pacote importe Flask e o renderizador de páginas
from flask import Flask, render_template, request
from controllers import routes

# Criando instância do Flask
app = Flask(__name__, template_folder='views') # __name__ representa o nome da aplicação
routes.init_app(app)

# se for executado diretamente pelo interpretador
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True) #iniciando servidor
