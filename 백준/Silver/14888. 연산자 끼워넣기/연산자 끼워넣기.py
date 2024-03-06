# 연산자 끼워넣기 (최적)
import sys
input = sys.stdin.readline

number = int(input())
num = list(map(int,input().split()))

operator = list(map(int,input().split()))

maxx = -1_000_000_000
minn = 1_000_000_000

def cal(count, s):
    global minn
    global maxx
    
    if count == number - 1:
        minn = min(minn, s)
        maxx = max(maxx, s)
        return

    if operator[0]:
        operator[0] -= 1
        cal(count+1, s+num[count+1])
        operator[0] += 1

    if operator[1]:
        operator[1] -= 1
        cal(count+1, s-num[count+1])
        operator[1] += 1

    if operator[2]:
        operator[2] -= 1
        cal(count+1, s*num[count+1])
        operator[2] += 1

    if operator[3]:
        operator[3] -= 1
        if s >= 0:
            cal(count+1, s//num[count+1])
        else:
            cal(count+1, -(abs(s)//num[count+1]))
        operator[3] += 1

cal(0, num[0])

print(maxx)
print(minn)