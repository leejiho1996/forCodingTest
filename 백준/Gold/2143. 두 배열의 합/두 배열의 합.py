import sys
input = sys.stdin.readline

t = int(input())

n = int(input())
n_num = list(map(int,input().split()))
n_part = []

m = int(input())
m_num = list(map(int,input().split()))


for i in range(n):
    n_part.append(n_num[i])
    total = n_num[i]
    for j in range(i+1, n):
        total += n_num[j]
        n_part.append(total)

dic = {}

for i in range(m):
    total = m_num[i]
    if m_num[i] in dic:
        dic[m_num[i]] += 1
    else:
        dic[m_num[i]] = 1

    for j in range(i+1, m):
        total += m_num[j]
        if total in dic:
            dic[total] += 1
        else:
            dic[total] = 1

cnt= 0
for i in n_part:
    if t - i in dic:
        cnt += dic[t-i]

print(cnt)