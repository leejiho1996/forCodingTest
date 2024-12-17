import sys
sys.setrecursionlimit(1000000)

costs = [[0] * (10) for _ in range(10)] # cost[i][j] -> 숫자자판 i 에서 j로 이동하는데 소요되는 가중치

numberPad = {
    1: (0, 0), 2: (0, 1), 3: (0,2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2), 
    0: (3, 1)}

for i in range(10):
    r1, c1 = numberPad[i]
    for j in range(10):
        total = 0
        if i == j:
            costs[i][j] = 1
            continue
            
        r2, c2 = numberPad[j]
        oppo = (min(abs(r1 - r2), abs(c1 - c2))) # 대각 이동 횟수
        if r1 != r2 and c1 != c2:
            total += 3 * oppo
            total += 2 * (abs(r1 - r2) + abs(c1 - c2) - oppo*2)
        else:
            total += 2 * (abs(r1 - r2) + abs(c1 - c2))
        
        costs[i][j] = total

def dfs(dp, k, i, j):
    if k >= len(number):
        return 0
    
    if dp[k][i][j] != -1:
        return dp[k][i][j]
    
    num = int(number[k])
    result = float('inf')
    
    if j != num:
        result = min(result, dfs(dp, k+1, num, j) + costs[i][num])
    
    if i != num:
        result = min(result, dfs(dp, k+1, i, num) + costs[j][num])
        
    dp[k][i][j] = result
    
    return dp[k][i][j]
    

number = ""
def solution(numbers):
    global number
    length = len(numbers)
    number = numbers
    # dp[k][i][j] -> k번째 수를 탐색할때 왼손이 i번, 오른손이 j번에 있을 때 시작하여 마지막까지 확인했을 경우 최소 가중치 
    dp = [[[-1] * 10 for _ in range(10)] for _ in range(length)]
    
    return dfs(dp, 0, 4, 6)
    