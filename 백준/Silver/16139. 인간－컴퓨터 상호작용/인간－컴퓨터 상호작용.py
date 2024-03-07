# 인간-컴퓨터 상호작용
import sys
input = sys.stdin.readline

string = input().rstrip()
n = int(input())

s = ''
acc = []

for i in range(len(string)):
    s += string[i]
    acc.append(s)

for i in range(n):
    a, start, end = input().rstrip().split()
    print(string[int(start):int(end)+1].count(a))
    
