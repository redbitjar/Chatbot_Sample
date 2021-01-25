from app.kakao.components import SkillTemplate, SimpleText, QuickReply, Action, BasicCard, Carousel, Thumbnail

def make_def_plan_prod_sts(data : dict):
    print('make_def_plan_prod_sts')
    data_type_img = {
        "D" : "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
        "W" : "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
        "M" : "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
        "Q" : "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
        "Y" : "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
    }

    simpleText = SimpleText("목표대비 생산현황 입니다")
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

def make_def_order_prod_sts(data : dict):
    print('make_def_order_prod_sts')
    data_type_img = {
        "D" : "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
        "W" : "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
        "M" : "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
        "Q" : "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
        "Y" : "http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
    }

    simpleText = SimpleText("작업지시대비 생산현황 입니다")
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