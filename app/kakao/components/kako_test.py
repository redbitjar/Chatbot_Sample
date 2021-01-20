import json
# from components import button
from . import *

btn = Button("label", Action.WEBLINK)
btn.set_block_id("block id")
print(btn.to_string())


# from flask import jsonify

# k = KaKaoTemplate()

# # print(k.simpletextComponent("test"))

# d = k.simpletextComponent("test")
# # print(d["simpleText"])

# s =  json.dumps(k.simpletextComponent("test"))
# # print(s)


# ---------------------------------- componet test ------------------------ #
# simpleText
# simpleText = SimpleText("간단한 텍스트 ")
# print(simpleText.to_string())

# simpleImage
# simpleImage = SimpleImage("http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg", "보물상자입니다")
# print(simpleImage.to_string())

# basic = k.basicCardComponent('', '', '', '')
# print(basic)

# ---- thumbnail test
# thumbnail = Thumbnail("imageURl")
# link = Link()
# link.set_pc("pc").set_pc('mobile')
# st = thumbnail.set_link(link).set_fixed_ratio(True)
# # st = thumbnail.set_link("link").set_fixed_ratio(True).set_width(10).set_height(100)
# print(st.to_string())
# # print(json.dumps(st.to_string()))

# ---- btn test
# # btn = Button("label", Action.WEBLINK)
# # btn.set_block_id("block id")
# # print(btn.to_string())

# ---- CarouseHeader test
# carouselHeader = CarouselHeader("title", "description", thumbnail)
# print(carouselHeader.to_string())

# list item test
# listItem = ListItem('title')
# link = Link()
# link.set_pc("pc")
# listItem.set_link(link)
# print(listItem.to_string())

# ---- extra test
# extra = Extra("key", "value")
# extra.append("key2", "value2")
# extra.append("key", "value change")
# print(extra.to_string())

# ---- quickReplies test
# quickReplies = QuickReplies()
# quickReplies.set_action(Action.BLOCK)
# quickReplies.set_label()
# # extra = { "interval" : 'input_date', "matCode" : 'input_matCode'}
# extra = 'test'
# quickReplies.set_extra(extra)
# print(quickReplies.to_string())
# print(json.dumps( quickReplies.to_string()))


# ---- basicCard Test
# thumbnail = Thumbnail("http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg")
# basicCard = BasicCard(thumbnail)
# basicCard.set_title("보물상자")
# basicCard.set_description('보물상자 안에는 뭐가 있을까')
# btn1 = Button("열어보기", Action.MESSAGE)
# btn1.set_mesaage_text("짜잔! 우리가 찾던 보물입니다")
# # basicCard.set_button(btn1)

# btn2 = Button("열어보기2", Action.MESSAGE)
# btn2.set_mesaage_text("짜잔! 우리가 찾던 보물입니다2")
# # basicCard.set_button(btn2)
# btns = [btn1, btn2]
# basicCard.set_buttons(btns)
# print(basicCard.to_string())


# ---- listCard Test
# link = Link()
# link.set_web("https://namu.wiki/w/%EB%9D%BC%EC%9D%B4%EC%96%B8(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)")

# header = ListItem("카카오 i 디벨로퍼스를 소개합니다")

# item1 = ListItem("Kakao i Developers")
# item1.set_description("새로운 AI의 내일과 일상의 변화")
# item1.set_image_url("http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg")
# item1.set_link(link)

# item2 = ListItem("Kakao i Developers")
# item2.set_description("새로운 AI의 내일과 일상의 변화")
# item2.set_image_url("http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg")
# item2.set_link(link)
# btn1 = Button("열어보기", Action.MESSAGE)
# btn1.set_mesaage_text("짜잔! 우리가 찾던 보물입니다")
# # basicCard.set_button(btn1)

# btn2 = Button("열어보기2", Action.MESSAGE)
# btn2.set_mesaage_text("짜잔! 우리가 찾던 보물입니다2")
# # basicCard.set_button(btn2)
# btns = [btn1, btn2]

# listCard =  ListCard(header, [item1, item2])
# listCard.set_buttons(btns)
# print(listCard.to_string())


# if not len(buttons) == 0:
#     print('cnt')
# else:
#     print('not cnt')

# ---- simpe_text Test
# skillTemplate = SkillTemplate()
# simpleText = SimpleText("SimpleText Test")
# skillTemplate.set_add_component(simpleText)
# print(skillTemplate.to_string())

# ---- simpe_image Test
# skillTemplate = SkillTemplate()
# simpleImage = SimpleImage("http://k.kakaocdn.net/dn/83BvP/bl20duRC1Q1/lj3JUcmrzC53YIjNDkqbWK/i_6piz1p.jpg",
# "보물상자입니다")
# skillTemplate.set_add_component(simpleImage)
# print(skillTemplate.to_string())

# ---- basicCard Test
skillTemplate = SkillTemplate()
thumbnail = Thumbnail("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM")
basicCard = BasicCard(thumbnail)
basicCard.set_title("보물상자").set_description("보물상자 안에는 뭐가 있을까")
button1 = Button("열어보기", Action.MESSAGE)
button1.set_mesaage_text("짜잔! 우리가 찾던 보물입니다")
basicCard.set_button(button1)
button2 = Button("구경하기", Action.WEBLINK)
button2.set_web_link_url("https://e.kakao.com/t/hello-ryan")
basicCard.set_button(button2)

skillTemplate.set_add_component(basicCard)
print(skillTemplate.to_string())