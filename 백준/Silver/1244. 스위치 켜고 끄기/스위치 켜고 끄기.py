# 스위치 켜고 끄기
import sys
input = sys.stdin.readline

n = int(input())
switch = [0] + list(map(int,input().split()))
s = int(input())

for i in range(s):
    g, num = map(int,input().split())

    if g == 1:
        for j in range(num, n+1, num):
            switch[j] = 1 - switch[j]
    else:
        start = num-1
        end = num+1
        switch[num] = 1 - switch[num]
        
        while start >= 1 and end <= n:
            if switch[start] == switch[end]:
                switch[start] = 1 - switch[start]
                switch[end] = 1 - switch[end]
            else:
                break

            start -= 1
            end += 1

for i in range(1, n+1):
    print(switch[i], end = " ")

    if i % 20 == 0:
        print()
