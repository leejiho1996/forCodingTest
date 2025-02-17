nums = []
minn = 1000000000
total = 0
for i in range(7):
    cur = int(input())
    if cur % 2:
        total += cur
        minn = min(minn, cur)

if minn == 1000000000:
    print(-1)
else:
    print(total)
    print(minn)