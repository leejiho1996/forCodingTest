#Facebook2
import sys
input = sys.stdin.readline

N = int(input())
links = []

for i in range(N):
    links.append(input().rstrip())

# Q입력
Q = int(input())

for i in range(Q):
    a, b = map(int,input().split())

    print((int(links[a-1], 2) & int(links[b-1], 2)).bit_count())
        
