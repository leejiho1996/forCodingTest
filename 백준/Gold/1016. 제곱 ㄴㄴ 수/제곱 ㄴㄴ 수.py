# 제곱 ㄴㄴ 수
import sys
input = sys.stdin.readline

minn, maxx = map(int,input().split())
dic = {}
result = 0

for i in range(minn, maxx+1):
    dic[i] = 0

cur = 2
while cur**2 <= maxx:

    sqr = cur**2

    if minn % sqr == 0:
        start = minn
    else:
        start = sqr * (minn // sqr + 1)

    for i in range(start, maxx+1, sqr):
        dic[i] = 1

    cur += 1

for i in range(minn, maxx+1):
    if dic[i] == 0:
        result += 1
    
print(result)
