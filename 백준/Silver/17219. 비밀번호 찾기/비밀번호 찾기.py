import sys
input = sys.stdin.readline

dic = {}
n, m = map(int,input().split())

for i in range(n):
    word, pwd = input().rstrip().split()
    dic[word] = pwd

for i in range(m):
    print(dic[input().rstrip()])