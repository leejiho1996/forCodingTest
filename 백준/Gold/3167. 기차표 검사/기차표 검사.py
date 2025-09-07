# 기차표 검사
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
in_out = [[0] * 2 for _ in range(N)]

for i in range(N):
    out, enter = map(int,input().split())
    in_out[i][0] = enter
    in_out[i][1] = out

maxx = 0
c = in_out[0][0]
nc = 0
for i in range(1, N):
    out = in_out[i][1]

    if nc >= out:
        nc -= out
        maxx += out
    else:
        maxx += nc
        nc = 0
        c -= (out - nc)

    nc += in_out[i][0]

    if i % K == 0:
        c += nc
        nc = 0
    
minn = 0
c = in_out[0][0]
nc = 0
for i in range(1, N):
    out = in_out[i][1]

    if c >= out:
        c -= out
    else:
        minn += (out - c)
        nc -= (out - c)
        c = 0
        
    nc += in_out[i][0]
    if i % K == 0:
        c += nc
        nc = 0

print(minn, maxx)
