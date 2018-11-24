from database import Database
from flask_httpauth import HTTPBasicAuth
from flask import Blueprint, jsonify, make_response, request


bp_api = Blueprint('api', __name__, url_prefix='/api/v1')
db = Database()

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    return db.getUser(username, password)


@bp_api.route('/add/user', methods=['POST'])
def add_user():
    user_expression = 'username' in request.json and 'password' in request.json
    if request.json and user_expression:
        user = db.addUser(request.json)
        return jsonify({'user': user})

    return make_response(jsonify({
        'error': 'Username and password is required!'
    }))


@bp_api.route('/', methods=['GET'])
@bp_api.route('/<int:id>', methods=['GET'])
@auth.login_required
def get_games(id=None):
    if id is not None:
        game = db.getGame(id)
        return jsonify(**game)

    games = db.listGames()

    if games:
        return jsonify({'games': games})

    return make_response(jsonify({
        'error': 'Nenhum registro encontrado!'
    }), 404)


@bp_api.route('/add', methods=['POST'])
@auth.login_required
def save_game():
    if request.json:
        game = db.saveGame(request.json)

        return jsonify(game)


@bp_api.route('/alter/<int:id>', methods=['PUT'])
@auth.login_required
def alter_game(id=None):
    if request.json and id is not None:
        game = db.updateGame(id=id, data=request.json)

        return jsonify(**game)


@bp_api.route('/delete/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_game(id=None):
    if request.json and id is not None:
        db.deleteGame(id=id)
        games = db.listGames()

        return jsonify({'games': games})
