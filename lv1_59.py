def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    answer_1 = 0
    answer_2 = 0
    answer_3 = 0
    
    for i in range(len(answers)):
        if answers[i] == one[i % len(one)]:
            answer_1 += 1
        if answers[i] == two[i % len(two)]:
            answer_2 += 1
        if answers[i] == three[i % len(three)]:
            answer_3 += 1
    
    max_score = max(answer_1, answer_2, answer_3)
    result = []
    
    if answer_1 == max_score:
        result.append(1)
    if answer_2 == max_score:
        result.append(2)
    if answer_3 == max_score:
        result.append(3)    
    return result

print(solution([1,2,3,4,5]))