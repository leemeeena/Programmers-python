#나머지가 1이 되는 수 찾기
def solution(n):
    answer = 0
    x = 2 
    while x > 1: 
        if n % x == 1: 
            break
        x += 1
    return x 
print(solution(10))
print(solution(12))