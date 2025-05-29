# 현수막 걸기
import sys
input = sys.stdin.readline

N, K, R = map(int,input().split())
stakes = list(map(int,input().split()))
flagpoles = list(map(int,input().split()))

stakes.sort()
flagpoles.sort()

visited = [0] * 40001
result = -1

for i in range(N):
    for j in range(i+1, N):
        width = stakes[j] - stakes[i]

        if visited[width]:
            continue
        else:
            visited[width] = 1
            
        target = R / width * 2
        
        start = 0
        end = K-1

        while start <= end:
            mid = (start + end) // 2

            if flagpoles[mid] <= target:
                start = mid+1
            else:
                end = mid-1

        if flagpoles[start-1] <= target:
            result = max(result, width * flagpoles[start-1] / 2)
        else:
            break
            
print(result)
    
