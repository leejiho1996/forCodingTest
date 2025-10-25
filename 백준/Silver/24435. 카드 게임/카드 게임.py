# 카드 게임
import sys
input = sys.stdin.readline

def backtrack(S, minn):

    global result
    
    if S and int(S) < minn:
        result = max(result, int(S))
    
    for i in range(N):
        if visited[i]:
            continue

        visited[i] = 1
        backtrack(S+Alice[i], minn)
        visited[i] = 0

T = int(input())

for i in range(T):
    N = int(input())

    Bob = input().rstrip()
    Alice = input().rstrip()

    minn = min(int(Bob), int(Bob[::-1]))

    visited = [0] * N
    result = -1

    backtrack("", minn)

    print(result)
