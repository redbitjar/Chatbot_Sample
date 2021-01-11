# 목표대비 실적 현황 정보 (생산계획대비) , 생산 종합 현황 정보	(생산지시대비) 관련 blueprints 소스 코드

import requests
import json
from flask import Blueprint, request, jsonify, render_template, current_app as app


bp = Blueprint('kbot_prod_status', __name__, url_prefix='/')


@bp.route("kbotProdStatus", methods=['GET', 'POST'])
def kbot_prod_status():
    # return 'test'
    print(request.get_json())

    responseBody = {
        "version": "2.0",
        "template": {         
            'outputs': [
                {
                    'simpleText': {
                        'text': "보고 싶은 생산현황을 선택하세요"
                    }
                }
            ],
            "quickReplies":[
                {                    
                    "label": "목표대비실적현황",
                    "action": "message",
                    "messageText": "목표실적현황"                    
                },
                {                    
                    "label": "작업지시대비실적현황",
                    "action": "message",
                    "messageText": "작업지시실적현황"                    
                }
            ]
        }
    }
    return jsonify(responseBody)


@bp.route("kbotPlanProdStatus", methods=['GET', 'POST'])
def kbot_plan_prod_status():
    # return 'test'
    print(request.get_json())

    responseBody = {
        "version": "2.0",
        "template": {    
            "outputs": [
                {
                    'simpleText': {
                        'text': "굿"
                    }
                },
                {
                    "carousel": {
                    "type": "basicCard",
                    "items": [
                        {
                        "title": "보물상자",
                        "description": "보물상자 안에는 뭐가 있을까",
                        "thumbnail": {
                            "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                        },
                        "buttons": [
                            {
                            "action": "message",
                            "label": "열어보기",
                            "messageText": "짜잔! 우리가 찾던 보물입니다"
                            },
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                            }
                        ]
                        },
                        {
                        "title": "보물상자2",
                        "description": "보물상자2 안에는 뭐가 있을까",
                        "thumbnail": {
                            "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                        },
                        "buttons": [
                            {
                            "action": "message",
                            "label": "열어보기",
                            "messageText": "짜잔! 우리가 찾던 보물입니다"
                            },
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                            }
                        ]
                        },
                        {
                        "title": "보물상자3",
                        "description": "보물상자3 안에는 뭐가 있을까",
                        "thumbnail": {
                            "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                        },
                        "buttons": [
                            {
                            "action": "message",
                            "label": "열어보기",
                            "messageText": "짜잔! 우리가 찾던 보물입니다"
                            },
                            {
                            "action":  "webLink",
                            "label": "구경하기",
                            "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                            }
                        ]
                        }
                    ]
                    }
                }
            ],
        }
    }
    return jsonify(responseBody)

# @bp.route('/')
# @bp.route('/index')
# def index():
#     print(app.config['NAME'])
#     return "Hello, World!"