#문자열을 정수로 바꾸기
def solution(s):
    try: 
        #문자열을 정수로 변환 시도
        return int(s)
    except ValueError:
        try:
            #정수 변환에 실패하면 실수로 변환시도
            return float(s)
        except ValueError:
            #변환할 수 없는 문자열인 경우
            return None
#테스트 실행
print(solution("1234"))
print(solution("-1234"))
