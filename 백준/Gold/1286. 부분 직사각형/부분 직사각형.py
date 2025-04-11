# 부분 직사각형
import sys
input = sys.stdin.readline

dic = {}

for i in range(26):
    dic[chr(65+i)] = 0

N, M = map(int,input().split())
N2 = 2*N
M2 = 2*M

for i in range(N):
    word = input().rstrip()
    for j in range(M):
        c = word[j]
        dic[c] += (i+1-0) * (j+1-0) * (N2-i) * (M2-j)
        
        for dr, dc in [(N,0), (0, M), (N, M)]:
            nr, nc = i+dr, j+dc
            dic[c] += (nr+1-0) * (nc+1-0) * (N2-nr) * (M2-nc)
        
for i in range(26):
    print(dic[chr(65+i)])
