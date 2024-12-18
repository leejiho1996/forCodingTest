import sys
input = sys.stdin.readline

n = int(input())
word = input().rstrip()
MOD = 1234567891
total = 0
for i in range(n):
    total += ((ord(word[i]) - ord('a') + 1) * 31**i) % MOD
print(total % MOD)
    
