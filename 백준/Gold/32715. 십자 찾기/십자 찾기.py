import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    K = int(input())
    L = 2 * K + 1
    arr = [list(map(int, input().split())) for _ in range(N)]
    if K == 0:
        cnt = sum(sum(line)for line in arr)
        print(cnt)
        return
    vert = [arr[0]] + [[0] * M for _ in range(N-1)]
    horz = [[0] * M for _ in range(N)]
    cnt = 0
    for row in range(1, N):
        for col in range(M):
            if arr[row][col] == 0:
                continue
            vert[row][col] = vert[row - 1][col] + 1
            if col > 0:
                horz[row][col] = horz[row][col - 1] + 1
            else:
                horz[row][col] = 1

            if vert[row][col] >= L:
                if col + K < M:
                    nr, nc = row - K, col + K
                    if horz[nr][nc] >= L:
                        cnt += 1
    print(cnt)

solve()