def solution(arr):
    for i in arr:
        if int(i + 1) == int(i):
            del(i)
    return i
a = [1,1,3,3,0,1,1]
print(solution(a))