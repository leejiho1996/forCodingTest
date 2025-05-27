# 램프
import sys
input = sys.stdin.readline

def switch(j):
    for i in range(N):
        if ramps[i][j] == '0':
            ramps[i][j] = '1'
        else:
            ramps[i][j] = '0'
            
#-- 입력
N, M = map(int,input().split())
ramps = []
result = 0

for i in range(N):
    row = list(input().rstrip())
    ramps.append(row)

K = int(input())
#-- 입력 끝

for i in range(N):
    switches = []

    for j in range(M):
        if ramps[i][j] == '0' and K:
             switch(j)
             switches.append(j)
             K -= 1

    if K % 2 == 1:
        K += len(switches)

        for s in switches:
            switch(s)

        continue
    
    total = 0
    for j in range(N):
        cnt = 0
        for k in range(M):
            if ramps[j][k] == '1':
                cnt += 1

        if cnt == M:
            total += 1

    result = max(result, total)

    K += len(switches)
    for s in switches:
        switch(s)

print(result)
