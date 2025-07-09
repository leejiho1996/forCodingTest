# 팰린드롬 공장
import sys
input = sys.stdin.readline

def solve():
    for i in range(length):
        for j in range(length-i):
            start = j
            end = j + i

            if start == end: # 글자가 1개인 경우는 무조건 펠린드롬
                continue

            if word[start] == word[end]: # 양끝 글자가 같은지 확인
                diff = 0
            else:
                diff = 1
                
            if start - end == 1: # 글자가 두 개고, 양 끝 글자가 다르다면 1
                dp[start][end] = diff
                continue

            dp[start][end] = min(dp[start][end-1] + 1, # 오른쪽 글자 제거
                                 dp[start+1][end] + 1, # 왼쪽 글자 제거
                                 dp[start+1][end-1] + diff) # 양옆의 글자를 똑같이 해줌

    return dp[0][length-1]

word = list(input().rstrip())
length = len(word)
# dp[i][j] => word[i:j]의 글자를 펠린드롬으로 만들기 위한 최소 변경 횟수
dp = [[0] * length for _ in range(length)]

result = solve() # 문자 교환을 한 번도 하지 않은 경우

# 문자 교환을 하는 모든 경우의 수에 대해 확인
for i in range(length):
    for j in range(i+1, length):
        word[i], word[j] = word[j], word[i]
        result = min(result, solve()+1) # 문자를 바꾼 뒤 다시 횟수 계산
        word[i], word[j] = word[j], word[i]
        
print(result)
