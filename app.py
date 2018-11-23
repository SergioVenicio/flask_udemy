#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

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


__app__.run()
