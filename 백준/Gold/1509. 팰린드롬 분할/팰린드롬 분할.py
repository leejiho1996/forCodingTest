import sys
input = sys.stdin.readline

word = list(input().rstrip())
n = len(word) # word의 길이 n
pel = [[0] * (n) for _ in range(n)] # 펠린드롬 여부 체크 ex)pel[1][4] 첫번째 부터 4번째까지의 문자가 펠린드롬인지 확인

for i in range(n):
    for j in range(0, n-i):
        start = j
        end = j + i

        if end - start == 0:
            pel[start][end] = 1
            continue
        
        if word[start] == word[end]:
            if end - start == 1 or pel[start+1][end-1] == 1:
                pel[start][end] = 1

dp = [2501] * (n+1)
dp[-1] = 0

for i in range(n):
    for j in range(i+1):
        if pel[j][i] == 1:
            dp[i] = min(dp[i], dp[j-1] + 1)
        else:
            dp[i] = min(dp[i], dp[i-1] + 1)

print(dp[n-1])