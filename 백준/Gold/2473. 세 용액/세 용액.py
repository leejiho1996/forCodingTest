# 세용액
import sys
input = sys.stdin.readline

n = int(input())
solution = list(map(int,input().split()))
solution.sort()

prev = 3000000001

start = 0
end = n - 1

for i in range(n-2):
    start = i
    end = n-1
    mid = i+1
    while mid < end:
        sum_sol = solution[start] + solution[mid] + solution[end]

        if abs(sum_sol) < prev:
            prev = abs(sum_sol)
            result = [solution[start], solution[mid], solution[end]]
            
        if sum_sol > 0: 
            end -= 1
        elif sum_sol < 0:
            mid += 1
        else:
            break

print(*result)
