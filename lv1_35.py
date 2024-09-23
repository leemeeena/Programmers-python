def solution(n):
    ternary = ""  # 3진법 문자열 초기화
    while n > 0:  # 3진법으로 변환
        ternary += str(n % 3)  # 나머지를 문자열로 변환하여 추가
        n //= 3  # n을 3으로 나누어 몫을 업데이트
    
    reversed_ternary = ternary[::-1]  # 3진법 문자열 뒤집기
    result = 0  # 최종 10진법 값을 저장할 변수 초기화
    
    for i, digit in enumerate(reversed_ternary):  # 뒤집은 3진법 문자열을 순회
        result += int(digit) * (3 ** i)  # 각 자리수의 10진법 값을 계산하여 더하기
    
    return result  # 최종 결과 반환

# 테스트 예시
a = 45
print(solution(a))  # 출력: 7
