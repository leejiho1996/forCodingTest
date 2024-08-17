n = int(input())
s = ""
for _ in range(2 * n - 1):
    w = input()
    if w == '/':
        w = '//'
    s += w
print(eval(s))