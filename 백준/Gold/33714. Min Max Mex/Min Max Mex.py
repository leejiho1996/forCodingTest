# Min Max Mex
import sys
input = sys.stdin.readline

# Mex(A) -> 배열 A에 포함되어 있지 가장 작은 음이 아닌 정수
N, K = map(int,input().split())

nums = list(map(int,input().split()))
nums.sort()

sett = set(nums)
set_list = list(sett)
set_list.sort()

dic = {}

for i in range(N):
    num = nums[i]
    
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

minn = 200000
for i in range(200000):
    if i not in dic or dic[i] <= K:
        minn = i
        break

print(minn)

prev = -1
check = False
for i in range(len(set_list)):
    fill = set_list[i] - prev - 1
    
    if fill < 1:
        prev = set_list[i]
        continue
    
    if K - fill < 0:
        check = True
        break
    else:
        K -= fill
        prev = set_list[i]

if check:
    print(prev + (K+1))
else:
    print(set_list[-1] + (K+1))

