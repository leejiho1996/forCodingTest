# 가장 긴 증가하는 부분 수열2
import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))

arr = [0]

for i in num:
    if i > arr[-1]:
        arr.append(i)
    else:
        start = 1
        end = len(arr)-1

        while start <= end:
            mid = (start+end) // 2

            if arr[mid] >= i :
                end = mid - 1
            else:
                start = mid + 1

        arr[end+1] = i

print(len(arr)-1)