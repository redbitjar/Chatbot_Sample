from flask import Flask
import logging
import log


def create_app():

    # logging.basicConfig(filename = "logs/project.log", level = logging.DEBUG)

    app = Flask(__name__)
    # app.config.from_pyfile('../config.py')
    # app.config.from_object('config.Config')
    # app.config.from_object('config.DevConfig')
    # app.config['JSON_AS_ASCII'] = False
    app.config.from_object('config.ProdConfig')
    # print(app.config)
    # print('-----------------')

    from .kakao.views import prod_status as kakao_prod_status
    app.register_blueprint(kakao_prod_status.bp)

    #-------------- test --------------
    from example import router
    app.register_blueprint(router.bp)
 

    # from .kakao_sample.views import helloKbot
    # app.register_blueprint(helloKbot.bp)

    # @app.route('/')
    # def hello_app():
        
    #     # print(app.config['NAME'])
    #     print(app.config['FLASK_ENV'])
    #     print('app.config.NAME')
    #     return 'Hello, app'
    
    return app

 