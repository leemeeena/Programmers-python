#제일 작은 수 제거하기 
def solution(arr):
    if len(arr) <= 1:
        return [-1]
    min_value = min(arr)
    arr.remove(min_value)
    return arr
a = [4, 3, 2, 1]
print(solution(a))
