#하샤드 수
def solution(x):
    x_str = str(x)
    answer = sum(int(digit) for digit in sorted(x_str))
    if int(x) % answer == 0:
        return True
    else:
        return False
a = 10
print(solution(a))
b = 12
print(solution(b))
c = 11
print(solution(c))
d = 13
print(solution(d))