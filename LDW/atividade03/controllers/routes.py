from flask import render_template, request, url_for, redirect, flash
import urllib.request, json
from models.database import db, Filme, Autor

def init_app(app):

    actors = ['Gustavo', 'Ana', 'Isabely', 'Yasmin']

    @app.route('/', endpoint='home')
    def home():
        return render_template('index.html')

    @app.route('/movies', methods=['GET', 'POST'], endpoint='movies')
    def movies():
        title = 'Pixels'
        year = 2018
        category = 'Comedy'
        sinopse = 'A movie of comedy and games!'
        director = {'name': 'Gustavo', 'age': 25, 'country': 'Brasil'}

        if request.method == 'POST':
            if request.form.get('actor'):
                actors.append(request.form.get('actor'))

        return render_template('movies.html', title=title, year=year, category=category, sinopse=sinopse, director=director, actors=actors)

    @app.route('/newmovie', methods=['GET', 'POST'], endpoint='newmovie')
    def newmovie():
        return render_template('newMovie.html', movielist=[])

    @app.route('/apimovies', methods=['GET'], endpoint='apimovies')
    @app.route('/apimovies/<int:id>', methods=['GET'], endpoint='apimovieinfo')
    def apimovies(id=None):
        url = 'https://yts.mx/api/v2/list_movies.json'
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())

        moviesList = data.get("data", {}).get("movies", [])

        if id:
            movieInfo = next((movie for movie in moviesList if movie['id'] == id), None)
            if movieInfo:
                return render_template('movieinfo.html', movieInfo=movieInfo)
            else:
                return f'Filme com a ID {id} não foi encontrado'
        else:
            return render_template('apimovies.html', moviesList=moviesList)

    @app.route('/cadfilmes', methods=['GET', 'POST'], endpoint='cadfilmes')
    def cadfilmes():
        autores = Autor.query.all()

        if request.method == 'POST':
            titulo = request.form.get('titulo')
            ano = request.form.get('ano')
            categoria = request.form.get('categoria')
            sinopse = request.form.get('sinopse')
            autor_id = request.form.get('autor_id')

            if not all([titulo, ano, categoria, sinopse, autor_id]):
                flash('Todos os campos são obrigatórios, incluindo o autor.')
                return redirect(url_for('cadfilmes'))

            novo_filme = Filme(
                titulo,
                ano,
                categoria,
                sinopse,
                autor_id
            )
            db.session.add(novo_filme)
            db.session.commit()
            flash('Filme cadastrado com sucesso!')
            return redirect(url_for('cadfilmes'))

        filmes = Filme.query.all()
        return render_template('cadfilmes.html', autores=autores, filmes=filmes)

    @app.route('/filmes/estoque', methods=['GET', 'POST'], endpoint='filmesestoque')
    @app.route('/filmes/estoque/delete/<int:id>')
    def filmesEstoque(id=None):
        if id:
            filme = Filme.query.get(id)
            if filme:
                db.session.delete(filme)
                db.session.commit()
            return redirect(url_for('filmesestoque'))

        if request.method == 'POST':
            autor_id = request.form.get('autor')
            if not autor_id:
                flash('Selecione um autor para cadastrar o filme.')
                return redirect(url_for('filmesestoque'))

            newfilme = Filme(
                request.form['titulo'],
                request.form['ano'],
                request.form['categoria'],
                request.form['sinopse'],
                autor_id
            )
            db.session.add(newfilme)
            db.session.commit()
            return redirect(url_for('filmesestoque'))

        page = request.args.get('page', 1, type=int)
        per_page = 3
        filmes_page = Filme.query.paginate(page=page, per_page=per_page)

        autores = Autor.query.all()
        return render_template('filmesestoque.html', filmesestoque=filmes_page, autores=autores)

    @app.route('/filmes/edit/<int:id>', methods=['GET', 'POST'], endpoint='filmeedit')
    def filmeEdit(id):
        f = Filme.query.get(id)
        if not f:
            flash('Filme não encontrado.')
            return redirect(url_for('cadfilmes'))

        autores = Autor.query.all()

        if request.method == 'POST':
            f.titulo = request.form['titulo']
            f.ano = request.form['ano']
            f.categoria = request.form['categoria']
            f.sinopse = request.form['sinopse']
            autor_id = request.form.get('autor')
            if autor_id:
                f.autor_id = autor_id
            db.session.commit()
            flash(f'Filme "{f.titulo}" atualizado com sucesso!')
            return redirect(url_for('cadfilmes'))

        return render_template('editfilme.html', f=f, autores=autores)

    @app.route('/filmes/delete/<int:id>', methods=['GET'], endpoint='filmesdelete')
    def filmesDelete(id):
        filme = Filme.query.get_or_404(id)
        db.session.delete(filme)
        db.session.commit()
        flash(f'Filme "{filme.titulo}" excluído com sucesso.')
        return redirect(url_for('cadfilmes'))

    @app.route('/autores/estoque', methods=['GET', 'POST'], endpoint='autoresestoque')
    @app.route('/autores/estoque/delete/<int:id>')
    def autoresEstoque(id=None):
        if id:
            autor = Autor.query.get(id)
            if autor:
                db.session.delete(autor)
                db.session.commit()
            return redirect(url_for('autoresestoque'))

        if request.method == 'POST':
            newautor = Autor(
                request.form['nome'],
                request.form['idade'],
                request.form['genero'],
                request.form['nacionalidade']
            )
            db.session.add(newautor)
            db.session.commit()
            return redirect(url_for('autoresestoque'))

        page = request.args.get('page', 1, type=int)
        per_page = 3
        autores_page = Autor.query.paginate(page=page, per_page=per_page)

        return render_template('autorestoque.html', autoresestoque=autores_page)

    @app.route('/autores/edit/<int:id>', methods=['GET', 'POST'], endpoint='autoredit')
    def autorEdit(id):
        autor = Autor.query.get(id)
        if not autor:
            flash('Autor não encontrado.')
            return redirect(url_for('autoresestoque'))

        if request.method == 'POST':
            autor.nome = request.form['nome']
            autor.idade = request.form['idade']
            autor.genero = request.form['genero']
            autor.nacionalidade = request.form['nacionalidade']
            db.session.commit()
            return redirect(url_for('autoresestoque'))

        return render_template('editautor.html', autor=autor)

    @app.route('/autores/estoque/delete/<int:id>', methods=['GET'], endpoint='autoresdelete')
    def autoresDelete(id):
        autor = Autor.query.get_or_404(id)
        db.session.delete(autor)
        db.session.commit()
        flash(f'Autor "{autor.nome}" excluído com sucesso.')
        return redirect(url_for('autoresestoque'))
