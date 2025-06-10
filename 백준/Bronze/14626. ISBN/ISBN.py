# ISBN
import sys
input = sys.stdin.readline

ISBN = input().rstrip()

total = int(ISBN[-1])

for i in range(12):

    if ISBN[i] == "*":
        loss = i
        continue

    if i % 2 :
        total += 3 * int(ISBN[i])
    else:
        total += int(ISBN[i])

target = (10 - total % 10) % 10

if loss % 2:
    weight = 3
else:
    weight = 1

for i in range(10):

    if i * weight % 10 == target:
        print(i)
        break
