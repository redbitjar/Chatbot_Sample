# 카카오 빌더 template 조회 예제 코드

import requests
import json
from flask import Blueprint, request, jsonify, render_template, current_app as app


bp = Blueprint('hello_kbot', __name__, url_prefix='/hello_kbot')


@bp.route('/')
def index():
    print(app.config['NAME'])
    return "Hello, World!"

@bp.route("/simpleText", methods=['GET', 'POST'])
def hello_simpleText():
    # return 'test'
    print(request.get_json())

    responseBody = {
        'version': "2.0",
        'template': {
            'outputs': [
                {
                    'simpleText': {
                        'text': "hello I'm Ryan"
                    }
                }
            ]
        }
    }
    return jsonify(responseBody)


    
@bp.route("/simpleImage", methods=['GET', 'POST'])
def hello_simpleImage():
    # return 'test'
    print(request.get_json())

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
                        "altText": "보물상자입니다"
                    }
                }
            ]
        }
    }
    return jsonify(responseBody)


@bp.route("/basicCard", methods=['GET', 'POST'])
def hello_basicCard():
    # return 'test'
    print(request.get_json())

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": "보물상자",
                        "description": "보물상자 안에는 뭐가 있을까",
                        "thumbnail": {
                            "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                        },
                        "profile": {
                            "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
                            "nickname": "보물상자"
                        },
                        "social": {
                            "like": 1238,
                            "comment": 8,
                            "share": 780
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
                }
            ]
        }
    }
    return jsonify(responseBody)


@bp.route("/listCard", methods=['GET', 'POST'])
def hello_listCard():
    # return 'test'
    print(request.get_json())

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "카카오 i 디벨로퍼스를 소개합니다"
                        },
                        "items": [
                            {
                            "title": "Kakao i Developers",
                            "description": "새로운 AI의 내일과 일상의 변화",
                            "imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                            "link": {
                                "web": "https://namu.wiki/w/%EB%9D%BC%EC%9D%B4%EC%96%B8(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)"
                            }
                            },
                            {
                            "title": "Kakao i Open Builder",
                            "description": "카카오톡 채널 챗봇 만들기",
                            "imageUrl": "http://k.kakaocdn.net/dn/N4Epz/btqqHCfF5II/a3kMRckYml1NLPEo7nqTmK/1x1.jpg",
                            "link": {
                                "web": "https://namu.wiki/w/%EB%AC%B4%EC%A7%80(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)"
                            }
                            },
                            {
                            "title": "Kakao i Voice Service",
                            "description": "보이스봇 / KVS 제휴 신청하기",
                            "imageUrl": "http://k.kakaocdn.net/dn/bE8AKO/btqqFHI6vDQ/mWZGNbLIOlTv3oVF1gzXKK/1x1.jpg",
                            "link": {
                                "web": "https://namu.wiki/w/%EC%96%B4%ED%94%BC%EC%B9%98"
                            }
                            }
                        ],
                        "buttons": [
                            {
                            "label": "구경가기",
                            "action": "webLink",
                            "webLinkUrl": "https://namu.wiki/w/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88"
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(responseBody)


@bp.route("/carousel", methods=['GET', 'POST'])
def hello_carousel():
    # return 'test'
    print(request.get_json())

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
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