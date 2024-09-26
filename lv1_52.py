def solution(a, b, n):
    bottle = n
    answer = 0
    
    while bottle >= a: 
        quo = bottle // a
        new_bottles = quo * b 
        bottle = bottle % a + new_bottles
        answer += new_bottles
    return answer 

print(solution(2, 1, 20))
print(solution(3, 1, 20))