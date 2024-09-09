import sys
input = sys.stdin.readline

n = input().rstrip()

result = [n[0]]
for i in range(len(n)):
    if n[i] == "-":
        result.append(n[i+1])
print(*result, sep="")
