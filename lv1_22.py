#수박수박수박수박수박수?
def solution(n):
    answer = "수박" * (n//2) + "수" * (n % 2)
    return answer