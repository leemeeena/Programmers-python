def solution(s): 
    number = { 'zero' : 0 , 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7 , 'eight': 8, 'nine' : 9 }
    result = ''
    word = ''
    for char in s:
        if char.isdigit(): #현재 문자가 숫자라면
            result += char #결과 문자열에 추가
        else: #문자가 숫자가 아닌라면
            word += char #현재 문자를 누적
            if word in number: #누적된 문자가 숫자 영단어와 매칭되는지 확인
                result += str(number[word]) #매칭된 영단어를 숫자로 변환하여 결과에 추가
                word = ''   #누적된 단어 초기화
    return int(result) #최종 결과를 정수로 반환
solution("one4seveneight")