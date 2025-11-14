# 카드 바꾸기
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))
maxx = 0

for i in range(N):
    cur = nums[i]
    dic = {}
    
    left = i-1
    right = i+1
    
    while left >= 0:
        if (cur - nums[left]) % (i - left) == 0:
            gap = (cur - nums[left]) // (i-left)

            if gap in dic:
                dic[gap] += 1
            else:
                dic[gap] = 1

        left -= 1
        
    while right < N:
        if (nums[right] - cur) % (right - i) == 0:
            gap = (nums[right] - cur) // (right-i)

            if gap in dic:
                dic[gap] += 1
            else:
                dic[gap] = 1

        right += 1
    
    for k in dic.keys():
        maxx = max(dic[k], maxx)

print(N - (maxx+1))
    
