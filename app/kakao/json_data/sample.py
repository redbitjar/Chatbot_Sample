default_skill_data = '''{
    "intent": {
      "id": "wf1xgqdy4a0jc7bj7gbq1fzx",
      "name": "블록 이름"
    },
    "userRequest": {
      "timezone": "Asia/Seoul",
      "params": {
        "ignoreMe": "true"
      },
      "block": {
        "id": "wf1xgqdy4a0jc7bj7gbq1fzx",
        "name": "블록 이름"
      },
      "utterance": "발화 내용",
      "lang": null,
      "user": {
        "id": "305542",
        "type": "accountId",
        "properties": {}
      }
    },
    "bot": {
      "id": "5fd1a86bb6158466bd57308e",
      "name": "봇 이름"
    },
    "action": {
      "name": "8ium42d8br",
      "clientExtra": null,
      "params": {},
      "id": "tizpbi4c2ubljw1kf19m0ik5",
      "detailParams": {}
    }
  }'''


def get_default_skill_data():
    return default_skill_data




# 화면 형태
# [캐로셀(베이직카드)]
# API url 예시
# /v1/chatvot/plnSts?currentDate = 20210114
# 응답 샘플
res_def_mes_plan_sts = '''{
    "responseType": "default",
    "data": {
        "D": {
            "title": "1월 19일 생산현황",
            "desc": "계획:100 실적:10 달성률:0.1" 
        },
        "W": {
            "title": "1월 3주 생산현황",
            "desc": "계획:100 실적:10 달성률:0.1" 
        },
        "M": {
            "title": "1월 생산현황",
            "desc": "계획:100 실적:10 달성률:0.1" 
        },
        "Q": {
            "title": "1분기 생산현황",
            "desc": "계획:100 실적:10 달성률:0.1" 
        },
        "Y": {
            "title": "2021년 생산현황",
            "desc": "계획:100 실적:10 달성률:0.1" 
        }

    }
}
'''

# - 작업지시대비 실적 현황 조회
# 참고화면 : 생산관리 > 생산종합현황 > 생산종합현황
# currentDate를 전달받아 작업지시 대비 실적 현황을 요청일 기준으로 (일, 주, 월, 분기, 년) 결과
# 화면 형태
# [캐로셀(베이직카드)]
# API url 예시
# /v1/chatvot/plnSum?currentDate=20210114
# 응답 샘플
res_def_mes_pln_sum = '''{
    "responseType": "default",
    "data": {
        "D": {
            "title": "1월 19일 생산현황",
            "desc": "계획:100 실적:10 달성률:0.1" 
        },
        "W": {
            "title": "1월 3주 생산현황",
            "desc": "계획:100 실적:10 달성률:0.1" 
        },
        "M": {
            "title": "1월 생산현황",
            "desc": "계획:100 실적:10 달성률:0.1" 
        },
        "Q": {
            "title": "1분기 생산현황",
            "desc": "계획:100 실적:10 달성률:0.1" 
        },
        "Y": {
            "title": "2021년 생산현황",
            "desc": "계획:100 실적:10 달성률:0.1" 
        }
    }
}
'''

# MES공통모듈에서 기본적으로 제공하는 화면 외 커스텀이 필요할때
# 1. SimpleText : 텍스트로만 이루어진 메세지 전송 (최대 1000자)
# 화면 형태
# [심플텍스트]
# 응답형태
res_simple_text_mes = '''{
    "responseType": "simpleText",
    "data": {
        "desc": "창고목록\\n\\n자재창고\\n제품창고"
    }
}
'''

# 2. kakao 응답구조 전체를 MES에서 전달
# 화면 형태 : 카카오에서 제공하는 모든 화면형태
# [심플텍스트, 심플이미지, 리스트카드, 베이직카드, 캐로셀]
# 참고 url : https://i.kakao.com/docs/skill-response-format#
# 응답형태)
res_kakao_text_mes = '''
{
    "responseType": "kakao",
    "data": {
        "version": "2.0",
        "template": {
            "outputs": [{
                "basicCard": {
                    "title": "보물상자",
                    "description": "보물상자 안에는 뭐가 있을까",
                    "thumbnail": {
                        "imageUrl": "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg"
                    },
                    "buttons": [{
                        "action": "message",
                        "label": "열어보기",
                        "messageText": "짜잔! 우리가 찾던 보물입니다"
                    },
                    {
                        "action": "webLink",
                        "label": "구경하기",
                        "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                    }]
                }
            }]
        }
    }
}
'''
