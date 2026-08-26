def solution(nums):
# 가져갈 수 있는 최대 수: nums // 2
# 종류의 수를 일단 카운트 -> num//2보다 크면 num//2를 리턴, 작으면 카운트 수를 리턴

    # answer = 0
    res = []
    
    for i in nums:
        if i not in res:
            res.append(i)
            
    answer = len(res)
    l = len(nums) // 2
            
    if l > answer:
        return answer
    else:
        return l