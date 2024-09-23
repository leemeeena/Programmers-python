def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit() #문자열이 모두 숫자인지 확인
    return False
a = "a234"
b = "1234"
print(solution(a))
print(solution(b))