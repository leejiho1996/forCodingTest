# 그래프 트리 분할
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

if m == 0: # m이 0이라면 불가능
    print(-1)
    exit()

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def check(k, sep=-1):
    nodes = []
    link = set()
    for i in range(1, n+1):
        if i == sep or parent[i] != k:
            continue
        nodes.append(i)
        for j in links[i]:
            if j[0] == sep:
                continue
            link.add(j[1])
    
    return [nodes, link]

parent = [i for i in range(n+1)] # 부모노드 저장
links = [[] for _ in range(n+1)] 

for i in range(m):
    start, end = map(int,input().split())

    p1 = find(start)
    p2 = find(end)

    if p1 != p2: # 부모 노드가 같지 않다면 부모노드 갱신
        if p1 > p2:
            parent[p1] = p2
        else:
            parent[p2] = p1
        links[start].append((end, i+1))
        links[end].append((start, i+1))

trees = {}
leaf = []

for i in range(1, n+1):
    p = find(i)
    if p not in trees:
        trees[p] = 1
    else:
        trees[p] += 1

    if len(links[i]) == 1:
        leaf.append(i)

if len(trees) >= 3: # 트리가 3개 이상이면 둘로 못나눈다 
    print(-1)
    exit()
# 트리가 2개더라도 노드의 수가 같으면 다른 크기로 못나눈다
elif len(trees) == 2 and len(set(trees.values())) == 1: 
    print(-1)
    exit()
elif n == 2: # 노드수가 2개라면 다른 크기로 못나눈다
    print(-1)
    exit()

root = list(trees.keys())
visited = [0] * (n+1)

if len(root) == 2:
    main, main_link = check(root[0])
    sep, sep_link = check(root[1])
else:
    main, main_link = check(root[0], leaf[0])
    sep, sep_link = [leaf[0]], []   

print(len(main), len(sep))
print(*main)
print(*main_link)
print(*sep)
print(*sep_link)


