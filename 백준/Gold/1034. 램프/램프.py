# 램프
import sys
input = sys.stdin.readline

N, M = map(int,input().split())
dic = {}
result = 0

for i in range(N):
    row = input().rstrip()

    if row not in dic:
        dic[row] = 1
    else:
        dic[row] += 1

K = int(input())

for row in dic.keys():

    if row.count('0') <= K and (K - row.count('0')) % 2 == 0:
        result = max(result, dic[row])
        
print(result)
