def solution(nums):
    len_ = len(nums) / 2
    li = list(set(nums)) #리스트에서 중복된 요소를 제거하려면, 리스트를 집합으로 변환한후, 다시 리스트로 변환
    if len_ < len(li):
        return len_
    if len_ >= len(li):
        return len(li)
print(solution([3,3,3,2,2,4]))