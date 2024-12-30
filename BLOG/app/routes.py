from app import app
from flask import render_template
from flask import request
@app.route('/')
@app.route('/index/')

def index(nome):
    dados ="Estudante","Bonita","Emprendedora"
    return render_template('index.html', nome="Ariel", dados= dados)
@app.route('/contactos')
def contactos():
    return render_template('contactos.html')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autentificar', methods=['GET'])
def autentificar():
    usuaurio = request.arg.get('usuario')
    senha = request.args.get('senha')
e    return "usuario: {} e senha: {}".format(usuaurio,senha)