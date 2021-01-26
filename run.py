from app import create_app

# 실행 방법 py.exe run.py
# debug=truen 저장 시 자동으로 갱신 됨
#create_app().run(host='0.0.0.0', port=80, debug=True)
create_app().run(host='0.0.0.0')
