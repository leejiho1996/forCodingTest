import sys
input = sys.stdin.readline

S = input().rstrip()
N = len(S)
best_last = float('inf')
best_seq = []

def seq_better(a, b):

    for x, y in zip(a, b):
        xi = int(x); yi = int(y)

        if xi != yi:
            return xi > yi

def dfs(start, seq, prev_int):

    global best_last, best_seq

    if start == N:
        last_int = prev_int
        
        if last_int < best_last:
            best_last = last_int
            best_seq = seq.copy()
        elif last_int == best_last:
            if seq_better(seq, best_seq):
                best_seq = seq.copy()
        return

    for i in range(start+1, N+1):
        part = S[start:i]
        cur = int(part)

        if cur > prev_int:

            if cur > best_last:
                break

            seq.append(part)
            dfs(i, seq, cur)
            seq.pop()

dfs(0, [], -1)

if best_seq == -1:
    print(S)
else:
    print(",".join(best_seq))
