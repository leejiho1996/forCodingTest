time = 0
exercise = 0
N,m,M,T,R = list(map(int, input().split()))
X=m
if(M-m < T):
  print(-1)
else:
  while exercise < N:
    if(X+T <= M):
      time += 1
      exercise += 1
      X += T
    else:
      time += 1
      X -= R
      if X < m:
        X=m
  print(time)
