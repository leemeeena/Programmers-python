#내적
def solution(a, b):
    return sum(ai * bi for ai, bi in zip(a, b))
c = [1, 2, 3, 4]
d = [-3, -1, 0, 2]
print(solution(c, d))