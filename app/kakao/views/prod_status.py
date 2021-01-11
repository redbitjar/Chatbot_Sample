# 목표대비 실적 현황 정보 (생산계획대비) , 생산 종합 현황 정보	(생산지시대비) 관련 blueprints 소스 코드

import requests
import json
from flask import Blueprint, request, jsonify, render_template, current_app as app


bp = Blueprint('kbot_prod_status', __name__, url_prefix='/prod')


@bp.route("kBotProdStatus", methods=['GET', 'POST'])
def kbot_prod_status():
    # return 'test'
    print(request.get_json())

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
               {
                    'simpleText': {
                        'text': "생산현황 보여2줘"
                    }
                }
            ],
            "quickReplies":[
                {                    
                    "label": "목표대비 실적현황",
                    "action": "message",
                    "messageText": "목표실적"                    
                },
                {                    
                    "label": "작업지시대비 실적현황",
                    "action": "message",
                    "messageText": "작업지시실적"                    
                }
            ]
        }
    }
    return jsonify(responseBody)

@bp.route("kBotPlanProdStatus", methods=['GET', 'POST'])
def kbot_plan_prod_status():
    # return 'test'
    print(request.get_json())

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
               {
                    'simpleText': {
                        'text': "생산현황 보여줘"
                    }
                }
            ],
            "quickReplies":[
                {                    
                    "label": "목표대비 실적현황",
                    "action": "message",
                    "messageText": "목표실적"                    
                },
                {                    
                    "label": "작업지시대비 실적현황",
                    "action": "message",
                    "messageText": "작업지시실적"                    
                }
            ]
        }
    }
    return jsonify(responseBody)

@bp.route("kBotOrderProdStatus", methods=['GET', 'POST'])
def kbot_order_prod_status():
    # return 'test'
    print(request.get_json())

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
               {
                    'simpleText': {
                        'text': "생산현황 보여줘"
                    }
                }
            ],
            "quickReplies":[
                {                    
                    "label": "목표대비 실적현황",
                    "action": "message",
                    "messageText": "목표실적"                    
                },
                {                    
                    "label": "작업지시대비 실적현황",
                    "action": "message",
                    "messageText": "작업지시실적"                    
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