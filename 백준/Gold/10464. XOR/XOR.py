# XOR
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    S, F = map(int,input().split())

    bitCnt = []

    div = 1
    while div <= F:
        cnt = 0

        nums = F - (div - 1) # 해당열의 비트가 첫번째로 켜지는 숫자
        times = nums // div # 해당열의 비트가 꺼지고 켜지는 횟수
        resi = nums % div # 비트열이 잘린 경우
        
        # 비트열이 꺼지고 켜진 횟수의 절반반 켜진 상태
        cnt += (times+1) // 2 * div
        
        if times % 2 == 0: # 짝수 번일때만 비트가 켜진경우므로 resi 더해줌
            cnt += resi

        bitCnt.append(cnt)

        div *= 2

    div = 1
    idx = 0
    while div <= S-1:
        cnt = 0

        nums = S - 1 - (div - 1)
        times = nums // div
        resi = nums % div

        cnt += (times+1) // 2 * div

        if times % 2 == 0:
            cnt += resi

        bitCnt[idx] -= cnt

        div *= 2
        idx += 1

    result = ""
    for i in bitCnt:
        if i % 2 == 1:
            result += "1"
        else:
            result += "0"

    print(int(result[::-1], 2))
