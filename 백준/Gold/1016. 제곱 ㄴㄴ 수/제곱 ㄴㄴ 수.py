# 제곱 ㄴㄴ 수
import sys
input = sys.stdin.readline

minn, maxx = map(int,input().split())
result = 0
cnt = maxx - minn + 1 # 숫자의 갯수
visited = [0] * cnt

cur = 2
sqr = 4 # 4부터 시작
while sqr <= maxx: # 현재의 제곱수가 최댓값보다 작을때까지 반복

    # 최솟값이 현재 제곱수로 나누어떨어지면 최솟값(0번 인덱스)부터 시작
    if minn % sqr == 0: 
        start = 0
    else:  # 그렇지 않다면 시작 인덱스 계산
        start = sqr * (minn // sqr + 1) - minn
    # 시작인덱스부터 현재 제곱수 간격으로 체크해준다
    for i in range(start, cnt, sqr):
        visited[i] = 1

    cur += 1
    sqr = cur**2

# 제곱 ㄴㄴ수 계산
for i in range(cnt):
    if visited[i] == 0:
        result += 1
    
print(result)
