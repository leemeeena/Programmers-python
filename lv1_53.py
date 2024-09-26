def solution(k, score):
    hall_of_fame = []
    daily_min_scores = []
    
    for i in score:
        hall_of_fame.append(i)
        hall_of_fame.sort(reverse = True)
        
        if len(hall_of_fame) > k:
            hall_of_fame.pop() 
            #가장 작은 값 제거(정렬된 상태이므로 마지막 요소 )
        daily_min_scores.append(hall_of_fame[-1])  
        
    return daily_min_scores
print(solution(3, [10, 100, 20, 150, 1, 100, 200]))