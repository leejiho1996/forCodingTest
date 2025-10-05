# 미국스타일
import sys
input = sys.stdin.readline

dic = {"kg": 2.2046, "lb": 0.4536, "l" : 0.2642, "g" : 3.7854}
unit = {"kg": "lb", "lb":"kg", "l":"g", "g":"l"}

N = int(input())
for i in range(N):
    n, s = input().rstrip().split()
    result = float(n) * dic[s]
    
    print(f'{result:.4f}', unit[s])