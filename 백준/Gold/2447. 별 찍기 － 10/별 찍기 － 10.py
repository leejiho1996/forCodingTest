# 별찍기

n = int(input())

def star(n):
    if n == 3:
        return ["***", "* *", "***"]

    array = []
    recur = star(n//3)
    for i in range(3):
        for j, n in enumerate(recur):
            if i == 1:
                array.append(n + ' '*len(n) + n)
                continue
            array.append(n*3)
    return array

print('\n'.join(star(n)))