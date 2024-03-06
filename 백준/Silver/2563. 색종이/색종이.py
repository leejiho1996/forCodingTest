#색종이

paper = [[0 for _ in range(100)] for _ in range(100)]

a = int(input())
cnt = 0
for i in range(a):
    x, y = map(int,input().split())
    for j in range(10):
        for k in range(10):
            paper[x+j][y+k] = 1

for i in paper:
    for j in i:
        if j == 1:
            cnt += 1

print(cnt)