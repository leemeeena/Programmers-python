def solution(s, n):
    answer = ''
    for char in s:
        if char.isalpha(): #알파벳인지 확인
            if char.isupper(): #대문자 처리
                answer += chr((ord(char) - ord('A') + n)%26 + ord('A')) 
#chr() : 주어진 정수(ASCII)를 해당하는 문자로 반환 #ord() : 주어진 문자의 Unicode값을 정수로 반환
            else:
                answer += chr((ord(char) - ord('a') + n)%26 + ord('a'))
        else: 
            answer += char
    return answer
solution("AB", 1)
solution("z", 1)
solution("a B z", 4)