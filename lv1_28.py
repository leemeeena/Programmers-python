a, b = map(int, input().strip().split(' '))
#input(): 사용자가 입력한 값을 문자열로 
#strip(): 문자열의 앞뒤에 있는 공백을 제거
#split(' '): 문자열을 공백(스페이스)를 기준으로 나누어 리스트로 반환
#map(int) :map 함수 int를 적용하여 문자열을 정수로 반환
for _ in range(b):
    print('*' * a)
#map()함수는 반복 가능한(iterable)자료형(예:리스트,튜플,문자열 등)의 각 요소에 대해 지정된 함수를 적용하여 새로운 반복 가능한 객체 생성
#map(function, iterable) function:각 요소에 적용할 함수 iterable: 리스트, 튜플, 문자열 등의 반복 가능한 자료형