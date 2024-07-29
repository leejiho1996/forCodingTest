# 우수마을
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
people = [0] + list(map(int,input().split()))

link = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b = map(int,input().split())
    link[a].append(b)
    link[b].append(a)

def dfs(n, prev):
    choice = people[n]
    nchoice = 0

    for i in link[n]:
        if i == prev:
            continue
        
        next_choice, next_nchoice = dfs(i, n)
        choice += next_nchoice
        nchoice += max(next_nchoice, next_choice)
        
    return choice, nchoice


ans = max(dfs(1,-1))
print(ans)
