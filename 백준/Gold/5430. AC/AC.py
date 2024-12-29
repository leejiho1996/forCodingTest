# AC
import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

for i in range(t):
    function = input().rstrip()
    length = int(input())
    tmp = input().rstrip()
    que = deque(tmp[1:len(tmp)-1].split(","))

    isReverse = 0
    result = ""
    
    for j in function:
        if j == "R":
            isReverse = 1 - isReverse
        elif j == "D":
            if length == 0:
                result = "error"
                break
            elif isReverse:
                que.pop()
            else:
                que.popleft()

            length -= 1
    
    if result == "error":
        print(result)
    else:
        result = list(que)
        if isReverse:
            result = result[::-1]
        result = ",".join(result)
        
        print("[", end="")
        print(result, end="")
        print("]")