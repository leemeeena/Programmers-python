def solution(number, limit, power):
    answer = []
    for num in range(1, number + 1):
        count = 0
        for num1 in range(1, int(num**0.5) + 1):
            if num % num1 == 0:
                count += 1
                if num1 != num // num1: #여기 몰루...
                    count += 1
                
        if count > limit:
            answer.append(power)
        else:
            answer.append(count)
    result = sum(answer)
    return result
print(solution(5, 3, 2))