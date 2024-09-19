#자릿수 더하기
def solution(n):
    n_str = str(n)
    
    answer = sum(int(digit) for digit in n_str)
    return answer

a = "123"
print(solution(a))