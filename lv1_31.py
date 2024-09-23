def solution(arr):
    result = [] #중복을 제거한 값을 저장할 리스트 
    previous = None #이전 값을 저장할 변수
    
    for i in arr:
        if i != previous:
            result.append(i)
        previous = i
        
    return result

a = [1,1,3,3,0,1,1]
print(solution(a))