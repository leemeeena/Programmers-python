#정수 내림차순으로 배치하기 
def solution(n):
    #정수를 문자열로 변환
    n_str = str(n)
    #문자열을 리스트로 변환 후, 각 자릿수를 내림차순으로 정렬
    sorted_digits = sorted(n_str, reverse=True)
    #정렬된 리스트를 문자열로 변환
    sorted_str = ''.join(sorted_digits)
    return int(sorted_str)
a = 118372
print(solution(a))
