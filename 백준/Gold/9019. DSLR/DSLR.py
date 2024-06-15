# DSLR
import sys
input = sys.stdin.readline
from collections import deque
import heapq

t = int(input())

def D(n):
    tmp = int(n) * 2
    if tmp > 9999:
        return tmp % 10000
    else:
        return tmp
    
def S(n):
    if n == 0:
        return 9999
    else:
        tmp = n
        return tmp-1

def L(n):
    tmp = (n % 1000 * 10) + (n // 1000)
    return int(tmp)

def R(n):
    tmp = (n % 10 * 1000) + (n // 10)
    return int(tmp)

for i in range(t):
    a, b = map(int, input().split())

    visited = [-1] * 10000
    command = ["no"] * 10000
    visited[a] = 100001
    
    que = deque([])
    que.append(a)
    
    while que:
        cur = que.popleft()

        if cur == b:
            break

        D_num = D(cur)
        if visited[D_num] == -1:
            visited[D_num] = cur
            que.append(D_num)
            command[D_num] = 'D'

        S_num = S(cur)
        if visited[S_num] == -1:
            visited[S_num] = cur
            que.append(S_num)
            command[S_num] = 'S'
            
        L_num = L(cur)
        if visited[L_num] == -1:
            visited[L_num] = cur
            que.append(L_num)
            command[L_num] = 'L'
            
        R_num = R(cur)
        if visited[R_num] == -1:
            visited[R_num] = cur
            que.append(R_num)
            command[R_num] = 'R'

    result = command[b]
    next_num = visited[b]

    while next_num != a:
        result += command[next_num]
        next_num = visited[next_num]

    print(result[::-1])
