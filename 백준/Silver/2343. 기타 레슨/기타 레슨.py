# 기타레슨
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

lesson = list(map(int,input().split()))

start = max(lesson)
end = sum(lesson)

while start <= end:
    mid = (start+end)//2
    
    blueray = []
    summ = 0
    for i in lesson:
        if summ + i <= mid:
            summ += i
              
        else:
            blueray.append(summ)
            summ = i

    blueray.append(summ)
    
    if m >= len(blueray):
        end = mid - 1
    else:
        start = mid + 1

print(end+1)