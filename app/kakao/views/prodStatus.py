# 목표대비 실적 현황 정보 (생산계획대비) , 생산 종합 현황 정보	(생산지시대비) 관련 blueprints 소스 코드

import requests
import json
from flask import Blueprint, request, jsonify, render_template, current_app as app


bp = Blueprint('kBotProdStatus', __name__, url_prefix='/kBotProdStatus')


@bp.route("/", methods=['GET', 'POST'])
def kBotProdStatus():
    # return 'test'
    print(request.get_json())

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
               {
                    'simpleText': {
                        'text': "hello I'm Ryan"
                    }
                }
            ],
            "quickReplies":[
                {                    
                    "label": "라미코미 이리온",
                    "action": "message",
                    "messageText": "라미코미 이리온"                    
                }
            ]
        }
    }
    return jsonify(responseBody)

# @bp.route('/')
# @bp.route('/index')
# def index():
#     print(app.config['NAME'])
#     return "Hello, World!"