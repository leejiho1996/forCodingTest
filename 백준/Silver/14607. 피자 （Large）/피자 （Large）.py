# 피자(Large)

def divide(N):
    if N == 2:
        return 1
    elif N == 1:
        return 0
    
    part1 = N // 2
    part2 = N - part1

    mul = part1 * part2
    
    if N % 2 == 0:
        return mul + divide(part1) * 2
    else:
        return mul + divide(part1) + divide(part2)
    
result = 0
N = int(input())

print(divide(N))
