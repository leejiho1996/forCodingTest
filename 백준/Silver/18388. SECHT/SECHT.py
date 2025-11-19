# SECHT
import sys
input = sys.stdin.readline

key = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

sentence = list(input().rstrip().split())
result = []

for i in sentence:
    cur = ''
    for j in i:
        check = False
        for k in key:
            if j in k:
                cur += k[k.find(j)+1]
                check = True
                break

        if not check:
            cur += j

    result.append(cur)

print(*result)
