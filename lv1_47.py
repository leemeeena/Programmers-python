def solution(array, commands):
    answer = []
    for number in commands:
        i, j, k = number
        com = sorted(array[i-1:j])
        answer.append(com[k-1])
    return answer
print(solution([1,5,2,6,3,7],[[2,5,3],[4,4,1],[1,7,3]]))