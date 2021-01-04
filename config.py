# TESTING = True
# FLASK_ENV = 'development2'

import os

class Config(object):
    BASE_DIR = os.path.dirname(__file__)
    NAME = 'HH.K'

class ProdConfig(Config):
    DEBUG = False
    FLASK_ENV = 'production'
    NAME = 'HH.K.PRD'

class DevConfig(Config):    
    DEBUG = True
    FLASK_ENV = 'development'