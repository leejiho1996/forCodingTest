# Chop Ahoy! Revisited!
import sys
input = sys.stdin.readline

def backtrack(s, e, prev):
    global cnt
    
    if s == e:
        cnt += 1
        return

    for i in range(s+1, e+1):

        num = agg[i] - agg[s]

        if num < prev:
            continue

        backtrack(i, e, num)

order = 1
while True:
    digit = input().rstrip()

    if digit == "bye":
        break

    N = len(digit)
    agg = [0] * (len(digit)+1)
    cnt = 0

    for i in range(N):
        agg[i+1] = agg[i] + int(digit[i])

    backtrack(0, N, -1)
    print(f'{order}. {cnt}')

    order += 1
