# 풍선 터뜨리기

a = int(input())

balloon = list(map(int,input().split()))
bump = []
start = 0

for i, n in enumerate(balloon):
    balloon[i] = (i, n)

while balloon:
    bump.append(balloon[start][0]+1)

    if balloon[start][1] < 0:
        next_balloon = balloon[start][1]
    else:
        next_balloon = balloon[start][1] - 1

    del balloon[start]

    if not balloon:
        break
    
    start = (start + next_balloon) % len(balloon)


print(*bump)
    
