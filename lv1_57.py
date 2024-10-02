def solution(a, b):
    days_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ["FRI", "SAT","SUN", "MON", "TUE", "WED", "THU"]             
    
    sum_days = sum(days_in_month[:a - 1])
    
    sum_days += b - 1
    
    return day[sum_days % 7]
print(solution(5, 24))