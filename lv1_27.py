def solution(arr1, arr2):
    result = []
    for c1, c2 in zip(arr1, arr2):
        result.append([x + y for x, y in zip(c1, c2)])
    return result
a = [[1,2],[2,3]]
b = [[3,4],[5,6]]
print(solution(a, b))