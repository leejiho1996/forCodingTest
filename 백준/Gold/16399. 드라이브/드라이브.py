from collections import deque
import sys
input=sys.stdin.readline
F=lambda:[*map(int,input().split())]

C,E,D=F()
N=int(input())
X=F()
for i in range(1,N):X[i]+=X[i-1]
for i in range(N):X[i]*=E
D*=E
P=F()

ans=x=i=0; c=C
DQ=deque([])
while x<D:
  if i<N and X[i]==x:
    p=P[i]
    while DQ and P[DQ[-1]]>=p:DQ.pop()
    DQ.append(i)
    i+=1
  if DQ and X[DQ[0]]+C<=x:DQ.popleft()
  if c>0:c-=1;x+=1
  elif not DQ:print(-1);quit()
  else:
    ans+=P[DQ[0]]
    x+=1
print(ans)