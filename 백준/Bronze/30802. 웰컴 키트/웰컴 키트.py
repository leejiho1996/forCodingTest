# 웰컴 키트
import sys
input = sys.stdin.readline

n = int(input())
sizes = list(map(int,input().split()))
t, p = map(int,input().split())

t_bundle = 0

for i in sizes:
    t_bundle += i // t

    if i % t > 0:
        t_bundle += 1

print(t_bundle)
print(n//p, n %p)
