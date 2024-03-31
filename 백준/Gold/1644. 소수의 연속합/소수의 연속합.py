# 소수의 연속합
import sys
input = sys.stdin.readline

n = int(input())

sosu = [True] * (n+1)
sosu[1] = False
sosu[0] = False

m = int((n)**(0.5))

for i in range(2, m+1):
    if sosu[i] == False:
        continue
    cnt = 2
    check = 0
    num = i
    while cnt < num**(0.5):
        if i%cnt == 0:
            break
        else:
            cnt += 1
            
    if check == 0:
        num = i+i
        while num <= n:
            sosu[num] = False
            num += i

acc = 0
num_list = [0]
for i in range(2, n+1):
    if sosu[i] == True:
        acc += i
        num_list.append(acc)

start = 0
end = 1
result = 0

while start <= end and end <= len(num_list)-1:
    cur = num_list[end] - num_list[start]
    if cur == n:
        result += 1
    if cur <= n:
        end += 1
    else:
        start += 1

print(result)