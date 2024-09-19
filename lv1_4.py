#약수의 합
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            print(i)# i가 n의 약수인지 확인 
            answer += i # 약수의 합을 계산 
    return answer
print(solution(12))