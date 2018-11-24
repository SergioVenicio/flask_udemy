#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Blueprint, session, request, redirect


bp_requisicao = Blueprint('requisicao', __name__)


@bp_requisicao.route('/restrito')
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


@bp_requisicao.route('/proccess_form', methods=['GET', 'POST'])
def proccess_form():
    if request.method == 'GET':
        name = request.args.get('name', '')
        age = request.args.get('age', '')
    elif request.method == 'POST':
        name = request.form.get('name', '')
        age = request.form.get('age', '')

    return '<h1>{}<h1><h2>{}</h2>'.format(name, age)


@bp_requisicao.route('/create_session')
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


@bp_requisicao.route('/validacao', methods=['POST'])
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


@bp_requisicao.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')

    return redirect('')
