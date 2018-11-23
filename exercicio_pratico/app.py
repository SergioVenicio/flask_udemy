#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect

__app__ = Flask(__name__)


@__app__.route('/')
def main():
    return render_template('login.html'), 200


@__app__.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect('success')
    else:
        return redirect('')


@__app__.route('/success')
def success():
        return '<h1>Estou na tela principal!</h1>'


__app__.run()
