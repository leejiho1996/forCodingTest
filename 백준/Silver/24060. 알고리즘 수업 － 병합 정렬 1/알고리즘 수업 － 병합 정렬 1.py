#병합정렬
import sys
input = sys.stdin.readline

a, b = map(int,input().split())

array = list(map(int,input().split()))

start = 0
end = len(array)-1

def merge_sort(array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid+1, end)
        merge(array, start, mid, end)

tmp = [0]*500001
cnt = 0
def merge(array, start, mid, end):
    global cnt
    global tmp
    i = start
    j = mid + 1
    t = 0
    while i <= mid and j <= end:
        if array[i] <= array[j]:
            tmp[t] = array[i]
            t += 1
            i += 1
        else:
            tmp[t] = array[j]
            t += 1
            j += 1
    while i <= mid:
        tmp[t] = array[i]
        t += 1
        i += 1
    while j <= end:
        tmp[t] = array[j]
        t += 1
        j += 1
    i = start
    t = 0
    while i <= end:
        cnt += 1
        if cnt == b:
            print(tmp[t])
            exit()
        array[i] = tmp[t]
        i += 1
        t += 1

merge_sort(array, start, end)

print(-1)
        
