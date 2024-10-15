# 친구
import sys
input = sys.stdin.readline

n = int(input())

friends = ["0"] * n

for i in range(n):
    friends[i] = input().rstrip()    

count_friends = [0] * n

for i in range(n):
    cnt = 0
    visited = [0] * n
    for j in range(n):
        if friends[i][j] != "Y":
            continue
        cnt += 1
        for k in range(n):
            if k == i or visited[k]:
                continue
            if friends[j][k] == "Y" and friends[i][k] =="N" :
                visited[k] = 1
                cnt += 1

    count_friends[i] = cnt

print(max(count_friends))
