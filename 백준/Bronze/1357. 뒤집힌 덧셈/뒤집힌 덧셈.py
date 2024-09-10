def Rev(num):
    return int(str(num)[::-1])

x, y = map(int, input().split())
print(Rev(Rev(x) + Rev(y)))