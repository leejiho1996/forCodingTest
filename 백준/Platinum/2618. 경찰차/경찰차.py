# 경찰차
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000001)

n = int(input()) # N*N 도로의 갯수
w = int(input()) # 사건의 갯수

w_list = [(0,0)]
seq = []

for i in range(w):
    a, b = map(int,input().split())
    w_list.append((a,b))

# 거리계산 함수
def cal_distance(x1, y1, x2, y2):
    x = abs(x1-x2)
    y = abs(y1-y2)
    return x + y

def cal_dp(i, j):
    
    if i == w or j == w: # 사건 갯수 w에 도달했다면 0을 리턴
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    # 다음 사건 
    next_w = max(i, j) + 1
  
    if i == 0:
        next_p1 = cal_distance(1, 1, w_list[next_w][0], w_list[next_w][1])
    else:
        next_p1 = cal_distance(w_list[i][0], w_list[i][1], w_list[next_w][0], w_list[next_w][1])

    if j == 0:
        next_p2 = cal_distance(n, n, w_list[next_w][0], w_list[next_w][1])
    else:
        next_p2 = cal_distance(w_list[j][0], w_list[j][1], w_list[next_w][0], w_list[next_w][1])

    dp[i][j] = min(cal_dp(next_w, j) + next_p1, cal_dp(i, next_w) + next_p2)
    
    return dp[i][j]

def cal_seq(i, j):
    if i == w or j == w:
        return

    next_w = max(i, j) + 1

    if i == 0:
        p1 = cal_distance(1, 1, w_list[next_w][0], w_list[next_w][1])
    else:
        p1 = cal_distance(w_list[i][0], w_list[i][1], w_list[next_w][0], w_list[next_w][1])

    if j == 0:
        p2 = cal_distance(n, n, w_list[next_w][0], w_list[next_w][1])
    else:
        p2 = cal_distance(w_list[j][0], w_list[j][1], w_list[next_w][0], w_list[next_w][1])

    if dp[next_w][j] + p1 > dp[i][next_w] + p2:
        print(2)
        cal_seq(i, next_w)
    else:
        print(1)
        cal_seq(next_w, j)

# 경찰차 좌표
p1 = [1,1]
p2 = [n, n]

# 최소거리dp
# dp[i][j]는 1번째 경찰차가 마지막으로 i번째 사건을 방문 2번째 경찰차가 마지막으로 j번째 사건을 방문 했을 때 남은 최소 거리 수
dp = [[-1]*(w+1) for _ in  range(w+1)]

# 사건이 맡겨진 경찰차 번호
p_num = [0] * (w)



print(cal_dp(0,0))
cal_seq(0,0)
