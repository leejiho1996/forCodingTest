# List of Unique Numbers
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int,input().split()))

visited = [0] * 100001
start, end = 0, 0
visited[num[0]] = 1
result = 0

for i in range(1, n):
    number = num[i]
    end += 1
    
    if visited[number]:
        while True:
            result += (end - start)

            if num[start] == number:
                start += 1
                break

            visited[num[start]] = 0
            start += 1
    else:
        visited[number] = 1
        
    if i == n-1:
        result += ((end - start + 1) * (end - start + 2)//2)

print(result)