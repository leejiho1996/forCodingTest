# 단지번호 붙히기
import sys
input = sys.stdin.readline

n = int(input())

house = [list(input().rstrip()) for _ in range(n)]
result = []

def check(row, column):
    if row < 0 or column < 0 or row >= len(house) or column >= len(house[row]):
        return False
    return True

def village(row, column, cnt):
    if not check(row, column):
        return 
    
    if house[row][column] == "1":
        house[row][column] = "visited"
        result[cnt] += 1
    else:
        return 
    
    for x, y in [(0, -1), (0, 1), (-1,0), (1,0)]:
        village(row+x, column+y, cnt)

cnt = 0
for i in range(n):
    for j in range(n):
        if house[i][j] == "1":
            result.append(0)
            village(i, j, cnt)
            cnt += 1

print(cnt)
for i in sorted(result):
    print(i)