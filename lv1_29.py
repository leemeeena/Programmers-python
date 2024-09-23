import math
def solution(n, m):
    #최대공약수(GCD)
    gcd = math.gcd(n, m)
    #최소공배수(LCM)
    lcm = abs(n * m) // gcd
    return[gcd, lcm]
a = 3
b = 12
c = 2
d = 5
print(solution(a, b))
print(solution(c, d))