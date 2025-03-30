import sys
from itertools import permutations
input = sys.stdin.readline

def calc_min_dist(topping, start, end):
    min_total = float('inf')
    for order in permutations(topping, 3):
        total = 0
        r, c = start
        for tr, tc in order:
            total += abs(r - tr) + abs(c - tc)
            r, c = tr, tc
        total += abs(r - end[0]) + abs(c - end[1])
        min_total = min(min_total, total)
    return min_total

N = int(input())
J, C, B, W = [], [], [], []
home, end = None, None

for i in range(N):
    row = input().strip()
    for j in range(N):
        if row[j] == 'H':
            home = (i, j)
        elif row[j] == '#':
            end = (i, j)
        elif row[j] == 'J':
            J.append((i, j))
        elif row[j] == 'C':
            C.append((i, j))
        elif row[j] == 'B':
            B.append((i, j))
        elif row[j] == 'W':
            W.append((i, j))

results = [
    (calc_min_dist(J, home, end), "Assassin"),
    (calc_min_dist(C, home, end), "Healer"),
    (calc_min_dist(B, home, end), "Mage"),
    (calc_min_dist(W, home, end), "Tanker"),
]

# 우선순위 고려해서 최소 거리 찾기
print(min(results, key=lambda x: (x[0], ["Assassin", "Healer", "Mage", "Tanker"].index(x[1])))[1])
