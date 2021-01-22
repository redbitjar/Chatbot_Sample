import json
# from sample import get_default_skill_data
import app.kakao.json_data.sample as s
from app.kakao.components import SkillTemplate, SimpleText, QuickReply, Action, BasicCard, Carousel, Thumbnail
# import sample as s

# print(s.res_def_mes_plan_sts)
def make_simple_text(data : dict):

    # print('make_simple_text  call')
    # print(data["data"])
    simpleText = SimpleText(data["desc"])
    skillTemplate = SkillTemplate()
    skillTemplate.set_add_output(simpleText)

    return skillTemplate.to_string()

def make_def_mes_plan_sts(data : dict):
    data_type_img = {
        "D" : "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
        "W" : "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
        "M" : "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
        "Q" : "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
        "Y" : "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
    }

    simpleText = SimpleText("목표대비 생상현황 입니다")
    basicCards = []

    for key, value in data_type_img.items():
        thumbnail = Thumbnail(value)
        basicCard = BasicCard(thumbnail)
        basicCard.set_title(data[key]['title'])
        basicCard.set_description(data[key]['desc'])
        basicCards.append(basicCard)

    carousel = Carousel(basicCards)   
    
    skillTemplate = SkillTemplate()
    skillTemplate.set_add_output(simpleText)
    skillTemplate.set_add_output(carousel)
    
    return skillTemplate.to_string()

def mes_data_parser(data : str, func : callable = None):

    dic = json.loads(data)
    res_type = dic['responseType']
    data = dic['data']
    
    # if res_type == "default":
    #     dic = func(data)
    # elif res_type == "simpleText":
    #     dic = make_simple_text(data)

    inner = test(data, func)
    dic = inner
        
    print(dic)
    return dic    

def test(data, func):

    def inner():
        return {
            "default" : 'default',
            "simpleText" : make_simple_text(data),
            "kakao" : data
            # "default" : func(data),
            # "simpleText" : make_simple_text(data),
            # "kakao" : data
        }
    t = inner()
    print(t["default"])
    return inner



    

# mes_data_parser(s.res_simple_text_mes)
mes_data_parser(s.res_def_mes_plan_sts, make_def_mes_plan_sts)

# default_skill_data =  get_default_skill_data()
# d_skill_data = json.loads(default_skill_data)
# # print(default_skill_data)
# print(d_skill_data['intent'])

# d = Data()
# print(d.to_string())




