# coding: utf-8
import dataset
from hashlib import sha512


class Database:
    def addUser(self, data):
        with dataset.connect('sqlite:///apijogos.sqlite.db') as db:
            hasher = sha512()
            hasher.update(data['password'].encode('utf-8'))
            data['password'] = hasher.hexdigest()
            return db['users'].insert(data)

    def getUser(self, username, password):
        with dataset.connect('sqlite:///apijogos.sqlite.db') as db:
            hasher = sha512()
            hasher.update(password.encode('utf-8'))
            password = hasher.hexdigest()
            return db['users'].find_one(username=username, password=password)

    def listGames(self):
        with dataset.connect('sqlite:///apijogos.sqlite.db') as db:
            games = db['games'].all()

            if db['games'].count() > 0:
                games = [data for data in games]

                return games

            return False

    def saveGame(self, data):
        with dataset.connect('sqlite:///apijogos.sqlite.db') as db:
            data['price'] = float(data['price'])
            return db['games'].insert(data)

    def getGame(self, id):
        with dataset.connect('sqlite:///apijogos.sqlite.db') as db:
            game = db['games'].find_one(id=id)

        return game or False

    def updateGame(self, id, data):
        with dataset.connect('sqlite:///apijogos.sqlite.db') as db:
            data['id'] = id
            data['price'] = float(data['price'])
            db['games'].update(data, ['id'])

        return self.getGame(id=id)

    def deleteGame(self, id):
        with dataset.connect('sqlite:///apijogos.sqlite.db') as db:
            return db['games'].delete(id=id)
