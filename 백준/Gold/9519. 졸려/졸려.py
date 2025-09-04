# 졸려
import sys
input = sys.stdin.readline

N = int(input())
word = input().rstrip()
length = len(word)

cycle = [[i for i in range(1, length+1)]]
half = (length+1) // 2 - 1

while True:
    cur = [0] * length     
    prev = cycle[-1]
    
    cur[0] = 1
    cur[-1] = prev[length-half-1]
    
    for i in range(half):
        cur[i*2+2] = prev[i+1]
        cur[i*2+1] = prev[length-1-i]

    if cur == cycle[0]:
        break
    else:
        cycle.append(cur)

order = N % len(cycle)
result = ['0'] * length

for i in range(length):
    result[cycle[order][i]-1] = word[i]

print("".join(result))
