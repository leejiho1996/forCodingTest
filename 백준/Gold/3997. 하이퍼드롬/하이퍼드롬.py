import sys
input = sys.stdin.readline

ALPHA = 26

n = int(input().strip())
s = input().strip()

vst = {}
vst[0] = 1

x = 0
ans = 0

for i in range(n):
    ch = s[i]

    if 'a' <= ch <= 'z':
        a = ord(ch) - ord('a')
    else:
        a = ord(ch) - ord('A') + ALPHA

    x ^= (1 << a)

    if x in vst:
        ans += vst[x]

    for j in range(2 * ALPHA):
        key = x ^ (1 << j)
        if key in vst:
            ans += vst[key]

    if x in vst:
        vst[x] += 1
    else:
        vst[x] = 1

print(ans)
