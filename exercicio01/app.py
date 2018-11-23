#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

__app__ = Flask(__name__)


class Objectives(object):
    def __init__(self, objectives):
        self.objectives = objectives or []

    def __iter__(self):
        return (objective for objective in self.objectives)


class User(object):
    def __init__(self, name, age, objectives):
        self.name = name
        self.age = age
        self.objectives = objectives


@__app__.route('/')
def main():
    objectives = Objectives(['Objective 1', 'Objective 2'])
    user = User('Sergio', 23, objectives)
    return render_template('primeiro_projeto.html', user=user), 200


__app__.run()
