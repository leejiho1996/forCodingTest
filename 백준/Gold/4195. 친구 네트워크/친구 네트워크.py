# 친구 네트워크
import sys
input = sys.stdin.readline

def find(n):
    if n != parent[n]:
        parent[n] = find(parent[n])
    return parent[n]

t = int(input())

for i in range(t):
    f = int(input())
    friend = {}
    parent = [i for i in range(f*2)]
    count = [1 for _ in range(f*2)]
    cnt = 0
    for j in range(f):
        f1, f2 = input().rstrip().split()

        if f1 not in friend:
            friend[f1] = cnt
            cnt += 1
        if f2 not in friend:
            friend[f2] = cnt
            cnt += 1

        f1_p = find(friend[f1])
        f2_p = find(friend[f2])

        if f1_p != f2_p:
            if f2_p > f1_p:
                count[f2_p] += count[f1_p]
                parent[f1_p] = f2_p
                print(count[f2_p])
            else:
                count[f1_p] += count[f2_p]
                parent[f2_p] = f1_p
                print(count[f1_p])
        else:
            print(count[f1_p])
    
