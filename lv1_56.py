def solution(cards1, cards2, goal):
    answer = ''
    num1 = 0
    num2 = 0
    for goal_ in goal:
        if num1 < len(cards1) and goal_ == cards1[num1]:
            num1 += 1
        elif num2 < len(cards2) and goal_ == cards2[num2]:
            num2 += 1
        else:
            return "No"
    return "Yes"
    
print(solution(["i","water","drink"],["want","to"],["i","want","to","drink","water"]))