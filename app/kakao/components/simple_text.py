from .component_base import OutputComponent

class SimpleText(OutputComponent):
    '''
        text 전달하고자 하는 텍스트입니다 (1000자)
    '''
    def __init__(self, text : str):
        self.__text = text

    def to_string(self) -> str:
        fields = {
            "simpleText":{
                "text": self.__text
            }
        }
        return fields