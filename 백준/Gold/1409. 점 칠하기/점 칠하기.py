import sys

input = sys.stdin.readline

ang = [0] * 360

n = int(input())
for _ in range(n):
    x = int(input())
    ang[x] = 1

max_cnt = 0
for diff in range(1, 181):
    cnt = 0
    use = [0] * 360
    for start in range(181):
        if use[start]:
            continue

        cur = start
        length = 0
        lens = []

        while True:
            if ang[cur]:
                length += 1
            else:
                lens.append(length)
                length = 0

            use[cur] = 1
            cur = (cur + diff) % 360

            if cur == start:
                break

        if not lens:
            lens.append(length)
        else:
            lens[0] += length

        for e in lens:
            cnt += (e // 2) * 2

    max_cnt = max(max_cnt, cnt)

print(max_cnt)
