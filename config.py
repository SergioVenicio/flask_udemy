import random


class _Config(object):
    @staticmethod
    def secret(length):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyz'
        allowed_chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

        return ''.join(random.choice(allowed_chars) for i in range(length))

    DEBUG = False
    TEMPLATE_AUTO_RELOAD = False


class DevelopmentConfig(_Config):
    DEBUG = True
    TEMPLATE_AUTO_RELOAD = True
    SECRET_KEY = _Config.secret(50)


class ProductionConfig(_Config):
    SECRET_KEY = _Config.secret(150)
