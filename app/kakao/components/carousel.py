from typing import List
from .component_base import OutputComponent
from .basic_card import BasicCard
from .carousel_header import CarouselHeader

TbasicCards = List[BasicCard]
class Carousel(OutputComponent):

    '''
    케로셀은 여러 장의 카드를 하나의 메세지에 일렬로 포함하는 타입입니다.
    '''
    def __init__(self, items : TbasicCards):
        self.__items = items
        self.__header = ''

    # def set_items(self, items : TbasicCards):
    #     self.__items = items

    # def set_header(self, header : CarouselHeader):
    #     '''
    #     CommerceCard 만 지원하고 있습니다. 추후 BasicCard 도 지원할 예정입니다.
    #     '''
    #     self.__header = header

    def to_string(self) -> str:
        type = "carousel"
        fields = {
            "carousel": {
                "type": 'basicCard',
            }
        }
        if not len(self.__items) == 0:
            fields[type]["items"] = []
        
        for item in self.__items:
            fields[type]["items"].append(item.to_string_notype())

        return fields


