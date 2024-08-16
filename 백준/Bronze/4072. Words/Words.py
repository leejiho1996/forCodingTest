import sys
input = sys.stdin.readline

while 1:
    arr = list(input().split())
    if arr[0] == "#":
        break
    for i in range(len(arr)):
        if(i==len(arr)-1):
            print(arr[i][::-1])
            break
        print(arr[i][::-1], end=" ")