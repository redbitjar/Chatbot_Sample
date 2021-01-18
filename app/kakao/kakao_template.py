class KaKaoTemplate:
    def __init__(self):
        self.__version = "2.0"

    def simpletextComponent(self, text):
        return {
            "simpleText": {"text": text}
        }

    def simpleImageComponent(self, imageUrl, altText):
        return{
            "simpleImage": {"imageUrl": imageUrl, "altText": altText}
        }

    def basicCardComponent(self, title, description, thumbnail, buttons):
        return{
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

    #사용자에게 응답 스킬 전송
    def send_response(self, bot_resp):
        reponseBody = {
            "version": self.version,
            "template":{
                "outputs": []
            }
        }

        #이미지 답변이 텍스 답변보다 먼저 출력됨
        # if bot_resp['AnswerImageUrl'] is not None:
        #     reponseBody['template']['outputs'].append(
        #         self.simpleImageComponent(bot_resp['Answer'], '')
        #     )
        
        # # 텍스 답변이 있는 경우
        # if bot_resp['Answer'] is not None:
        #     reponseBody['template']['outputs'].append(
        #         self.simpletextComponent(bot_resp['Answer'])
        #     )
        return  reponseBody
    
