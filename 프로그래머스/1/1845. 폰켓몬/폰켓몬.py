def solution(nums):
    num_length = len(nums)
    sett = set(nums)
    set_length = len(sett)
    
    if (set_length >= num_length//2):
        return num_length//2
    else:
        return set_length
    