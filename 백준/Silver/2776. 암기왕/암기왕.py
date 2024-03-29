# 암기왕
import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n1 = int(input())
    note1 = set(list(map(int,input().split())))

    n2 = int(input())

    for j in list(map(int,input().split())):
        if j in note1:
            print(1)
        else:
            print(0)
