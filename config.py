# TESTING = True
# FLASK_ENV = 'development2'

import os


class Config(object):
    BASE_DIR = os.path.dirname(__file__)
    NAME = 'HH.K'
    # NEXPLANT_MES_URL = 'https://odc.miracom.co.kr'
    NEXPLANT_MES_URL = 'https://mes-dev.miracom.co.kr'
    NEXPLANT_MES_VERSION_URL = NEXPLANT_MES_URL + '/v1'
    NEXPLANT_MES_PATH_OAUTH = NEXPLANT_MES_URL + '/iam/oauth/token?grant_type=password&username=tsung.lim&password=manager'
    NEXPLANT_MES_AUTHORIZATION = 'Basic b2F1dGgyX29pY2xpZW50OjBkMWFhNWE2LWM5NWUtNGVkMS05Y2E0LWNhOTQ4MjUwNzM3OQ=='

class ProdConfig(Config):
    DEBUG = False
    FLASK_ENV = 'production'
    NAME = 'HH.K.PRD'
    JSON_AS_ASCII = False

class DevConfig(Config):    
    DEBUG = True
    FLASK_ENV = 'development'
    JSON_AS_ASCII = False