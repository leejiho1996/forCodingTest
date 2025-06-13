# XOR
import sys
input = sys.stdin.readline

def cal(num, lis):

    div = 1
    while div <= num:
        cnt = 0

        start = num - (div-1)
        times = start // div
        resi = start % div

        cnt += (times+1) // 2 * div

        if times % 2 == 0:
            cnt += resi

        lis.append(cnt)
        
        div *= 2

T = int(input())

for i in range(T):
    S, F = map(int,input().split())

    listS = []
    listF = []

    cal(S-1, listS)
    cal(F, listF)

    for i in range(len(listS)):
        listF[i] -= listS[i]

    result = ""
    for i in listF:
        if i % 2 == 1:
            result += "1"
        else:
            result += "0"

    print(int(result[::-1], 2))
