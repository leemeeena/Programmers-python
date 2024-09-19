#가운데 글자 가져오기 
def solution(s):
    lenth = len(s)
    middle = len(s) // 2    
    if lenth % 2 == 0:
        return s[middle - 1 : middle + 1]
    else:
        return s[middle]
a = "abcde"
print(solution(a))
b = "qwer"
print(solution(b))
