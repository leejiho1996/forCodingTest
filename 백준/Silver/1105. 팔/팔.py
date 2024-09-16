import sys
input = sys.stdin.readline

l, r = input().rstrip().split()

if len(l) != len(r):
    print(0)
    exit()

cnt = 0

for i in range(len(l)):
    if l[i] == "8" and r[i] == "8":
        cnt += 1
    elif l[i] != r[i]:
        break
        
print(cnt)
