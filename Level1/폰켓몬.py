def solution(nums):
    answer = 0
    mm = max(nums)
    chk = [0] * (mm+1)
    selc = len(nums) // 2
    for n in nums:
        if chk[n] == 0:
            chk[n] = 1
    total = chk.count(1)
    if selc > total:
        answer = total
    else:
        answer = selc
    return answer