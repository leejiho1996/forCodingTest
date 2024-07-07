import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n+1)]
link = []
for i in range(n):
    tmp = list(map(int,input().split()))
    for j in range(i+1, n):
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
        else:
            parent[toParent] = startParent

plan = list(map(int,input().split()))

start = find(plan[0])
check = True
for i in plan:
    if find(i) != start:
        check = False

if check:
    print("YES")
else:
    print("NO")
