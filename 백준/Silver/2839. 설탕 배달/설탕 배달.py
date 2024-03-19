a = int(input())
cnt = 0
while True:
    if a % 5 == 0:
        cnt += a // 5
        a -= (a//5) * 5
    if a < 3:
        break
    a -= 3
    cnt +=1
    
if a != 0:
    print(-1)
else:
    print(cnt)