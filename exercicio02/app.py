#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template

__app__ = Flask(__name__)


class Objetos(object):
    def __init__(self):
        self.objetos = {}

    def add_element(self, element, key):
        self.objetos[key] = element

    def __getitem__(self, key):
        if key not in self.objetos:
            return False

        return self.objetos[key]


@__app__.route('/')
def ola_mundo():
    objetos = Objetos()

    frutas = ['Banana', 'Maca', 'Melao']
    legumes = ['Alface', 'Pepino', 'Cenoura']
    carnes = ['Coxao mole', 'Coxao duro', 'Patinho']

    objetos.add_element(frutas, 'frutas')
    objetos.add_element(legumes, 'legumes')
    objetos.add_element(carnes, 'carnes')

    return render_template('segundo_projeto.html', objetos=objetos), 200


__app__.run()
