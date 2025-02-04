# 사전 순 최대 공통부분 순열
import sys
input = sys.stdin.readline

a = int(input())
a_list = list(map(int,input().split()))

b = int(input())
b_list = list(map(int,input().split()))

result = []
while True:
    sort_list = sorted(a_list, reverse=True)

    max_num = -1
    
    for i in sort_list:
        if i in b_list:
            max_num = i 
            break

    if max_num == -1:
        break

    result.append(max_num)
    a_idx = a_list.index(max_num)
    b_idx = b_list.index(max_num)
        
    a_list = a_list[a_idx+1:]
    b_list = b_list[b_idx+1:]

if len(result) == 0:
    print(0)
else:
    print(len(result))
    print(*result)
