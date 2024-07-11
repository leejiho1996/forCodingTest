import sys

#input = sys.stdin.readline
N = int(input(), 8) # 8진수로 입력받음
ans = bin(N)[2:] # 2진수로 변환
print(ans)