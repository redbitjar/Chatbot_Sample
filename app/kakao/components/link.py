class Link:
    def __init__(self):
        self.__pc = ''
        self.__mobile = ''
        self.__web = ''

    def set_pc(self, pc : str) -> 'Link':
        self.__pc = pc
        return self

    def set_mobile(self, mobile : str) -> 'Link':
        self.__mobile = mobile
        return self

    def set_web(self, web : str) -> 'Link':
        self.__web = web
        return self

    def to_string(self) -> str:
        fileds = {}
        if self.__pc:
            fileds["pc"] = self.__pc
        if self.__mobile:
            fileds["mobile"] = self.__mobile
        if self.__web:
            fileds["web"] = self.__web
        
        return fileds
        

    