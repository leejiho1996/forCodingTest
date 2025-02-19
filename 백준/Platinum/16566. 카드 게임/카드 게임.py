# 카드 게임
import sys
input = sys.stdin.readline

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])

    return parent[n]

n, m, k = map(int,input().split())
cards = list(map(int,input().split()))
putOut = list(map(int,input().split()))
parent = [i for i in range(n+1)]

cards.sort()
for i in range(k):
    cur = putOut[i]

    start = 0
    end = m-1

    while start <= end:
        mid = (start + end) // 2

        if cur >= cards[mid]:
            start = mid + 1
        else:
            end = mid - 1

    p = find(start)
    print(cards[p])
    parent[p] = find(p+1)
    
