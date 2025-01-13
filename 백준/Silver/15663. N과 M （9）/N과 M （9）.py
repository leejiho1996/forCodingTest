# N과 M (9)
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
choice = [0] * n

def backTrack(seq, cnt):
    if cnt == m:
        print(seq)
        return

    prev = -1
    for i in range(n):
        if choice[i]:
            continue
        else:
            num = nums[i]
            choice[i] = 1
    
        if len(seq) == 0:
            nextSeq = str(num)
        else:
            nextSeq = seq + " " + str(num)

        if num != prev:
            prev = num
            backTrack(nextSeq, cnt+1)
        choice[i] = 0
        
backTrack("", 0)

