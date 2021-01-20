from  .link import Link

class Thumbnail:
    '''
    imageUrl 이미지의 url입니다.
    link  이미지 클릭시 작동하는 link입니다.
    fixedRatio true: 이미지 영역을 1:1 비율로 두고 이미지의 원본 비율을 유지합니다. 이미지가 없는 영역은 흰색으로 노출합니다.
    false: 이미지 영역을 2:1 비율로 두고 이미지의 가운데를 크롭하여 노출합니다.
    width fixedRatio를 true로 설정할 경우 필요한 값입니다. 실제 이미지 사이즈와 다른 값일 경우 원본이미지와 다르게 표현될 수 있습니다.
    height fixedRatio를 true로 설정할 경우 필요한 값입니다. 실제 이미지 사이즈와 다른 값일 경우 원본이미지와 다르게 표현될 수 있습니다.
    '''
    def __init__(self, image_url : str):
        self.__image_url = image_url
        self.__set_fixed_ratio = False        
        self.__link = ''
        self.__fixed_ratio = ''
        self.__width = ''
        self.__height = ''

    def set_link(self, link : Link) -> 'Thumbnail':
        self.__link = link.to_string()
        return self

    def set_fixed_ratio(self, fixed_ratio : bool) -> 'Thumbnail':
        self.__fixed_ratio = fixed_ratio
        return self
    
    def set_width(self, width : int) -> 'Thumbnail':
        self.__width = width
        return self

    def set_height(self, height : int) -> 'Thumbnail':
        self.__height = height
        return self

    def to_string(self) -> str:
       
        fileds = {"imageUrl" : self.__image_url}
        if self.__link:
            fileds["link"] = self.__link
        if self.__fixed_ratio:
            fileds["fixed_ratio"] = self.__fixed_ratio
        if self.__width:
            fileds["width"] = self.__width
        if self.__height:
            fileds["height"] = self.__height
        # ret = f"{self.__image_url} , {self.__link} , {self.__fixed_atio}, {self.__width} , {self.__height}"
        return fileds