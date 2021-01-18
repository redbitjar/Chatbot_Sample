from .thumbnail import Thumbnail

class CarouselHeader:
    
    def __init__(self, title : str, description : str, thumbnail : Thumbnail ):
        self.__title = title
        self.__description = description        
        self.__thumbnail = thumbnail.to_string()

    def to_string(self) -> str:
        fileds = {}
        if self.__title:
            fileds["title"] = self.__title
        if self.__title:
            fileds["description"] = self.__description
        if self.__title:
            fileds["thumbnail"] = self.__thumbnail
        
        return fileds

    