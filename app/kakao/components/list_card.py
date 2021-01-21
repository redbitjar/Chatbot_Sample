from typing import List
from .output_component import OutputComponent
from .button import Button
from .list_item import ListItem

Tbuttons = List[Button]
Titems = List[ListItem]
class ListCard(OutputComponent):

    '''
    header 카드의 상단 항목
    items 	카드의 각각 아이템 (최대 5개)
    buttons  (최대 2개)
    '''
    def __init__(self, header : ListItem, items : Titems):
        self.__header = header.to_string()
        if len(items) == 0:
            raise Exception('items count is zero')
        self.__items = items
        self.__buttons = []

    def set_button(self, button : Button) -> 'ListCard': 
        self.__buttons.append(button)
        return self

    def set_buttons(self, buttons : Tbuttons) -> 'ListCard': 
        self.__buttons = buttons
        return self

    def to_string(self) -> str:
        type = "listCard"
        fields = {
            type: {
                "header": self.__header,
            }
        }

        if len(self.__items) > 5:
            raise Exception('items는 최대 5개 입니다')
        if len(self.__buttons) > 2:
            raise Exception('button은 최대 2개 입니다')

        if not len(self.__items) == 0:
            fields[type]["items"] = []
            for item in self.__items:
                fields[type]["items"].append(item.to_string())
        
        if not len(self.__buttons) == 0:
            fields[type]["buttons"] = []
            for btn in self.__buttons:
                fields[type]["buttons"].append(btn.to_string())
        return fields