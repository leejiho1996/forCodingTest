# 방사형 그래프
import sys
input = sys.stdin.readline

def isPossible(arr):
    root2 = 2**(0.5)
    x = [0] * 8
    y = [0] * 8

    x[0], y[0] = 0, arr[0]
    x[1], y[1] = arr[1]/root2, arr[1]/root2
    x[2], y[2] = arr[2], 0
    x[3], y[3] = arr[3]/root2, -arr[3]/root2
    x[4], y[4] = 0, -arr[4]
    x[5], y[5] = -arr[5]/root2, -arr[5]/root2
    x[6], y[6] = -arr[6], 0
    x[7], y[7] = -arr[7]/root2, arr[7]/root2

    for i in range(8):
        a = (x[i], y[i])
        b = (x[(i+1)%8], y[(i+1)%8])
        c = (x[(i+2)%8], y[(i+2)%8])
        
        ab = (b[0]-a[0], b[1]-a[1])
        bc = (c[0]-b[0], c[1]-b[1])

        ccw = (ab[0] * bc[1]) - (ab[1] * bc[0])

        if ccw > 0:
            return False

    return True

def dfs(cnt, arr):
    global result
    
    if cnt == 8:
        if isPossible(arr):
            result += 1
        return

    for i in range(8):
        if visited[i]:
            continue

        visited[i] = 1
        arr.append(ability[i])
        dfs(cnt+1, arr)
        arr.pop()
        visited[i] = 0

ability = list(map(int,input().split()))
visited = [0] * 8
result = 0
dfs(0, [])

print(result)
