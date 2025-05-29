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

        # 한번 확인한 밑변은 패스
        if visited[width]:
            continue
        else:
            visited[width] = 1

        # 현재 밑변에 가능한 가장 큰 높이    
        target = R / width * 2

        if flagpoles[0] > target:
            continue
        
        start = 0
        end = K-1

        # 이분 탐색으로 현재 가능한 가장 큰 높이를 찾는다
        while start <= end:
            mid = (start + end) // 2

            if flagpoles[mid] <= target:
                start = mid+1
            else:
                end = mid-1

        # 해당 높이가 target보다 같거나 작으면 result 갱신
        if flagpoles[start-1] <= target:
            result = max(result, width * flagpoles[start-1] / 2)

print(result)
    
