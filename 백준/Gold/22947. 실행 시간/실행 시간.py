# 실행 시간
import sys
input = sys.stdin.readline

def calTime():
    global result

    stack = [1]
    endTime = [0] * (N+1)
    endTime[1] = time[1]

    frontt = front.copy()
    maxx = 0
    
    while stack:
        cur = stack.pop()

        for i in back[cur]:
            frontt[i] -= 1
            endTime[i] = max(endTime[i], endTime[cur] + time[i])
            maxx = max(maxx, endTime[i])

            if endTime[i] == maxx:
                last_work = i
            
            if frontt[i] == 0:
                stack.append(i)

    result = min(result, maxx)

    return last_work
    
def solve(k, last, last_work):

    if k == 0:
        calTime()
        return

    for i in range(last+1, N+1):
        if i == last_work:
            continue
        
        tmp = time[i]
        
        time[i] = 0
        solve(k-1, i, last_work)
        time[i] = tmp

N, M, K = map(int,input().split())
time = [0] + list(map(int,input().split()))
start = [0] * (N+1)

front = [0] * (N+1)
back = [[] for _ in range(N+1)]
result = 1_000_000_000

for i in range(M):
    n1, n2 = map(int,input().split())
    front[n2] += 1
    back[n1].append(n2)

last_work = calTime()

solve(K, 1, last_work)
print(result)
