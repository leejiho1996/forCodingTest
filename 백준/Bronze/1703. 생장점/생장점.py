while(1):
    line = list(map(int, input().split()))
    if (line[0] == 0):     # end if zero-input
        break

    seq = line[1:]
    size = line[0]

    sum = 1
    for i in range(0, size * 2, 2):
        sum = sum * seq[i] - seq[i + 1]

    print(sum)
