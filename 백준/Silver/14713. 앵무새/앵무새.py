# 앵무새
import sys
input = sys.stdin.readline

N = int(input())
order = set()
listenIdx = {}
sentences = []

for i in range(N):
    cur = input().rstrip()
    sentences.append(cur)
    cur = cur.split()
    
    for j in cur:
        order.add(j)
        
listen = input().rstrip().split()

for i, v in enumerate(listen):
    if v not in order:
        print("Impossible")
        exit()

    listenIdx[v] = i
    
for i in sentences:
    idx = -1
    cur = i.split()
    for j in cur:
        if j not in listenIdx or listenIdx[j] < idx:
            print("Impossible")
            exit()

        idx = listenIdx[j]

print("Possible")

# 없는 단어
# 순서가 올바르지 않은 문장
# 브루트 포스는 불가능
