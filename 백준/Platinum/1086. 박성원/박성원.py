# 박성원
import sys
input = sys.stdin.readline

num_list = []
n = int(input())

for i in range(n):
    num_list.append(input().rstrip())

div = int(input())
num_len = []
div_list = []
ten_div = [0]

for i in num_list:
    num_len.append(len(i))
    div_list.append(int(i) % div)

dp = [[-1] * div for _ in range(2**n)]

ten = 10
for i in range(max(num_len)):
    ten_div.append(ten % div)
    ten *= 10
    
def gcd(a, b):
    if a < b:
        a, b = b, a
        
    while b != 0:
        a, b = b, a % b

    return a

def cal_remain(remain, idx):
    if remain == 0:
        return div_list[idx]
    
    return ((remain * (ten_div[num_len[idx]]) + (div_list[idx]))) % div

def dfs(visited, remain):
    
    if visited == (1 << n) - 1:
    
        if remain == 0:
            return 1
        else:
            return 0
    
    if dp[visited][remain] != -1:
        return dp[visited][remain]
    
    for i in range(n):
        if visited & 1 << i:
            continue
        
        if dp[visited][remain] == -1:
            dp[visited][remain] = 0
            
        dp[visited][remain] += dfs(visited | 1 << i, cal_remain(remain, i))

    return dp[visited][remain]

numerator = dfs(0, 0)

denominator = 1
for i in range(1, n+1):
    denominator *= i

gcd = gcd(numerator, denominator)

numerator //= gcd
denominator //= gcd

print(f'{numerator}/{denominator}')
