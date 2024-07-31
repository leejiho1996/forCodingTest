# 경찰차 이중 for
def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def solve(n, w, events):
    dp = [[float('inf')] * (w + 1) for _ in range(w + 1)]
    dp[0][0] = 0
    trace = [[(-1, -1)] * (w + 1) for _ in range(w + 1)]
    
    for i in range(w + 1):
        for j in range(w + 1):
            next_event = max(i, j) + 1
            if next_event > w:
                continue
            
            event_pos = events[next_event]
            if i == 0:
                car1_pos = (1, 1)
            else:
                car1_pos = events[i]
            if j == 0:
                car2_pos = (n, n)
            else:
                car2_pos = events[j]

            new_dist_car1 = dp[i][j] + distance(car1_pos[0], car1_pos[1], event_pos[0], event_pos[1])
            new_dist_car2 = dp[i][j] + distance(car2_pos[0], car2_pos[1], event_pos[0], event_pos[1])
            
            if new_dist_car1 < dp[next_event][j]:
                dp[next_event][j] = new_dist_car1
                trace[next_event][j] = (i, j)
            if new_dist_car2 < dp[i][next_event]:
                dp[i][next_event] = new_dist_car2
                trace[i][next_event] = (i, j)
    
    result = float('inf')
    last_i, last_j = -1, -1
    for i in range(w + 1):
        if dp[w][i] < result:
            result = dp[w][i]
            last_i, last_j = w, i
        if dp[i][w] < result:
            result = dp[i][w]
            last_i, last_j = i, w
    
    # 경로 추적
    path = []
    x, y = last_i, last_j
    while trace[x][y] != (-1, -1):
        px, py = trace[x][y]
        if px == x:
            path.append(2)
        else:
            path.append(1)
        x, y = px, py
    
    path.reverse()
    return result, path

# 입력 처리
import sys
input = sys.stdin.read
data = input().strip().split()
index = 0

n = int(data[index])
index += 1
w = int(data[index])
index += 1

events = [(0, 0)] * (w + 1)
for i in range(1, w + 1):
    x = int(data[index])
    index += 1
    y = int(data[index])
    index += 1
    events[i] = (x, y)

# 문제 해결 및 결과 출력
result, path = solve(n, w, events)
print(result)
for p in path:
    print(p)
