# 소트
import sys
sys.stdin.readline

n = int(input())
elements = list(map(int,input().split()))
s = int(input())

def swap(idx, target):
    for i in range(idx, target, -1):
        tmp = elements[i]
        elements[i] = elements[i-1]
        elements[i-1] = tmp
        
for i in range(n):
    end = min(i+s, n-1)
    start = i

    for j in range(i+1, end+1):
        if elements[start] < elements[j]:
            start = j

    s -= (start-i)
    swap(start, i)
        
print(*elements)
