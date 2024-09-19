#자연수 뒤집어 배열로 만들기 
def solution(n):
    n_1 = str(n)
    reversed_deigits = [int(digit) for digit in reversed(n_1)]
    return reversed_deigits

a = 12345
print(solution(a))