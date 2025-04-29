# 책 페이지
import sys
input = sys.stdin.readline

N = int(input())
strN = str(N)
length = len(strN)

num_cnt = [0] * 10
num_cnt[0] = 1
one_to_nine = 0
result = [0] * 10

if N < 10:
    for i in range(1, N+1):
        result[i] += 1

    print(*result)
    exit()

# 0갯수 계산
zero = int(strN[0:-1])

for i in range(1, length-1):
    if strN[i] == '0':
        zero += (int(strN[:i])-1) * 10**(length-i-1)
        zero += int(strN[i+1:])+1
    else:
        zero += int(strN[:i]) * 10**(length-i-1)

for i in range(1, 10):
    num_cnt[i] = num_cnt[i-1] * 10 + 10**i
    
for i in range(length-1):
    cur = int(strN[i])

    if cur == 0:
        continue
    
    result[cur] += int(strN[i+1:])+1
    one_to_nine += cur * num_cnt[length-i-2]
    
    for j in range(1, cur):
        result[j] += 10**(length-i-1)

for i  in range(1, int(strN[-1])+1):
    result[i] += 1

for i in range(1, 10):
    result[i] += one_to_nine

result[0] += zero
print(*result)
