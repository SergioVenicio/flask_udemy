#!/usr/bin/python
# -*- coding: utf-8 -*-


from api import bp_api
from flask import Flask, jsonify, make_response


__app__ = Flask(__name__)
__app__.config.from_object('config.DevelopmentConfig')
__app__.register_blueprint(bp_api)


@__app__.errorhandler(404)
def not_found(error):
    return make_response(
        jsonify({
            'error': 'URL não encontrada!'
        })
    )


__app__.run()
