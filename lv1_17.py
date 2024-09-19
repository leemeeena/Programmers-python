#나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []
    for number in arr: #리스트 순회를 위함 
        if number % divisor == 0:
            answer.append(number)
    if not answer:
        return [-1]
    return sorted(answer) #오름차순
a = [5, 9, 7, 10]
b = 5
print(solution(a, b))