from abc import *

class OutputComponent(metaclass=ABCMeta):
    '''
    카카오 parent 컴포넌트
    child 컴포넌트에는 simpleText, simpleImage, basiCard, listCard 사용
    '''
    @abstractmethod
    def to_string(self) -> str:
        pass
