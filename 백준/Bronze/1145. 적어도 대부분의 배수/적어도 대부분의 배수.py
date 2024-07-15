a = list(map(int, input().split()))
n = min(a)

# 가장 작은 수의 배수 중에서 가장 큰 수까지 
while True:
    cnt = 0
    for num in a:
        if n % num == 0:
            cnt += 1
        if cnt > 2:
            print(n)
            break
    if cnt > 2:
        break
    n += 1