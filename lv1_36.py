def solution(t, p):
    num = len(p)
    count = 0
    for i in range(len(t) - num + 1):
        if t[i:i+num] <= p :
            count += 1
    return count
print(solution("3141592", "271"))