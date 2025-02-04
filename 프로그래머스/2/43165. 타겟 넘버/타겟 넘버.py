total = 0

def dfs(num, cnt, target, numbers):
    global total
    
    if cnt == len(numbers):
        if num == target:
            total += 1
        return
    
    dfs(num-numbers[cnt], cnt+1, target, numbers)
    dfs(num+numbers[cnt], cnt+1, target, numbers)

def solution(numbers, target):
    dfs(0, 0, target, numbers)
    return total