# 칵테일
import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def gcd(a, b):

    if a < b:
        a, b = b, a

    while b > 0:
        a, b = b, a % b

    return a

N = int(input())
amount = [1] * N
parent = list(range(N))

for _ in range(N - 1):
    a, b, p, q = map(int, input().split())
    pa, pb = find(a), find(b)

    # a 쪽을 p 비율로 맞추기 위한 최소공배수
    lcmA = p * amount[a] // gcd(p, amount[a])
    # 현재 칵테일 a를 p와 최소공배수로 맞추기 위해 곱해줘야 하는 수
    multiA = lcmA // amount[a]
    # q 값도 lcmA/p 만큼 커지므로
    nq = q * (lcmA // p)
    # b 쪽을 nq 비율로 맞추기 위한 최소공배수
    lcmB = nq * amount[b] // gcd(nq, amount[b])
    multiQ = lcmB // nq # nq 값을 최소공배수로 만들기 위해 곱해줘야 하는 수
    multiB = lcmB // amount[b] # 현재 칵테일 b를 nq와 최소공배수로 만들기위해 곱해줘야 하는 수

    for j in range(N):
        fj = find(j)
        if fj == pa: # a와 같은 부모를 가지는 칵테일을 계산
            amount[j] *= multiA * multiQ
        elif fj == pb: # b와 같은 부모를 가지는 칵테일을 계산
            amount[j] *= multiB

    # 부모를 통일해준다
    parent[pb] = pa

# 전체 칵테일을 최소공배수로 나눠 준다
g = amount[0]
for x in amount[1:]:
    g = gcd(g, x)

for i in range(N):
    amount[i] //= g

print(*amount)
