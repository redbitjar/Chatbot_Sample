from .output_component import OutputComponent

class SimpleImage(OutputComponent):
    '''
        imageUrl 전달하고자 하는 이미지의 url입니다 (URL 형식) , 
        altText url이 유효하지 않은 경우, 전달되는 텍스트입니다 (최대 1000자)
    '''
    def __init__(self, image_url : str, alt_text : str):       
        self.__image_url = image_url
        self.__alt_text = alt_text

    def to_string(self) -> str:
        fields = {
            "simpleImage":{
                "imageUrl": self.__image_url,
                "altText": self.__alt_text
            }
        }
        return fields