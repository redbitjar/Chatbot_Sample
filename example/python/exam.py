# https://wikidocs.net/16043

# 16 튜플

t = (1, "korea", 3.5, 1)
print(t)

# es6 해체할당과 비슷
def minmax(items):
     return min(items), max(items)

_min, _max = minmax([7,5,2,1,11,15,55])
print(_min, _max)

# 3. dictionary(딕셔너리) 변환
print('3. dictionary(딕셔너리) 변환')
name_and_ages = [['alice', 5], ['Bob', 13]]
print(dict(name_and_ages))
name_and_ages = [('alice', 5), ('Bob', 13)]
print(dict(name_and_ages))

# 6. dictionary(딕셔너리) for문
print('6. dictionary(딕셔너리) for문')
a = {'alice' : [1,2,3], 'bob':20, 'tony':15, 'suzy':30}
for key in a :
    print(key)
for value in a.values():
    print(value)
for key, val in a.items():
    print("key = {key}, value  = {value}".format(key=key, value=val))

# 7. dictionary(딕셔너리) 의 in
print('7. dictionary(딕셔너리) 의 in')
print('alice' in a)
print('teacher' not in a)

# 9. dictionary(딕셔너리)를 읽기 쉽게 표현해주는 pprint
print('9. dictionary(딕셔너리)를 읽기 쉽게 표현해주는 pprint')
from pprint import pprint as pp
pp(a)

# tuple 형태 반환
var_tuple = (1, 3, 5, 7)
for i, v in enumerate(var_tuple):
    print("index :{}, value: {}".format(i,v))

# import word.py
# import words
# help(words)

#2. 함수의 인자 전달
print('2. 함수의 인자 전달')
m = [1,5,7]
def modify(k):
    k.append(10)
    print("k = ", k)

modify(m)
print(m)

# 27. 함수 인자(Arguments)
# 1. default value(기본값)
print('1. default value(기본값)')
def define_suwoni(msg, nick='천재'):
    print("""
    수워니는 어떤사람? {msg}
    수워니의 별명은? {nick}
    """.format(msg=msg, nick=nick)
    )

define_suwoni('키큰사람', '바보')

# default value를 mutable한 객체로 했을때 주의가 필요합니다.
# 적당한 변수를 만들어 대입했을때는 문제가 없어 보이지만, default value를 여러번 사용하게 될 경우 예상치 않은 결과가 나올 수 있습니다.
print('default value를 여러번 사용하게 될 경우 예상치 않은 결과가 나올 수 있습니다.')
def add_book(book_list=[]):
    book_list.append('파이썬 베이직')
    return book_list

book_list=['hello', 'python', 'head first python']
print(add_book(book_list))
print(book_list)
print(add_book())
print(add_book())
# 해결책은 default value를 None으로 주고, None인 경우에만 값을 할당합니다.
print('해결책은 default value를 None으로 주고, None인 경우에만 값을 할당합니다.')

def add_book2(book_list=None):
    if book_list is None:
        book_list = []
    book_list.append('파이썬 베이직')
    return book_list
print(add_book2())
print(add_book2())

# 3. keyword argument(키워드 인자)
print('3. keyword argument(키워드 인자)')
def abc(a,b,c):
    return b,a,c

print(abc(1,2,3))
print(abc(1,2, c=3))
print(abc(1, c=3, b=2))

# 4. 위치 인자 언패킹
print('4. 위치 인자 언패킹')
def abc2(a,b,c):
    return b,a,c

p = [5,7,9]
print(abc2(*p))
# 함수의 인자 수와 입력하는 객체의 수가 다르면 에러가 발생합니다.
# z = [5,9]
# abc2(*z)
# 변수대신 바로 입력할 수 있습니다.
print('변수대신 바로 입력할 수 있습니다.')
print(abc2(*[1,5,9]))
print(abc2(*(1,5,9)))

# 입력할 때 뿐만아니라, 정의할 때도 사용할 수 있습니다.
print('입력할 때 뿐만아니라, 정의할 때도 사용할 수 있습니다.')
def abc3(*args):
    return args[1], args[0], args[2]
print(abc3(*(1,5,9)))

# 함수를 정의할때, 고정 인자와 위치인자 언패킹을 함께 사용할 수 있습니다.
print('함수를 정의할때, 고정 인자와 위치인자 언패킹을 함께 사용할 수 있습니다.')
def abc4(a, *args):
    return args[0], a, args[1]
print(abc4(*(1,5,9)))

# 5. 키워드 인자 언패킹
print('키워드인자 언패킹은 키와 값이 있는 dictionary타입의 변수에 ** 표시를 해서 대입합니다.')
def air_line(departure, arrival, flighttime):
    print('출발지는 : ', departure)
    print('도착지는 : ', arrival)
    print('비행시간은 : ', flighttime)

myflight = {'departure':'서울', 'arrival':'LA', 'flighttime':'10시간'}
air_line(**myflight)
print('변수가 아닌 인자에 바로 값을 입력하고 언패킹 표시를 해줄 수 있습니다.')
air_line(**{'departure':'서울', 'arrival':'LA', 'flighttime':'10시간'})

print('함수정의할 때 키워드 인자 언패킹을 이용할 수 있습니다.')
def air_line2(**kwargs):
    print('출발지는 : ', kwargs['departure'])
    print('도착지는 : ', kwargs['arrival'])
    print('비행시간은 : ', kwargs['flighttime'])

air_line2(**{'departure':'서울', 'arrival':'프라하', 'flighttime':'14시간'})

def air_line3(departure, **kwargs):
    print('출발지는 : ', departure)
    print('도착지는 : ', kwargs['arrival'])
    print('비행시간은 : ', kwargs['flighttime'])

air_line3(**{'departure':'서울', 'arrival':'프라하', 'flighttime':'11시간'})
