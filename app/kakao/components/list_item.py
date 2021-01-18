from  .link import Link

class ListItem:
    def __init__(self, title : str):
        self.__title = title
        self.__description = ''
        self.__image_url = ''
        self.__link = ''

    def set_description(self, description : str) -> 'ListItem':
        self.__description = description
        return self
    
    def set_image_url(self, image_url : str) -> 'ListItem':
        self.__image_url = image_url
        return self

    def set_link(self, link : Link) -> 'ListItem':
        self.__link = link.to_string()
        return self
    
    def to_string(self) -> str:
        fileds = {"title" : self.__title}
        if self.__description:
            fileds["description"] = self.__description
        if self.__image_url:
            fileds["image_url"] = self.__image_url
        if self.__link:
            fileds["link"] = self.__link

        return fileds