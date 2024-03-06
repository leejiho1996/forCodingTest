# 하노이 탑 이동 순서

a = int(input())

# msg = "{}번 원반을 {}에서 {}로 이동"

def move(N, start, end):
    print(start, end)

def hanoi(N, start, end ,sub):
    if N == 1:
        move(1, start, end)
    else:
        hanoi(N-1, start, sub, end) # a에 있는 원반을 c를 거쳐 b에 옮긴다
        move(N, start, end) # 마지막 원반을 c에 옮긴다
        hanoi(N-1, sub, end, start) # b에 있는 원반을 a를 거쳐 c로 옮긴다.

print(2**a - 1)

hanoi(a,"1","3","2")