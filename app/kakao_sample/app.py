from flask import Flask, request, jsonify, abort
import sorcket
import json
# 챗봇 엔진 서버 접속 정보
host = "127.0.0.1"  # 챗봇 엔진 서벗 ip 주소
port = 5050  # 챗봇 엔진 서버 통신 포트

# Flask 애플리케이션
app = Flask(__name__)

# 챗봇 엔진 서버 통신


def get_answer_from_engine(bottype, query):
    mySocket = socket.socket()
    mySocket.connect((host, port))

    # 챗봇 엔진 질의 요청
    json_data = {
        'Query': query,
        'BotyType': bottype
    }

    message = json.dumps(json_data)
    mySocket.send(message.encode())

    # 챗봇 엔진 답변 출력
    data = mySocket.recv(2048).decode()
    ret_data = json.loads(data)

    # 챗봇 엔진 서버 연결 소켓 닫기
    mySocket.close()

    return ret_data

# 챗봇 엔진 query 전송 api
@app.route('/query/<bot_typ>', method=['POST'])
def query(bot_type):
    body = request.get_json()

    try:
        if bot_type == 'TEST':
            # 챗봇 API 테스트
            ret = get_answer_from_engine(bottype=bot_type, query=body['query'])
            return jsonify(ret)
        else bot_type == "KAKAO":
            # 카카오톡 스킬 처리
            body = request.get_json()
            utterance = body['userRequest']['utterance']
            ret = get_answer_from_engine(bottype=bot_type, query=utterance)

            from kakaoTemplate import KaKaoTemplate
            skilTemplate = KaKaoTemplate()
            return skilTemplate.send_response(ret)
