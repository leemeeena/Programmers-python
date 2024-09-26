def solution(strings, n):
    # n번째 문자를 기준으로 정렬하기 위한 리스트 생성
    sorted_strings = []
    
    while strings:
        min_string = strings[0]  # 첫 번째 문자열을 기준으로 설정
        for string in strings:  
            if string[n] < min_string[n]:  # n번째 문자 비교
                min_string = string  # 더 작은 값을 찾으면 업데이트
            elif string[n] == min_string[n]:
                if string < min_string:
                    min_string = string
        sorted_strings.append(min_string)  # 정렬된 리스트에 추가
        strings.remove(min_string)  # 원본 리스트에서 제거
    
    return sorted_strings

# 함수 실행 예시
#print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))