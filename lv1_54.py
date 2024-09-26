def solution(n, arr1, arr2):
    answer = []  # 최종 비밀지도를 저장할 리스트
    
    for i in range(n):
        combined_map = arr1[i] | arr2[i]  # 비트 OR 연산
        row = bin(combined_map)[2:].zfill(n).replace('1', '#').replace('0', ' ')
        answer.append(row)  # 변환된 문자열을 결과 리스트에 추가
    
    return answer

# 실행 예시
print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))