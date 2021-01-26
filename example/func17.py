# 숨은 기능 17 가지
# 1. 변수 값 swap

print('--------- 1. 변수 값 swap ------')
a, b = 1, 10
print(a,b)
a, b = b, a
print(a,b)

print('--------- 2. 리스트 내용으로 문자열 만들기 ------')
a = ['Python', 'is', 'awesome']
print(' '.join(a))

print('--------- 3. 가장 빈번하게 등장한 요소 찾기 ------')
a = [1,2,3,1,2,3,1,1,1,1]
from collections import Counter
cnt = Counter(a)
print(cnt.most_common(3))