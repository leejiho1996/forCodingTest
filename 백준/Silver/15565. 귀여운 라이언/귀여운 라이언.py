# 귀여운 라이언
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
dolls = list(map(int,input().split()))
lionIdxs = []

for i in range(N):
    if dolls[i] == 1:
        lionIdxs.append(i)

start = 0
end = K - 1
result = 1000001

while end < len(lionIdxs):

    result = min(result, lionIdxs[end] - lionIdxs[start])
    
    start += 1
    end += 1

if result == 1000001:
    print(-1)
else:
    print(result + 1)
