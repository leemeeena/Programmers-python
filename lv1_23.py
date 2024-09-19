#약수의 개수와 덧셈
def solution(left, right):

    answer = 0
    for j in range(left, right + 1):
        num = 0
        for i in range(1 , j + 1):
            if j % i == 0:
                num += 1
        if num % 2 == 0:
            answer += j
        else: 
            answer -= j
    return answer
a = 13
b = 17
print(solution(a, b))