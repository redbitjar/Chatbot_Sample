import time
import requests
from flask import request, jsonify, current_app as app

nexPlantMesAuthKey = ""

def nexplant_mes_request(params={}):
    logStr = ""
    start = time.time()    
    # writeJson(req, "nexMes.json")  
    url  = params['url']
    data = params['data']
    method = params['method']
    #print("url : " + url )
    logStr = "\nurl : " + url + "\n"
    res = nexplant_mes_api_request(url, data, method)    
    
    if (res.status_code ==  401) :      
        nexplant_mes_api_auth()        
        res = nexplant_mes_api_request(url, data, method)       
        logStr += "re Authorization~!\n"       
    
    logStr += "API time : " + str(time.time()-start)
    app.logger.info(logStr)
    return res.json()


def nexplant_mes_api_request(url="", data = {}, method="GET"):        
    if (nexPlantMesAuthKey ==""): 
        nexplant_mes_api_auth()
    
    headers = {'Content-Type': 'application/json; charset=utf-8',
               'Authorization' :'Bearer ' + nexPlantMesAuthKey }
    
    if method == "GET":
        if data != {}:
            url = url + '?'
        for d in data:
            if type(data[d]) != str:
                continue
            url = url + d + '=' + data[d] + '&'        
        return requests.get(url, headers=headers)
    else:
        return requests.post(url, headers=headers, data=data)

def nexplant_mes_api_auth():
    # 응답서버 -> MES 내부서버 인증 견본 POST    
    # 챗봇공장(00000) 인증키
    url = app.config['NEXPLANT_MES_PATH_OAUTH']
    # url = "https://odc.miracom.co.kr/iam/oauth/token?grant_type=password&username=tsung.lim&password=manager"
    # 관리자(admin) 인증키
    #url = "https://odc.miracom.co.kr/iam/oauth/token?grant_type=password&username=admin&password=manager"
    headers = {'Authorization': app.config['NEXPLANT_MES_AUTHORIZATION']}        
    # headers = {'Authorization': 'Basic b2F1dGgyX29pY2xpZW50OjBkMWFhNWE2LWM5NWUtNGVkMS05Y2E0LWNhOTQ4MjUwNzM3OQ=='}        
    res = requests.post(url, headers = headers)
    res = res.json()    
    global nexPlantMesAuthKey 
    nexPlantMesAuthKey = res["access_token"]