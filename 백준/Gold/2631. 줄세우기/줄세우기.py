import sys
input = sys.stdin.readline

n = int(input())

lis = []
for i in range(n):
    num = int(input())
    start = 0
    end = len(lis) - 1

    if end == -1:
        lis.append(num)
        continue

    if lis[-1] < num:
        lis.append(num)
        continue
    
    while start <= end:
        mid = (start + end) // 2
        if lis[mid] >= num:
            end = mid - 1
        else:
            start = mid + 1

    if start >= len(lis):
        lis.append(num)
    else:
        lis[start] = num

print(n - len(lis))
