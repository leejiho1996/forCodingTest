# N차원 여행
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

nums = list(map(int,input().split()))
move = input().rstrip()
visited = []

dic = {}

for i in range(M):
    dic[nums[i]] = 0

visited.append(dic.copy())

for i in range(M):
    cur = nums[i]
    
    if move[i] == "+":
        m = 1
    else:
        m = -1

    dic[cur] += m

    for j in visited:
        check = True
        
        for k in j.keys():
            if j[k] == dic[k]:
                continue
            else:
                check = False
                break

        if check:
            print(0)
            exit()
        
    visited.append(dic.copy())

print(1)
