def solution(numbers):
    answer = []
    number = sorted(numbers)
    for i in range(len(number) - 1):
        for j in range( i + 1,len(number)):
            sum_value = number[i] + number[j]
            if sum_value not in answer:
                answer.append(sum_value)
    return sorted(answer)
solution([2,1,3,4,1])