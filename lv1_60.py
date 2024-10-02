import math
def solution(nums):
    nums.sort()
    count = 0
    
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):
                total = nums[i] + nums[j] + nums[k]
                
                is_prime = True #실수인지
                if total < 2:
                    is_prime = False
                else:
                    for n in range(2, int(math.sqrt(total)) + 1):
                        if total % n == 0:
                            is_prime = False
                            break
                if is_prime:
                    count += 1
    return count 
print(solution([1,2,3,4]))