# 문서 검색
import sys
input = sys.stdin.readline

D = input().rstrip()
S = input().rstrip()
len_S = len(S)
block = [0] * len(D)

res = 0

for i in range(len(D)):
    if block[i]:
        continue
    
    if D[i:i+len_S] == S:
        res += 1
        
        for j in range(i, i+len_S):
            block[j] = 1
            
print(res)
