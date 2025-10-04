from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Classe responsável por criar a entidade "Console" com seus atributos.
class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    idade = db.Column(db.Integer)
    genero = db.Column(db.String(150))
    nacionalidade = db.Column(db.String(150))

    def __init__(self, nome, idade, genero, nacionalidade):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.nacionalidade = nacionalidade

# Classe responsável por criar a entidade "Games" com seus atributos.
class Filme (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(150))
    sinopse = db.Column(db.String(500))
    # Criando a chave estrangeira
    autor_id = db.Column(db.Integer, db.ForeignKey('autor.id'))
    # Definindo o relacionamento
    autor = db.relationship('Autor', backref=db.backref('filme', lazy=True))

    def __init__(self, titulo, ano, categoria, sinopse, autor_id):
        self.titulo = titulo
        self.ano = ano
        self.categoria = categoria
        self.sinopse = sinopse
        self.autor_id = autor_id

# Classe de usuários
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    