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

class Data:
  def to_string(self):
    return default_skill_data