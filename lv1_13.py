#서울에서 김서방 찾기
def solution(seoul):
    x = seoul.index("Kim")
    return f"김서방은 {x}에 있다"
a = ["Jane", "Kim"]
print(solution(a))