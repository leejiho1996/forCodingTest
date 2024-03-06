import sys

input = sys.stdin.readline
n = int(input().strip())
m = n**2

chess = [0] * m
vertical = [0] * n
ldiagonal = [0] * (2 * n - 1)
rdiagonal = [0] * (2 * n - 1)

def queen(count, i):
    # 마지막 줄 이면 가능/불가능 체크
    if i // n == n - 1:
        if count == n: return 1
        else: return 0
    else:
        sum = 0
        for c in range(n):
            j = (i // n + 1) * n + c
            a, b = j // n, j % n
            # 수직, 대각선에 겹치는게 없다면, 그 자리에 두고 기록표에 체크함. 그리고 백트래킹을 위해 다시 원복
            if not (vertical[b] or ldiagonal[b - a + n - 1] or rdiagonal[a + b]):
                chess[i] = vertical[b] = ldiagonal[b - a + n - 1] = rdiagonal[a + b] = 1
                sum += queen(count + 1, j)
                chess[i] = vertical[b] = ldiagonal[b - a + n - 1] = rdiagonal[a + b] = 0
        return sum

print(queen(0, -1))
