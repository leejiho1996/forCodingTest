# ATM

a = int(input())

time = list(map(int,input().split()))

time.sort()

total = 0
acc = 0

for i in time:
    acc += i
    total += acc

print(total)
