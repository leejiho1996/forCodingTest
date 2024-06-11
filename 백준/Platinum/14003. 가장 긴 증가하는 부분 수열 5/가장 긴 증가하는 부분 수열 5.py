# 가장 긴 증가하는 부분 수열 5
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))

dp = []
seq = [1 for _ in range(n)]
max_seq = []

for i in range(n):
    number = num[i]

    if i == 0:
        dp.append(number)
        continue
    
    if dp[-1] < number:
        dp.append(number)
        seq[i] = len(dp)
        continue
    
    head = 0
    tail = len(dp)-1
    
    while head <= tail:
        mid = (head + tail) // 2

        if number <= dp[mid]:
            tail = mid - 1 
        else:
            head = mid + 1

    dp[tail+1] = number
    seq[i] = tail+2

max_len = len(dp)
print(max_len)

result = []

for i in range(n-1, -1, -1):
    if seq[i] == max_len:
        result.append(num[i])
        max_len -= 1

print(*result[::-1])
