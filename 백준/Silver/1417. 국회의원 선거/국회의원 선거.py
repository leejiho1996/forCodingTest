# 국회의원 선거
import sys
input = sys.stdin.readline

N = int(input())
votes = []

for i in range(N):
    votes.append(int(input()))

cnt = 0

while True:
    maxx = max(votes)
    max_idx = votes.index(maxx)

    if max_idx == 0:
        check = True
        
        for i in range(1, N):
            if votes[i] == maxx:
                check = False
                idx = i
                break

        if check:
            print(cnt)
            break
        else:
            votes[idx] -= 1
            votes[0] += 1
            cnt += 1
            continue

    votes[max_idx] -= 1
    votes[0] += 1
    cnt += 1

