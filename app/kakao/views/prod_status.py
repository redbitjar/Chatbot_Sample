# 목표대비 실적 현황 정보 (생산계획대비) , 생산 종합 현황 정보	(생산지시대비) 관련 blueprints 소스 코드
from typing import List
import requests
import json
from flask import Blueprint, request, jsonify, render_template, current_app as app
from app.utils.mes_api import nexplant_mes_request
from app.kakao.components import SkillTemplate, SimpleText, QuickReply, Action, BasicCard, Carousel, Thumbnail

bp = Blueprint('kbot_prod_status', __name__, url_prefix='/prod')

@bp.route("kBotProdStatus", methods=['GET', 'POST'])
def kbot_prod_status():
    # return 'test'
    req = request.get_json()
    # print(req)

    params = {
        'pageSize': '20',
        'pageNumber': '0',
        'fromData':'20201201',
        'toDate':'20201218',
        'ordStatus': 'PROCESS,WAIT,CLOSE,COMPLETE'
    }

    data = {
            # "url":'https://odc.miracom.co.kr/v1/wip/orders',
            "url":app.config['NEXPLANT_MES_VERSION_URL']+'/wip/orders',
            "data":params,
            "method":'GET'
    } 

    response = nexplant_mes_request(data)
    # print('------------------ mes data-------------')
    # print(response)
    # print('------------------ mes data end -------------')

    simpleText = SimpleText('보고 싶은 생산현황을 선택하세요')
    quickReply1 = QuickReply()
    quickReply1.set_label('목표대비 실적현황').set_action(Action.MESSAGE).set_message_text('목표실적')
    quickReply2 = QuickReply()
    quickReply2.set_label('작업지시대비 실적현황').set_action(Action.MESSAGE).set_message_text('작업지시실적')
    
    skillTemplate = SkillTemplate()
    skillTemplate.set_add_output(simpleText)
    skillTemplate.set_add_quick_reply(quickReply1)
    skillTemplate.set_add_quick_reply(quickReply2)
    responseBody = skillTemplate.to_string()
    
    return jsonify(responseBody)

@bp.route("kBotPlanProdStatus", methods=['GET', 'POST'])
def kbot_plan_prod_status():
    '''
    목표(계획)대비 실적현황
    '''
    # return 'test'
    req = request.get_json()
    # print(req)

    params = {
        'pageSize': '20',
        'pageNumber': '0',
        'fromData':'20201201',
        'toDate':'20201218',
        'ordStatus': 'PROCESS,WAIT,CLOSE,COMPLETE'
    }

    data = {
            # "url":'https://odc.miracom.co.kr/v1/wip/orders',
            "url":app.config['NEXPLANT_MES_VERSION_URL']+'/wip/orders',
            "data":params,
            "method":'GET'
    } 

    response = nexplant_mes_request(data)

    simpleText = SimpleText("목표대비 생상현황 입니다")


    thumbnail1 = Thumbnail("http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg")
    basicCard1 = BasicCard(thumbnail1)
    basicCard1.set_title('12월 30일 생산 현황')
    basicCard1.set_description('계획: 10, 실적: 5, 달성률: 0.5')

    thumbnail2 = Thumbnail("http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg")
    basicCard2 = BasicCard(thumbnail2)
    basicCard2.set_title('12월 5주 생산 현황')
    basicCard2.set_description('계획: 10, 실적: 5, 달성률: 0.5')

    thumbnail3 = Thumbnail("http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg")
    basicCard3 = BasicCard(thumbnail3)
    basicCard3.set_title('12월 생산 현황')
    basicCard3.set_description('계획: 10, 실적: 5, 달성률: 0.5')

    thumbnail4 = Thumbnail("http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg")
    basicCard4 = BasicCard(thumbnail4)
    basicCard4.set_title('4분기 생산 현황')
    basicCard4.set_description('계획: 10, 실적: 5, 달성률: 0.5')

    thumbnail5 = Thumbnail("http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg")
    basicCard5 = BasicCard(thumbnail5)
    basicCard5.set_title('2020년 생산 현황')
    basicCard5.set_description('계획: 10, 실적: 5, 달성률: 0.5')
    
    basicCards = [basicCard1, basicCard2, basicCard3, basicCard4, basicCard5]
    carousel = Carousel(basicCards)
    
    
    skillTemplate = SkillTemplate()
    skillTemplate.set_add_output(simpleText)
    skillTemplate.set_add_output(carousel)
    # skillTemplate.set_add_quick_reply(quickReply1)
    # skillTemplate.set_add_quick_reply(quickReply2)
    responseBody = skillTemplate.to_string()
    # responseBody = {
    #     "version": "2.0",
    #     "template": {
    #         "outputs": [
    #            {
    #                 'simpleText': {
    #                     'text': "생산현황 보여줘"
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
