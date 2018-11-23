#!/usr/bin/python
# -*- coding: utf-8 -*-

import dataset
from flask import Flask, render_template, request, redirect

__app__ = Flask(__name__)
__app__.debug = True
__db__ = dataset.connect('sqlite:///datasabe.sqlite')
__db__['notes']


def get_notes(id=None):
    if id is None:
        return __db__['notes'].all()
    return __db__['notes'].find_one(id=id)


@__app__.route('/')
def main():
    notes = get_notes()

    return render_template('index.html', notes=notes), 200


@__app__.route('/note/<id>')
def note(id):
    note = get_notes(id=id)

    return render_template('note.html', note=note), 200


@__app__.route('/save_note', methods=['GET', 'POST'])
def save_note():
    table = __db__['notes']
    title = request.form.get('title')
    description = request.form.get('description')

    if request.method == 'POST' and description:
        exists = __db__['notes'].find_one(
            description=description, title=title
        )

        if exists is None:
            table.insert(dict(description=description, title=title))

    return redirect('')


@__app__.route('/edit_note/<id>', methods=['GET', 'POST'])
def edit_note(id):
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        __db__['notes'].update(
            dict(id=id, description=description, title=title),
            ['id']
        )

        return redirect('')

    note = get_notes(id=id)

    return render_template('note_edit.html', note=note)


@__app__.route('/delete_note/<id>')
def delete_note(id):
    __db__['notes'].delete(id=id)

    return redirect('')


__app__.run()
