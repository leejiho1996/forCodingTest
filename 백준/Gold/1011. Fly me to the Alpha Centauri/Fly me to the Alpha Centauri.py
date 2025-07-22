# Fly me to the Alpha Centauri
import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    start, to = map(int,input().split())

    to = to - start
    start = 0
    
    if to - start <= 3:
        print(to - start)
        continue

    speed = int(to**0.5)
    rest = to - speed**2
    
    if rest % speed:
        print(2*speed + rest // speed)
    else:
        print(2*speed - 1 + rest // speed)
