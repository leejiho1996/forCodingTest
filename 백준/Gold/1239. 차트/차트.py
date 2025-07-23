# 차트
import sys
input = sys.stdin.readline

def dfs(cur, arr):
    global result

    if cur == N:
        cnt = 0
        total = 0
        
        for i in range(N):
            tmp = 0
            total += arr[i]

            if total > 50:
                break
            
            for j in range(i, N):
                tmp += arr[j]
                
                if tmp == 50:
                    cnt += 1
                    break
                
        result = max(result, cnt)

    for i in range(N):

        if visited[i]:
            continue
        else:
            arr.append(nums[i])
            visited[i] = 1
            
            dfs(cur+1, arr)

            visited[i] = 0
            arr.pop()
            
N = int(input())
nums = list(map(int,input().split()))
visited = [0] * N
result = 0

dfs(0, [])

print(result)
