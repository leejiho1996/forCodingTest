# 부품 대여장
import sys
input = sys.stdin.readline
from datetime import datetime

N, L, F = input().rstrip().split()

N = int(N)
F = int(F)

ddd = int(L[:3])
hh = int(L[4:6])
mm = int(L[7:9])

period = ddd * (24*60) + hh * 60 + mm

dic = {}
charge = {}
charged = False

for i in range(N):
    date, time, P, M = input().rstrip().split()
    y, m, d, = date.split("-")
    hh, mm = time.split(":")

    cur = datetime(int(y), int(m), int(d), int(hh), int(mm))

    if M not in dic:
        dic[M] = {}

    if M not in charge:
        charge[M] = 0
        
    if P in dic[M]:
        base = dic[M][P]
        minutes = int((cur - base).total_seconds() // 60)
        dic[M].pop(P)
        
        if minutes > period:
            charge[M] += (minutes - period) * F
            charged = True
    else:
        dic[M][P] = cur

keys = list(charge.keys())
keys.sort()

for i in keys:
    if charge[i] == 0:
        continue

    print(i, charge[i])

if not charged:
    print(-1)
