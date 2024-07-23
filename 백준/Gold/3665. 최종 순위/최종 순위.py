import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input()) # 팀의 수 n
    rank = list(map(int,input().split())) # 작년순위
    front = [0 for _ in range(n+1)]
    back = [{} for _ in range(n+1)]
    rank_dic = {}

    for i, v in enumerate(rank):
        front[v] = i
        back[v] = set(rank[i+1:].copy())
        rank_dic[v] = i 

    m = int(input()) # 상대적인 등수가 바뀐 수
    
    for j in range(m):
        a, b = map(int, input().split())
        if rank_dic[a] < rank_dic[b]:
            back[a].remove(b)
            front[a] += 1
            front[b] -= 1
            back[b].add(a)
        else:
            back[b].remove(a)
            front[b] += 1
            front[a] -= 1
            back[a].add(b)

    stack = []
    sequence = []
    for j in range(1, n+1):
        if front[j] == 0:
            stack.append(j)
            sequence.append(j)

    while stack:
        num = stack.pop()
        for j in back[num]:
            front[j] -= 1
            if front[j] == 0:
                stack.append(j)
                sequence.append(j)
    
    if len(sequence) == n:
        print(*sequence)
    else:
        print("IMPOSSIBLE")

