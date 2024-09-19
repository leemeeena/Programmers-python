#없는 숫자 더하기
def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers: #숫자가 numbers에 포함되지 않은 경우
            answer += i 
    return answer
a = [1,2,3,4,6,7,8,0]
print(solution(a))