from .enum_type import Action, action_navigate
from .extra import Extra

class Button:
    '''
    title 카드의 제목입니다.(최대 2줄)
    description 카드에 대한 상세 설명입니다. (최대 230자)
    thumbnail 카드의 상단 이미지입니다.
    buttons 카드의 버튼들을 포함합니다. (최대 3개)
    ''' 
    def __init__(self, label : str, action : Action):
        self.__label = label       
        self.__action = action_navigate(action)
        self.__web_link_url = ''
        self.__mesaage_text = ''
        self.__phone_number = ''
        self.__block_id = ''
        self.__extra = ''

    def set_web_link_url(self, web_link_url : str) -> 'Button':
        self.__web_link_url = web_link_url
        return self
    
    def set_mesaage_text(self, mesaage_text : str) -> 'Button':
        self.__mesaage_text = mesaage_text
        return self

    def set_phone_number(self, phone_number : str) -> 'Button':
        self.__phone_number = phone_number
        return self
    
    def set_block_id(self, block_id : str) -> 'Button':
        self.__block_id = block_id
        return self

    def set_extra(self, extra : Extra) -> 'Button':
         self.__extra = extra.to_string()
         return self

    def to_string(self) -> str:
        fields = {
            "label" : self.__label,
            "action" : self.__action
        }
        if self.__web_link_url:
            fields["webLinkUrl"] = self.__web_link_url
        if self.__mesaage_text:
            fields["messageText"] = self.__mesaage_text
        if self.__phone_number:
            fields["phoneNumber"] = self.__phone_number
        if self.__block_id:
            fields["blockId"] = self.__block_id
        if self.__extra:
            fields["extra"] = self.__extra

        return fields