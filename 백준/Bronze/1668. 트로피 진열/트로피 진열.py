import sys
n = int(input())
trophy = []
left = 0
right = 0
left_height = 0
right_height = 0
for _ in range(n):
    trophy.append(int(sys.stdin.readline().rstrip('\n')))


for i in range(n):
    if trophy[i] > left_height :
        left += 1
        left_height = trophy[i]
    if trophy[-1-i] > right_height:
        right += 1
        right_height = trophy[-1-i]

print(left)
print(right)