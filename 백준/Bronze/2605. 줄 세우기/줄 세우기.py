# 입력
N = int(input())
numlist = list(map(int, input().split()))

# 줄세우기
res = []
for idx, order in enumerate(numlist, 1):
    res.insert((idx-1) - order, idx)

# 출력
for i in res:
    print(i, end=" ")