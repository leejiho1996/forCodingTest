# 물정수열
import sys
input = sys.stdin.readline

N = int(input())
physics = list(map(int,input().split()))
information = list(map(int,input().split()))
math = list(map(int,input().split()))

before = min(physics[0], information[0], math[0])
for i in range(1, N):
    p, i, m = physics[i], information[i], math[i]
    maxx = max(p, i, m)
    minn = min(p, i, m)

    if before >= maxx:
        print("NO")
        exit()
    elif minn == before:
        before = minn + 1
    elif minn > before:
        before = minn
    else:
        before += 1
        
print("YES")
