# 목표대비 실적 현황 정보 (생산계획대비) , 생산 종합 현황 정보	(생산지시대비) 관련 blueprints 소스 코드
import requests
import json
import time
from flask import Blueprint, request, jsonify, render_template, current_app as app
from app.utils.mes_api import nexplant_mes_request

bp = Blueprint('kbot_prod_status', __name__, url_prefix='/prod')

@bp.route("kBotProdStatus", methods=['GET', 'POST'])
def kbot_prod_status():
    # return 'test'
    req = request.get_json()
    print(req)

    params = {
        'pageSize': '20',
        'pageNumber': '0',
        'fromData':'20201201',
        'toDate':'20201218',
        'ordStatus': 'PROCESS,WAIT,CLOSE,COMPLETE'
    }

    data = {
            "url":'https://odc.miracom.co.kr/v1/wip/orders',
            "data":params,
            "method":'GET'
    } 

    response = nexplant_mes_request(data)
    data = json.loads(response.text)
    print('------------------ mes data-------------')
    print(data)
    print('------------------ mes data end -------------')

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                 "simpleImage": {
                        "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
                        "altText": "보물상자입니다"
                    }
                },
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

    # responseBody = {
    #     "version": "2.0",
    #     "template": {
    #         "outputs": [
    #            {
    #                 'simpleText': {
    #                     'text': "생산현황 보여2줘"
    #                 }
    #             }
    #         ],
    #         "quickReplies":[
    #             {                    
    #                 "label": "목표대비 실적현황",
    #                 "action": "message",
    #                 "messageText": "목표실적"                    
    #             },
    #             {                    
    #                 "label": "작업지시대비 실적현황",
    #                 "action": "message",
    #                 "messageText": "작업지시실적"                    
    #             }
    #         ]
    #     }
    # }
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
