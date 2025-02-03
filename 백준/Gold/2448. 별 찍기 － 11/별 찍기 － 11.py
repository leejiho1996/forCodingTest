# 별 찍기 - 11
import sys
input = sys.stdin.readline
import math

def tri(cnt, n):
    if n > logN:
        return

    if n == 0:
        for i in base:
            blank = cnt * " "
            print(blank + i + blank, sep="")
            cnt -= 1
    else:
        length = len(base)
        start = len(base[-1])
        for i in range(length):
            base.append(base[i] + " " * start + base[i])
            start -= 2

        for i in range(length, len(base)):
            blank = cnt * " "
            print(blank + base[i] + blank, sep="")
            cnt -= 1
            
    tri(cnt, n+1)


n = int(input())
logN = int(math.log(n//3, 2))
base = ["*", "* *", "*****"]

tri(n-1, 0)
