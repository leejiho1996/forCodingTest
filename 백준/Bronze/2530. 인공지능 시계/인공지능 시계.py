import sys
input = sys.stdin.readline

total = 0
a, b, c = map(int,input().split())
d = int(input())
total += a * 3600 + b * 60 + c + d
 
print(total // 3600 % 24, total % 3600 // 60 % 60, total % 3600 % 60)