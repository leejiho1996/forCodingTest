# LCS2
import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

dp = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]

for i in range(len(s2)):
    c = s2[i]
    for j in range(len(s1)):
        if c == s1[j]:
            dp[i][j] = max(dp[i-1][j-1] + 1, dp[i-1][j])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[len(s2)-1][len(s1)-1])