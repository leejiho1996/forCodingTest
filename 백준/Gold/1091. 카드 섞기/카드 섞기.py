# 카드 섞기
import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))
s = list(map(int,input().split()))

origin = p.copy()
target = [0, 1, 2] * (n // 3) # target은 [0, 1, 2]의 순서로 반복되는 리스트

tmp = [0] * n # 카드를 섞은뒤 결과를 담을 리스트 
cnt = 0
while True:
    if target == p:
        break
    
    cnt += 1
    for i in range(n):
            tmp[s[i]] = p[i]

    p = tmp.copy() # copy를 하지 않으면 같은 리스트를 참조해서 문제 발생

    if origin == tmp:
        cnt = -1
        break
    
print(cnt)
 