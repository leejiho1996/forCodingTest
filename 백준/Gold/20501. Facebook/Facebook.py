#Facebook
import sys
input = sys.stdin.readline

N = int(input())
links = [[] for _ in range(N)]
bitCnt = [0] * ((1 << 20) + 1)

for i in range(N):
    link = input().rstrip()

    start = 0
    end = 20
    
    while start < N:
        links[i].append(int(link[start:end], 2))
        start = end
        end += 20
    
for i in range((1 << 20) + 1):
    bitCnt[i] = i.bit_count()

Q = int(input())

for i in range(Q):
    a, b = map(int,input().split())
    cnt = 0
    
    for j in range(len(links[0])):
        cnt += bitCnt[links[a-1][j] & links[b-1][j]]

    print(cnt)
        

        
