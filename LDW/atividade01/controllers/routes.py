from flask import render_template, request

def init_app(app):
    
    movielist = [{}]
    actors= ['Gustavo', 'Ana', 'Isabely', 'Yasmin']
    
    # Rota principal da aplicação '/'
    @app.route('/')
    def home(): #função que será executada ao acessar a rota
        return render_template('index.html')

    @app.route('/movies', methods=['GET', 'POST'])
    def movies():
        title = 'Pixels'
        year = 2018
        category = 'Comedy'
        sinopse= 'A movie of comedy and games!'
        director = {'name': 'Gustavo', 'age': 25, 'country': 'Brasil'}
        # tratando uma requisição post com request
        if request.method == 'POST':
            # Coletando o texto da input
            if request.form.get('actor'):
                actors.append(request.form.get('actor'))
        return render_template('movies.html', title=title, year=year, category=category, sinopse=sinopse, director=director, actors=actors)
    
    @app.route('/newmovie', methods=['GET', 'POST'])
    def newmovie():

        if request.method == 'POST':
            if request.form.get('title') and request.form.get('year') and request.form.get('category') and request.form.get('sinopse'): movielist.append({'Título': request.form.get('title'), 'Ano': request.form.get('year'), 'Categoria': request.form.get('category'), 'Sinopse': request.form.get('sinopse')})
        return render_template('newMovie.html', movielist=movielist)