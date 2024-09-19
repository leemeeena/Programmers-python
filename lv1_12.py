#두 정수의 합
def solution(a, b):
    start = min(a, b)
    end = max(a, b)
    total_sum = sum(range(start, end + 1))
    return total_sum
c = 3
d = 5
print(solution(c, d))
e = 5
f = 3
print(solution(e, f))