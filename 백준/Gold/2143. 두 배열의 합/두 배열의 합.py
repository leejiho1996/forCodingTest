import sys
input = sys.stdin.readline

t = int(input())

n = int(input())
n_num = list(map(int,input().split()))
n_part = []

m = int(input())
m_num = list(map(int,input().split()))
m_part = []

for i in range(n):
    n_part.append(n_num[i])
    total = n_num[i]
    for j in range(i+1, n):
        total += n_num[j]
        n_part.append(total)
n_part.sort()

dic = {}

for i in range(m):
    m_part.append(m_num[i])
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
        m_part.append(total)

m_part.sort()

cnt= 0
for i in n_part:
    if t - i in dic:
        cnt += dic[t-i]

print(cnt)
