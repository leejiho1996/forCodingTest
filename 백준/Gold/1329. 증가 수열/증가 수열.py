import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

S = input().rstrip()
N = len(S)
best_last = None
best_seq = None

def seq_better(a, b):
    for x, y in zip(a, b):
        xi = int(x); yi = int(y)
        if xi != yi:
            return xi > yi
    return len(a) > len(b)

def dfs(start, seq, prev_int):
    global best_last, best_seq
    if start == N:
        last_int = prev_int
        if best_last is None:
            best_last = last_int
            best_seq = seq.copy()
        else:
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
        if prev_int is None or cur > prev_int:
            if best_last is not None and cur > best_last:
                break
            seq.append(part)
            dfs(i, seq, cur)
            seq.pop()

dfs(0, [], None)

if best_seq is None:
    print(S)
else:
    print(",".join(best_seq))
