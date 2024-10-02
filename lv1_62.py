def solution(ingredient):
    count = 0
    for i in range(len(ingredient)-1):
        if ingredient[i + 1] == ingredient[i] + 1: 
            if ingredient[i] == 1 and ingredient[i + 1] ==  2 and ingredient[i + 2] == 3:
                count += 1
    return count
print(solution([2,1,1,2,3,1,2,3,1]))

#다시
