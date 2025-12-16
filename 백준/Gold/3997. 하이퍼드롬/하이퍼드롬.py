import sys
input = sys.stdin.readline

N = int(input().strip())

ans = 0
m1 = {} # 홀수
m2 = {0: 1} # 짝수

bef_bits = 0
word = input().rstrip()

for i in range(N):
    s = word[i]

    if 'a' <= s:
        val = ord(s) - ord('a') + 26
    else:
        val = ord(s) - ord('A')

    bits = (1 << val)
    bits ^= bef_bits
    bef_bits = bits

    if i % 2 == 0: # 짝수
        if bits in m1:
            ans += m1[bits]

        for j in range(52):
            odd = bits ^ (1 << j)

            if odd in m2:
                ans += m2[odd]
    else: # 홀수
        if bits in m2:
            ans += m2[bits]

        for j in range(52):
            odd = bits ^ (1 << j)

            if odd in m1:
                ans += m1[odd]

    if i % 2 == 0:
        if bits in m1:
            m1[bits] += 1
        else:
            m1[bits] = 1
    else:
        if bits in m2:
            m2[bits] += 1
        else:
            m2[bits] = 1

print(ans)
