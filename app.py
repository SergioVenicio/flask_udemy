#!/usr/bin/python
# -*- coding: utf-8 -*-


from flask import Flask, render_template
from requisicao import bp_requisicao


__app__ = Flask(__name__)
__app__.config.from_object('config.DevelopmentConfig')
__app__.register_blueprint(bp_requisicao)


@__app__.route('/')
def main():
    return render_template('forms.html'), 200


@__app__.route('/make_form/<method>')
def make_form(method='GET'):
    return render_template('make_form.html', method=method), 200


__app__.run()
