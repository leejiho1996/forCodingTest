# 단어 나누기
import sys
input = sys.stdin.readline

word = list(input().rstrip())
length = len(word)
result = []

for i in range(1, length):
    for j in range(i+1, length):        
        p1 = word[0:i]
        p2 = word[i:j]
        p3 = word[j:]

        p1 = p1[::-1]
        p2 = p2[::-1]
        p3 = p3[::-1]

        result.append("".join(p1) + "".join(p2) + "".join(p3))

result.sort()

print(result[0])
