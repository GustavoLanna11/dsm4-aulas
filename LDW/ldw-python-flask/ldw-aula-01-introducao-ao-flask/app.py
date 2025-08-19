# Do pacote importe Flask e o renderizador de páginas
from flask import Flask, render_template

# Criando instância do Flask
app = Flask(__name__, template_folder='views') # __name__ representa o nome da aplicação

# Rota principal da aplicação '/'
@app.route('/')
def home(): #função que será executada ao acessar a rota
    return render_template('index.html')

@app.route('/games')
def games():
    title = 'Tarisland'
    year = 2022
    category = 'MMORPG'
    return render_template('games.html', title=title, year=year, category=category)

# se for executado diretamente pelo interpretador
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True) #iniciando servidor
