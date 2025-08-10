# Min Max Mex
import sys
input = sys.stdin.readline

# Mex(A) -> 배열 A에 포함되어 있지 가장 작은 음이 아닌 정수
N, K = map(int,input().split())

nums = list(map(int,input().split()))

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

# 가능한 작은 수는 최대 N
minn = N
for i in range(N):
    # dic에 없거나 제거할 수 있다면 해당 숫자가 최솟값
    if i not in dic or dic[i] <= K:
        minn = i
        break

print(minn) # 최소값 출력


prev = -1 # 가능한 최솟값이 0이니 초기 prev는 -1
check = False
for i in range(len(set_list)):
    # 이전 값과 현재 값 사이에 넣어야하는 숫자 갯수
    fill = set_list[i] - prev - 1
    
    if fill == 0: # 채울 필요가 없으면 패스
        prev = set_list[i]
        continue

    # K번의 연산으로 채울 수 없다면 break
    if K - fill < 0:
        check = True
        break
    else: # 채울 수 있다면 다음 값을 넘어간다
        K -= fill
        prev = set_list[i]

# break 되었다면 이전 값에 (K+1) 
if check:
    print(prev + (K+1))
else: # 아니라면 마지막 값에 K+1
    print(set_list[-1] + (K+1))

