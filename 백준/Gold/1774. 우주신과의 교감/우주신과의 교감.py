# 우주신과의 교감
import sys
input = sys.stdin.readline
import heapq

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def calDistance(x1, y1, x2, y2):
    distance = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
    return distance

n, m = map(int,input().split())

stars = []
parent = [i for i in range(n+1)]

for i in range(n):
    x, y = map(int,input().split())
    stars.append((i, x, y))

link = [[] for _ in range(n+1)]

for i in range(n):
    idx1, x1, y1 = stars[i]
    idx1 += 1
    for j in range(i+1, n):   
        idx2, x2, y2 = stars[j]
        idx2 += 1
        distance = calDistance(x1, y1, x2, y2)
        link[idx1].append((distance, idx2, idx1))
        link[idx2].append((distance, idx1, idx2))

for i in range(m):
    s1, s2 = map(int,input().split())
    link[s1].append((0, s2, s1)) 
    link[s2].append((0, s1, s2))

que = []

for i in link[1]:
    heapq.heappush(que, i)

total = 0

while que:
    distance, to, start = heapq.heappop(que)

    parent_to = find(to)
    parent_start = find(start)

    if parent_to != parent_start:
        parent[parent_to] = parent_start
        total += distance

        for i in link[to]:
            heapq.heappush(que, i)

print(f'{total:.2f}')

                    

