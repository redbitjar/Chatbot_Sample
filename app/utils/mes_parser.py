import json
from app.kakao.components import SkillTemplate, SimpleText

def make_simple_text(data : dict):

    # print('make_simple_text  call')
    # print(data["data"])
    simpleText = SimpleText(data["desc"])
    skillTemplate = SkillTemplate()
    skillTemplate.set_add_output(simpleText)

    return skillTemplate.to_string()


def mes_data_parser(data : str, func : callable = None):
    print('mes_data_parser')

    dic = json.loads(data)
    res_type = dic['responseType']
    data = dic['data']
    
    # if res_type == "default":
    #     dic = func(data)
    # elif res_type == "simpleText":
    #     dic = make_simple_text(data)

    mes_type_func =  {
        "default" : func,
        "simpleText" : make_simple_text,
        "kakao" : lambda d : d
    }

    ret = mes_type_func[res_type](data)
    return ret