import sys
input = sys.stdin.readline

n = int(input())
cost = list(map(int,input().split()))
m = 0
y = 0

for i in cost:
    y += (i // 30 + 1) *10
    m += (i // 60 + 1 ) * 15
        
if m > y:
    print("Y", y)
elif m < y:
    print("M", m)
else:
    print("Y", "M", y)
