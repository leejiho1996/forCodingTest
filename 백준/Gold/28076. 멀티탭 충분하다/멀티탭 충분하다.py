# 멀티탭 충분하다
import sys
input = sys.stdin.readline

N = int(input())
tabs = [0] + list(map(int,input().split()))

tabs.sort()
total = tabs[-1]

if N == 1:
    print(total)
    exit()
elif N == 2:
    print(total + tabs[1] - 1)
    exit()

div = N // 3 

if N % 3 == 1 or N % 3 == 0:
    print(tabs[div] + tabs[2*div] + total - 3)
else:
    print(tabs[div] + tabs[2*div+1] + total - 3)
