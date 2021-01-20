from typing import List
from .thumbnail import Thumbnail
from .button import Button
from .component_base import OutputComponent

Tbuttons = List[Button]
class BasicCard(OutputComponent):

    '''
    title 카드의 제목입니다. (최대 2줄)
    description 카드에 대한 상세 설명입니다 (최대 230자)
    buttons 카드의 버튼들을 포함합니다. (최대 3개)
    '''
    def __init__(self, thumbnail : Thumbnail):
        self.__thumbnail = thumbnail.to_string()
        self.__title = ''
        self.__description = ''
        self.__buttons = []

    def set_title(self, title : str) -> 'BasicCard': 
        self.__title = title
        return self

    def set_description(self, description : str):
        self.__description = description
        return self

    def set_button(self, button : Button) -> 'BasicCard': 
        self.__buttons.append(button)
        return self

    
    def set_buttons(self, buttons : Tbuttons) -> 'BasicCard': 
        self.__buttons = buttons
        return self

    def to_string(self) -> str:
        type = "basicCard"
        fields = {
            type: {
                self.__to_string()
            }
        }
        # if self.__title:
        #     fields[type]["title"] = self.__title
        # if self.__description:
        #     fields[type]["description"] = self.__description
        # if not len(self.__buttons) == 0:
        #     fields[type]["buttons"] = []
        # for btn in self.__buttons:
        #     fields[type]["buttons"].append(btn.to_string())
        return fields

    def to_string_notype(self) -> str:
        fields = {
            self.__to_string()
            # "thumbnail": self.__thumbnail,
        }
        # if self.__title:
        #     fields["title"] = self.__title
        # if self.__description:
        #     fields["description"] = self.__description
        # if not len(self.__buttons) == 0:
        #     fields["buttons"] = []
        # for btn in self.__buttons:
        #     fields["buttons"].append(btn.to_string())
        # return fields

    def __to_string(self) -> str:
        fields = {
            "thumbnail": self.__thumbnail,
        }
        if self.__title:
            fields["title"] = self.__title
        if self.__description:
            fields["description"] = self.__description
        if not len(self.__buttons) == 0:
            fields["buttons"] = []
        for btn in self.__buttons:
            fields["buttons"].append(btn.to_string())
        return fields
