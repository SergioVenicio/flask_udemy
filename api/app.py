#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask, jsonify, make_response, request

__app__ = Flask(__name__)
__app__.config.from_object('config.DevelopmentConfig')

lista = [
    {'plataforma': 'desktop', 'nome': 'bfv', 'preco': 250.00},
]


@__app__.route('/jogos/api/v1/lista', methods=['GET', 'POST'])
@__app__.route('/jogos/api/v1/lista/<int:id>')
def get_games(id=None):
    if id is not None:
        return jsonify({'lista': lista[int(id) - 1]})

    return jsonify({'lista': lista})


@__app__.route('/jogos/api/v1/lista/add', methods=['POST'])
def add_games():
    if request.json:
        game = {
            'id': len(lista) + 1,
            'plataforma': request.json['plataforma'],
            'nome': request.json['nome'],
            'preco': float(request.json['preco'])
        }
        lista.append(game)

    return jsonify(**game)


@__app__.route('/jogos/api/v1/lista/put/<int:id>', methods=['PUT'])
def put_game(id=None):
    if id is not None and id > 0 and request.json:
        game = {
            'id': id,
            'plataforma': request.json['plataforma'],
            'nome': request.json['nome'],
            'preco': float(request.json['preco'])
        }

        lista[id - 1] = game

    return jsonify({'lista': lista})


@__app__.route('/jogos/api/v1/lista/del/<int:id>', methods=['DELETE'])
def del_game(id=None):
    try:
        lista.pop(id - 1)
    except IndexError:
        return jsonify({'error': 'Item não encontrado!'})

    return jsonify({'lista': lista})


@__app__.errorhandler(404)
def not_found(error):
    return make_response(
        jsonify({
            'error': 'URL não encontrada!'
        })
    )


__app__.run()
