from math import factorial
n=int(input())
l=[int(input()) for _ in range(n)]
k=int(input())
list1=[(i%k,len(str(i))) for i in l]

dp=[[0]*k for _ in range(1<<n)]
dp[0][0]=1
length=[0]*(1<<n)
length[0]=1
for i in range(1<<n):
    for j in range(n):
        if i&(1<<j):
            continue
        bit=i|(1<<j)
        #시간 줄이기 1: length 리스트를 dp 리스트와 함께 갱신
        #시간 줄이기 2: length 리스트를 자릿수의 합이 아닌, 10^(자릿수의 합)%k로 설정
        if length[bit] != 0:
            pass
        else:
            length[bit] = length[i] * pow(10, list1[j][1], k) % k
        for m in range(k): #시간 줄이기 3: dp[bit]의 모든 원소를 한번에 갱신
            dp[bit][m] += dp[i][(m-list1[j][0] * length[i]) % k]

def gcd(a,b):
    r=a%b
    while r:
        a,b=b,r
        r=a%b
    return b

g=gcd(dp[-1][0],factorial(n))
print(f'{dp[-1][0]//g}/{factorial(n)//g}')
