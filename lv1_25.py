#부족한 금액 계산하기 
def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        answer += price * i
    return max(answer - money, 0)
a = 3
b = 20
c = 4
print(solution(a, b, c))