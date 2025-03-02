# 차이를 최대로
import sys
input = sys.stdin.readline

def dfs(cnt, num_list):
    global result
    
    if cnt == n:
        total = 0
        
        for i in range(0, n-1):
            total += abs(num_list[i] - num_list[i+1])
    
        result = max(result, total)
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = 1
        num_list.append(nums[i])
        dfs(cnt+1, num_list)
        visited[i] = 0
        num_list.pop()

n = int(input())
nums = list(map(int,input().split()))
visited = [0] * n
result = -801

dfs(0, [])
print(result)
