#정수 제곱근 판별 
import math
def solution(n):
    sqrt_n = math.sqrt(n)
    
    if sqrt_n.is_integer(): #제곱근이 정수인지 확인 
        x = int(sqrt_n) #제곱근을 정수로 변환 
        return (x + 1) ** 2
    else: 
        return -1 
a = 121
print(solution(a))