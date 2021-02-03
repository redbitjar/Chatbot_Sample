"""Exception을 설명하는 모듈"""
# 31. Exception(예외) 흐름과 Exception Handling
# Exception 이란? : 정상적인 프로그램 흐름을 중단시키는 에러를 말합니다.
# Exception Handling이란? : 정상적인 프로그램 흐름을 중단하고 주변의 컨텍스트 또는 코드 블록에서 계속하기위한 메커니즘

def convert(s):
    """int로 변환"""    
    a = int(s)
    return a

# def convert2(s):
#     """int로 변환"""    
#     try:
#         a = int(s)
#     except ValueError:
#         print('실패 : ValueError')
#         a = -1
#     except TypeError:
#         print('실패 : TypeError')
#         a = -1
#     return a


# except 블럭을 하나로 합치겠습니다.
# def convert2(s):
#     """int로 변환"""    
#     try:
#         a = int(s)
#     except (ValueError, TypeError):
#         print('실패')
#         a = -1
#     return a

# 3-2 exception 정보얻기
# def convert2(s):
#     """int로 변환"""    
#     try:
#         a = int(s)
#     except (ValueError, TypeError) as e:
#         print('에러정보 : ', e)
#         a = -1
#     return a


def convert2(s):
    """int로 변환"""    
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print('에러정보 : ', e)
        raise

# 3-3. raise로 Exception발생시키기
from math import log
def string_logs(s):
    v = convert2(s)
    return log(v)