class Extra:
    # def __init__(self):
    #     self.__extra = {}               
    def __init__(self, key : str, value : object):
        self.__extra = {}       
        self.append(key, value)
    
    def append(self, key : str, value : object) -> 'Extra':
        if not isinstance(key, str):
            raise TypeError('key must be an instance of str')
        self.__extra[key] = value

        return self

    def to_string(self):
        return self.__extra


        