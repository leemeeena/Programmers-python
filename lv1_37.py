def solution(s):
    words = s.split(" ")
    #입력된 문자열을 공백 기준으로 단어별로 나누어 리스트로 변환 
    #결과를 저장할 빈 리스트 생성
    result = []
    #각 단어에 대해 반복
    for word in words:
        #변화된 단어를 저장할 빈 문자열 생성
        new_word = ''
        #단어의 각 문자에 대해 인덱스와 문자를 함께 가져옴
        for i, char in enumerate(word):
            #인덱스가 짝수일 때는 대문자로 변환
            if i % 2 ==0:
                new_word += char.upper()
            #인덱스가 홀수일 때는 소문자로 변환
            else:
                new_word += char.lower()
        #변화된 단어를 결과 리스트에 추가
        result.append(new_word)
    
    #변화된 단어들을 공백으로 다시 연결하여 문자열로 반환
    return " ". join(result)
a = "try hello world"
print(solution(a))