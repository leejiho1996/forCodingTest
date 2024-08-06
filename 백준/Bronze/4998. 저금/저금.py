try:
    while True:
        n,b,m=map(float,input().strip().split())
        cnt=0
        while True:
            if n*(1+(b/100))**cnt>=m:break
            cnt+=1
        print(cnt)
except:
    exit()