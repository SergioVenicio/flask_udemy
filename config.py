class __Config(object):
    DEBUG = False
    TEMPLATE_AUTO_RELOAD = False


class DevelopmentConfig(__Config):
    DEBUG = True
    TEMPLATE_AUTO_RELOAD = True


class ProductionConfig(__Config):
    pass
