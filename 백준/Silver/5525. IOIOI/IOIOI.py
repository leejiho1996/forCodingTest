# IOIOI
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
length = 2 * n + 1
string = input().rstrip()
cnt = 0

tmp = []
for i in range(m):
    cur = string[i]
    if len(tmp) == 0 and cur == "O":
        continue
    elif len(tmp) == 0:
        tmp.append("I")
        continue
    
    if tmp[-1] == cur:
        if len(tmp) >= length:
            cnt += (len(tmp) - length) // 2 + 1 

        if cur == "I":
            tmp = ["I"]
        else:
            tmp = []
        continue
    
    else:
        tmp.append(cur)

if len(tmp) >= length:
    cnt += (len(tmp) - length) // 2 + 1
    
print(cnt)
