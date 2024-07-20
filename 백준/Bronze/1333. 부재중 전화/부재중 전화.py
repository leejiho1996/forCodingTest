N, L, D = map(int, input().split())
time1 = []
for i in range(N):
    for j in range((L+5)*i+L, (L+5)*(i+1)):
        time1.append(j)
time2 = []
count1 = 0
while (N*L+5*(N-1)) >count1:
    count1 += D
    time2.append(count1)
time3 = []
for i in time1:
    for j in time2:
        if i == j:
            time3.append(i)
if len(time3) != 0:
    print(time3[0])
else:
    print(time2[-1])