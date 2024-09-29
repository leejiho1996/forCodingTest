import sys
input = sys.stdin.readline
N, M = map(int, input().split())
securities = [input() for _ in range(N)] # 입력
row = set() # 경비원이 있는 행을 저장하는 집합
col = set() # 경비원이 있는 열을 저장하는 집합
for i in range(N):
    for j in range(M):
        if securities[i][j] == 'X': # 경비원이 있는 곳의 열과 행을 집합에 추가
            col.add(i)
            row.add(j)
print(max(N - len(col), M - len(row))) # 경비원이 없는 열과 행의 가수 중 큰 값 출력