# 부분합 (투포인터)
import sys
input = sys.stdin.readline

n, s = map(int,input().split())

num = list(map(int,input().split()))
total = [0]
summ = 0

for i in num:
    summ += i
    total.append(summ) 

start = 0
end = 1

min_len = 100010

while start <= end and end <= n:
    check = total[end] - total[start]
    if check >= s:
        min_len = min(min_len, end - start)
        start += 1
    else:
        end += 1
    
if min_len == 100010:
    print(0)
else:
    print(min_len)