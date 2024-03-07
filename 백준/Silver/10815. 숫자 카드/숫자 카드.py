# 숫자 카드

a = int(input())

s = list(map(int,input().split()))

b = int(input())

c = list(map(int,input().split()))


arr = [0] * 20000001

for i in s:
    arr[i+10000000] = 1

for i in c:
    print(arr[i+10000000], end = ' ')