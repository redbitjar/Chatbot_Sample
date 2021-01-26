from flask import Blueprint, request, jsonify, render_template, current_app as app
import log
import logging

bp = Blueprint('index', __name__, url_prefix='/')



@bp.route("", methods=['GET', 'POST'])
def index_sample():
    logging.info("index test")
    # a = 4 / 0
    b = {}
    # name = b['name']
    print('---------request------', str(request))
    log.log(request, "index test")
    f = open("나없는파일", 'r')
    # req = request.get_json()
    # print(app.config)
    # print('ab')
    
    return 'index'
