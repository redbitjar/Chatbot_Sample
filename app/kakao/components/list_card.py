from .kakao_component import KakaoComponent
from .button import Button
from .list_item import ListItem

class ListCard(KakaoComponent):

    '''
    header 카드의 상단 항목
    items 	카드의 각각 아이템 (최대 5개)
    buttons  (최대 2개)
    '''
    def __init__(self, header : ListItem, items : list[ListItem]):
        self.__header = header.to_string()
        if len(items) == 0:
            raise Exception('items count is zero')
        self.__items = items
        self.__buttons = []

    def set_button(self, button : Button) -> 'ListCard': 
        self.__buttons.append(button)
        return self

    def set_buttons(self, buttons : list[Button]) -> 'ListCard': 
        self.__buttons = buttons
        return self

    def to_string(self) -> str:
        type = "listCard"
        fields = {
            type: {
                "header": self.__header,
            }
        }
        if not len(self.__items) == 0:
            fields[type]["items"] = []
            for item in self.__items:
                fields[type]["items"].append(item.to_string())
        
        if not len(self.__buttons) == 0:
            fields[type]["buttons"] = []
            for btn in self.__buttons:
                fields[type]["buttons"].append(btn.to_string())
        return fields