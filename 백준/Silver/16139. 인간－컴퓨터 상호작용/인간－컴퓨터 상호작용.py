# 인간-컴퓨터 상호작용
import sys
input = sys.stdin.readline

string = input().rstrip()
n = int(input())

alpha = 'abcdefghijklmnopqrstuvwxyz'

acc = [[0] * (len(string)+1) for _ in range(len(alpha))]

for i in range(len(alpha)):
    for j in range(len(string)):
        if alpha[i] == string[j]:
            acc[i][j] = acc[i][j-1]+1
        else:
            acc[i][j] = acc[i][j-1]

for i in range(n):
    char, start, end = input().rstrip().split()
    start = int(start)
    end = int(end)

    print(acc[alpha.index(char)][end] - acc[alpha.index(char)][start-1])
            
