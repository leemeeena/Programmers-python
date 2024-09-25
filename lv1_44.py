def solution(s):
    answer = [] #결과를 저장할 리스트
    #각 문자의 마지막 위치를 저장할 딕셔너리
    last_seen = {}
    
    for i in range(len(s)):
        char = s[i]
        if char in last_seen:
            #문자가 이미 나타났다면, 마지막 인덱스와 현재 인덱스 간의 거리 계산
            distance = i - last_seen[char]
            answer.append(distance)
        else:
            answer.append(-1)
        last_seen[char] = i
    
    return answer
print(solution("banana"))