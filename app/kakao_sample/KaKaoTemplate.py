class KaKaoTemplate:
    def __init__(self):
        self.version = "2.0"

    def simpletextComponent(self, text):
        return {
            "simpleText": {"text": text}
        }

    def simpleImageComponent(self, imageUrl, altText):
        return{
            "simpleImage": {"imageUrl": imageUrl, "altText": altText}
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
        if bot_resp['AnswerImageUrl'] is not None:
            reponseBody['template']['outputs'].append(
                self.simpleImageComponent(bot_resp['Answer'], '')
            )
        
        # 텍스 답변이 있는 경우
        if bot_resp['Answer'] is not None:
            reponseBody['template']['outputs'].append(
                self.simpletextComponent(bot_resp['Answer'])
            )
        return  reponseBody
