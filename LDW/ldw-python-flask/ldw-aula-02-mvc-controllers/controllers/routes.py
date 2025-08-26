from flask import render_template, request

def init_app(app):
    
    gamelist = [{}]
    players= ['Gustavo', 'Ana', 'Isabely', 'Yasmin']
    
    # Rota principal da aplicação '/'
    @app.route('/')
    def home(): #função que será executada ao acessar a rota
        return render_template('index.html')

    @app.route('/games', methods=['GET', 'POST'])
    def games():
        title = 'Tarisland'
        year = 2022
        category = 'MMORPG'
        console = {'name': 'Playstation 5', 'manufacturer': 'Sony', 'year': 2020}
        # tratando uma requisição post com request
        if request.method == 'POST':
            # Coletando o texto da input
            if request.form.get('player'):
                players.append(request.form.get('player'))
        return render_template('games.html', title=title, year=year, category=category, players=players, console=console)
    
    @app.route('/newgame', methods=['GET', 'POST'])
    def newgame():

        if request.method == 'POST':
            if request.form.get('title') and request.form.get('year') and request.form.get('category'): gamelist.append({'Título': request.form.get('title'), 'Ano': request.form.get('year'), 'Categoria': request.form.get('category')})
        return render_template('newGame.html', gamelist=gamelist)