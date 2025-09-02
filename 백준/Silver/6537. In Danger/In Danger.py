# In Danger
import sys
input = sys.stdin.readline

def solve(num):

    p = 1
    while p <= num:
        p *= 2

    return (2 * num) - p + 1
        
while True:
    cur = input().rstrip()

    if cur == "00e0":
        break

    num = int(cur[0:2]) * 10**(int(cur[-1]))
    
    print(solve(num))
