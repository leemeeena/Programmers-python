number = int(input())

answer = 0

while number > 0:
    answer += number % 100
    number //= 100 #'/= 연산자' ; 실수나누기 
    # '//= 연산자' ; 정수나누기  

print(answer)