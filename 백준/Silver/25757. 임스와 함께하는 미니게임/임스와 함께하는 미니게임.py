# 임스와 함께하는 미니게임
import sys
input = sys.stdin.readline

n, g = input().rstrip().split()

game =  {
    "Y" : 2,
    "F" : 3,
    "O" : 4
    }

member = set()
for i in range(int(n)):
    member.add(input().rstrip())

print(len(member)//(game[g]-1))