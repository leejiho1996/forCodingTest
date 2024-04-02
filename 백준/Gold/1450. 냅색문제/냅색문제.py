# 냅색 문제 (투포인터)
import sys
input = sys.stdin.readline

n, c = map(int,input().split())

item = list(map(int,input().split()))
half = len(item)//2

front_item = item[:half]
back_item = item[half:]

def find_part_sum(arr):
    part_sum = [0]
    for i in range(len(arr)):
        for j in range(len(part_sum)):
            part_sum.append(part_sum[j] + arr[i])
    return part_sum


front_sum = find_part_sum(front_item)
back_sum = find_part_sum(back_item)

back_sum.sort()

cnt = 0

for i in front_sum:
    if c-i >= 0:
        target = c-i
        start = 0
        end = len(back_sum) - 1
        while start <= end:
            
            mid = (start+end)//2
            if target >= back_sum[mid]:
                start = mid + 1
            else:
                end = mid - 1
                
        cnt += (start) # 인덱스 임으로 +1 해줘야함 ex) idx가 2일때 최대이면 총 3개가 정답

print(cnt)