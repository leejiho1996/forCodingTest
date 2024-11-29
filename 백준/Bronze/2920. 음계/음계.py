import sys
input = sys.stdin.readline

dic = {(1,2,3,4,5,6,7,8):"ascending", (8,7,6,5,4,3,2,1) : "descending"}

cur = tuple(map(int,input().split()))

if cur in dic:
    print(dic[cur])
else:
    print("mixed")
