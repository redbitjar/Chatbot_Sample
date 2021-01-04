from flask import Flask


def create_app():
    app = Flask(__name__)
    # app.config.from_pyfile('../config.py')
    # app.config.from_object('config.Config')
    app.config.from_object('config.ProdConfig')
    print(app.config)
    print('-----------------')

    from .kakaoBot.views import hello as kakaoHello
    from .kakaoBot.views import prodStatus as kakaoProdStatus
    app.register_blueprint(kakaoHello.bp)
    app.register_blueprint(kakaoProdStatus.bp)

    # @app.route('/')
    # def hello_app():
        
    #     # print(app.config['NAME'])
    #     print(app.config['FLASK_ENV'])
    #     print('app.config.NAME')
    #     return 'Hello, app'
    
    return app

 