#핸드폰 번호 가리기 
def solution(phone_number):
    length = len(phone_number)
    masked_part = '*' * (length - 4)
    last_4_digits = phone_number[-4:]
    return masked_part + last_4_digits
a = "01033334444"
print(solution(a))