# 성냥개비
import sys
input = sys.stdin.readline

mat = {2:1, 3:7, 4:4, 5:2, 6:0, 7:8} # 만들수 있는 최소 수
maxx = 7

t = int(input())

dp = [float('inf')] * 101

for i in range(2, 101):
    if i in mat:
        dp[i] = mat[i]
        continue

    for k in range(2, i//2 + 1):
        num1 = str(dp[k]) + str(dp[i-k])
        num2 = str(dp[i-k]) + str(dp[k])
        
        if num1[0] == "0":
            num1 = "6" + num1[1:]

        if num2[0] == "0":
            num2 = "6" + num2[1:]
   
        dp[i] = min(dp[i], int(num1), int(num2))
        
for i in range(t):
    n = int(input())

    if n == 6:
        print(6, end=' ')
    else:
        print(dp[n], end=" ")
    
    mx = ""
    cur = n

    if cur % 2 == 1:
        mx += str(mat[3])
        cur -= 3
        mx += '1' * (cur // 2)
    else:
        mx += '1' * (cur // 2)

    print(mx)
