import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]
link = []
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(n):
        if tmp[j]:
            link.append((i+1, j+1))


def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

for start, to in link:
    startParent = find(start)
    toParent = find(to)

    if startParent != toParent:
        if startParent > toParent:
            parent[startParent] = toParent
            find(start)
        else:
            parent[toParent] = startParent
            find(to)

plan = list(map(int,input().split()))

start = parent[plan[0]]
check = True
for i in plan:
    if parent[i] != start:
        check = False

if check:
    print("YES")
else:
    print("NO")
