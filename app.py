#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

__app__ = Flask(__name__)
__app__.config.from_object('config.DevelopmentConfig')


@__app__.route('/')
def main():
    user = {'username': 'Sergio'}
    return render_template('index.html', user=user), 200


__app__.run()
