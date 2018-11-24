#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask, render_template, request, redirect, session

__app__ = Flask(__name__)
__app__.config.from_object('config.DevelopmentConfig')


@__app__.route('/')
def main():
    return render_template('forms.html'), 200


@__app__.route('/make_form/<method>')
def make_form(method='GET'):
    return render_template('make_form.html', method=method), 200


@__app__.route('/proccess_form', methods=['GET', 'POST'])
def proccess_form():
    if request.method == 'GET':
        name = request.args.get('name', '').encode('utf-8')
        age = request.args.get('age', '').encode('utf-8')
    elif request.method == 'POST':
        name = request.form.get('name', '').encode('utf-8')
        age = request.form.get('age', '').encode('utf-8')

    return '<h1>{}<h1><h2>{}</h2>'.format(name, age)


@__app__.route('/create_session')
def create_session():
    options = """
        <option selected>Escolha</option>
        <option value="funcionario">Funcionario</option>
        <option value="gerente">Gerente</option>
    """
    return u"""
        <h1>Inicio da sessão</h1>
        <form action="/validacao" method="POST">
            Usuario: <input type="text" name="user" /> <br>
            Tipo: <select name="tipo">{}</select>
            <button type="submit"> Salvar </button>
        </form>
    """.format(options), 200


@__app__.route('/validacao', methods=['POST'])
def validacao():
    if request.method != 'POST':
        return redirect('create_session')

    user = request.form.get('user')
    type_ = request.form.get('tipo')

    if not user or not type_:
        return redirect('')

    session['user'] = user
    session['tipo'] = type_

    return redirect('restrito')


@__app__.route('/restrito')
def restrito():
    logout = '<a href="logout">Logout</a>'
    type_ = session.get('tipo')
    user = session.get('user')

    if type_ == 'funcionario':
        welcome_message = u"""
            Olá, {} <br> Você é o mais novo funcionário, seja bem vindo.
            {}
        """.format(user, logout)
    elif type_ == 'gerente':
        welcome_message = u"""
            Olá, {} <br>
            sua função é gerenciar todos os funcionários da empresa.
            {}
        """.format(user, logout)
    else:
        return redirect('')

    return welcome_message


@__app__.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')

    return redirect('')


__app__.run()
