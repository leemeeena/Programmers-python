def solution(d, budget):
    d.sort()
    total = 0 #현재까지 사용한 예산
    count = 0 #포함된 항목의 수 
    
    for cost in d:
        if total + cost <= budget:
            total += cost 
            count += 1
        else:
            break
    return count

a = [1, 3, 2, 5, 4]
money = 9
print(solution(a, money))